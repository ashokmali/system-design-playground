import hashlib
import bisect
from typing import List, Dict, Optional


class ConsistentHashing:
    """
    Consistent Hashing implementation using:
    - Sorted list for the hash ring
    - Dictionary for hash -> server lookup
    - Virtual nodes for better load balancing
    """

    def __init__(self, servers: Optional[List[str]] = None, virtual_nodes: int = 128):

        self.ring: List[int] = []      # Sorted list of servers
        self.hash_to_server: Dict[int, str] = {}
        self.virtual_nodes: int = virtual_nodes

        if servers:
            self.add_server(servers)

    def _hash(self, value: object) -> int:
        """
        Convert any object into a stable MD5 hash integer.
        """
        value_bytes = str(value).encode("utf-8")
        return int(hashlib.md5(value_bytes).hexdigest(), 16)

    def get_server(self, req_id: object) -> str:
        """
        Find the server responsible for a request id.
        """
        if not self.ring:
            raise ValueError("No servers available in the hash ring")

        req_hash = self._hash(req_id)
        idx = bisect.bisect_right(self.ring, req_hash)
        server_hash = self.ring[idx % len(self.ring)]   # covering ring's wrap around logic

        return self.hash_to_server[server_hash]

    def add_server(self, server_list: List[str]) -> None:
        """
        Add servers to the ring with virtual nodes.
        """
        for server in server_list:
            for i in range(self.virtual_nodes):
                vnode_key = f"{server}#{i}"
                server_hash = self._hash(vnode_key)

                bisect.insort(self.ring, server_hash)
                self.hash_to_server[server_hash] = server

    def remove_server(self, server_list: List[str]) -> None:
        """
        Remove servers and their virtual nodes from the ring.
        """
        for server in server_list:
            for i in range(self.virtual_nodes):
                vnode_key = f"{server}#{i}"
                server_hash = self._hash(vnode_key)

                if server_hash in self.hash_to_server:
                    self.ring.remove(server_hash)
                    del self.hash_to_server[server_hash]
