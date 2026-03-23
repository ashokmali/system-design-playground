from predicate import Predicate
from file_system import FileSystem

class FileSearchCriteria:

    def __init__(self, predicate: Predicate):
        self._predicate = predicate

    def is_match(self, input_file: FileSystem) -> bool:
        return self._predicate.is_match(input_file)
