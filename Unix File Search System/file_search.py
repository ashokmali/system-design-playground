from file_system import FileSystem
from file_search_criteria import FileSearchCriteria
from collections import deque

class FileSearch:

    def search(self, root: FileSystem, criteria: FileSearchCriteria) -> list[FileSystem]:
        result = []
        stack = deque([root])  # acts like ArrayDeque

        while stack:
            current = stack.pop()

            # Apply predicate
            if criteria.is_match(current):
                result.append(current)

            # Traverse children (if directory)
            if hasattr(current, "get_entries"):
                for entry in current.get_entries():
                    stack.append(entry)

        return result

