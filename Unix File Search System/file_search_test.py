import unittest
from file_system import File, Directory
from predicate import SimplePredicate, AndPredicate
from comparison_operator import EqualsOperator, RegexMatchOperator
from file_search import FileSearch
from file_search_criteria import FileSearchCriteria

class FileSearchTest(unittest.TestCase):

    def test_file_search(self):
        # Create root directory
        root = Directory("root", "adam")

        # Create files
        a = File("a", "adam", 2000)
        b = File("b", "george", 3000)

        # Add to root
        root.add_entry(a)
        root.add_entry(b)

        # Build predicates
        is_file_pred = SimplePredicate(
            lambda f: isinstance(f, File),
            EqualsOperator(),
            True,
        )

        owner_pred = SimplePredicate(
            lambda f: f.get_owner(),
            RegexMatchOperator(),
            r"ge.*",
        )

        criteria = FileSearchCriteria(AndPredicate([is_file_pred, owner_pred]))

        # Execute search
        search = FileSearch()
        result = search.search(root, criteria)

        # Assertions
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_name(), "b")


if __name__ == "__main__":
    unittest.main()