from abc import ABC, abstractmethod
from file_system import FileSystem
from comparison_operator import ComparisonOperator
from typing import Callable, Iterable

class Predicate(ABC):

    @abstractmethod
    def is_match(self, input_file: FileSystem) -> bool:
        pass


class SimplePredicate(Predicate):

    def __init__(self, attribute_name: Callable[[FileSystem], object], operator: ComparisonOperator, expected_value: object) -> None:
        self._attribute_name = attribute_name
        self._operator = operator
        self._expected_value = expected_value

    def is_match(self, input_file: FileSystem) -> bool:
        actual_value = self._attribute_name(input_file)
        if not isinstance(actual_value, type(self._expected_value)):
            return False

        return self._operator.is_match(actual_value, self._expected_value)



class CompositePredicate(Predicate, ABC):
    pass



class AndPredicate(CompositePredicate):
    def __init__(self, predicates: Iterable[Predicate]):
        self._predicates = list(predicates)

    def is_match(self, entity) -> bool:
        return all(p.is_match(entity) for p in self._predicates)



class OrPredicate(CompositePredicate):
    def __init__(self, predicates: Iterable[Predicate]):
        self._predicates = list(predicates)

    def is_match(self, entity) -> bool:
        return any(p.is_match(entity) for p in self._predicates)



class NotPredicate(CompositePredicate):
    def __init__(self, predicate: Predicate):
        self._predicate = predicate

    def is_match(self, entity) -> bool:
        return not self._predicate.is_match(entity)