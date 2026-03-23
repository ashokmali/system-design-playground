from abc import ABC, abstractmethod


class FileSystem(ABC):
    def __init__(self, name: str, owner: str):
        self._name = name
        self._owner = owner

    @abstractmethod
    def get_size(self) -> float:
        pass

    def get_owner(self) -> str:
        return self._owner

    def get_name(self) -> str:
        return self._name


class File(FileSystem):
    def __init__(self, name: str, owner: str, size: float):
        super().__init__(name, owner)
        self._size = size

    def get_size(self) -> float:
        return self._size

    def __repr__(self):
        return f"File({self._name}, size={self._size})"


class Directory(FileSystem):
    def __init__(self, name: str, owner: str):
        super().__init__(name, owner)
        self._entries: set[FileSystem] = set()

    def add_entry(self, entry: FileSystem):
        self._entries.add(entry)

    def get_size(self) -> float:
        return sum(entry.get_size() for entry in self._entries)

    def get_entries(self) -> set[FileSystem]:
        return self._entries

    def __repr__(self):
        return f"Directory({self._name}, entries={len(self._entries)})"

