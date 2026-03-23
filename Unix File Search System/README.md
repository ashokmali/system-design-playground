# Unix File Search System

Imagine you’re a developer trying to find specific files on a Unix system, like files owned by a user, or text files matching a pattern, buried deep in a directory structure. You run a search command, specify your criteria, and the system returns matching files quickly. Behind the scenes, it’s recursively traversing directories, evaluating file attributes, and applying your filters efficiently. Let’s design a Unix File Search system that handles this process.

## 1) Functional Requirements

- The search system can search for files based on attributes such as size, type, filename, and owner.
- The search system supports comparison types depending on the attribute: ‘equals’ and ‘regex match’ for strings, and ‘greater than’, ‘equals’, and ‘less than’ for numbers.
- The system can combine multiple search criteria using logical operators (and, or, not).
- The file search system can perform recursive searches within directories.
- The search system can apply search criteria to directories as well as files.

## 2) Non-functional Requirements

- Scalability: Efficiently handle large directory trees with thousands or millions of files using resource-efficient traversal strategies.
- Extensibility: Support adding new attributes (e.g., modification time) and comparison operators without altering core traversal or filtering logic.
- Separation of concerns: Keep traversal logic separate from filtering logic for a modular and maintainable design.

## 3) Core Objects

- **_File_** : A file object with it's attributes
- **_Directory_** : A folder object with it's attributes and collection of entries
- **_ComparisonOperator_** : An interface defining how attribute values are compared, with implementations like EqualsOperator, RegexMatchOperator, GreaterThanOperator, and LessThanOperator.
- **_Predicate_** : An interface defining the contract for evaluating whether a File matches a condition, enabling both simple checks (e.g., "size > 10") and composite conditions (e.g., AND, OR, NOT). We separate Predicate from FileSearchCriteria to isolate comparisons and logical combinations from how FileSearch uses the criteria. This keeps FileSearchCriteria a lightweight wrapper, while Predicate manages the complex logic.
- **_SimplePredicate_** : Implements Predicate to compare one file attribute (e.g., "size > 10") against a value with an operator (e.g., equals, greater than).
- **_CompositePredicate_** : Extends Predicate for combining conditions (e.g., AND, OR, NOT) with implementations like AndPredicate, OrPredicate, and NotPredicate. It supports complex queries, such as "size > 10 AND owner = 'bob'".
- **_FileSearchCriteria_** : Encapsulates a search condition and determines whether a given File matches it by delegating to a Predicate. This wrapper class decouples the search execution logic (FileSearch) from the condition evaluation logic (Predicate), promoting separation of concerns and greater flexibility.
- **_FileSearch_** : The central entity managing the search process, serving as the entry point into our application logic. It recursively traverses the filesystem from a starting File (directory) and returns matches based on a FileSearchCriteria object.
