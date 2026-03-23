from abc import ABC, abstractmethod
import re

class ComparisonOperator(ABC):

    @abstractmethod
    def is_match(self, attribute_value: object, expected_value: object ) -> bool:
        pass


class EqualsOperator(ComparisonOperator):

    def is_match(self, attribute_value: object, expected_value: object) -> bool:
        return attribute_value == expected_value


class GreaterThanOperator(ComparisonOperator):

    def is_match(self, attribute_value: float, expected_value: float) -> bool:
        return attribute_value > expected_value


class LessThanOperator(ComparisonOperator):

    def is_match(self, attribute_value: float, expected_value: float) -> bool:
        return attribute_value < expected_value


class RegexMatchOperator(ComparisonOperator):

    def is_match(self, attribute_value: str, expected_value: str) -> bool:
        return re.fullmatch(expected_value, attribute_value) is not None