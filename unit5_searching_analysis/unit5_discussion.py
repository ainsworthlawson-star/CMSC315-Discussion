"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target, stats=None):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # stats is optional; normal two-argument calls still return only an index.
    # Examine one element at a time, beginning at index 0.
    # In the worst case, all n elements must be checked: O(n).
    for index in range(len(lst)):
        # Record one comparison of the target with a list value.
        if stats is not None:
            stats["comparisons"] += 1

        if lst[index] == target:
            return index

    # An empty list also reaches this return without any comparisons.
    return -1


def binary_search(lst, target, stats=None):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # low and high describe the remaining range of sorted values.
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = low + (high - low) // 2

        # Count one comparison of the target with the middle value.
        if stats is not None:
            stats["comparisons"] += 1

        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            # Discard the middle and the entire right half.
            high = mid - 1
        else:
            # Discard the middle and the entire left half.
            low = mid + 1

    # No matching value remains. This also handles an empty list.
    return -1


def run_search_case(label, values, target, expected_index):
    """Run both algorithms and explain their results and comparison counts."""
    print(f"\n{label}")
    print(f"Dataset size: {len(values):,}; target: {target}")

    for name, search_function in (
            ("Linear search", linear_search),
            ("Binary search", binary_search),
    ):
        stats = {"comparisons": 0}
        result = search_function(values, target, stats)

        # Check the expected answer so the demonstration is self-checking.
        if result != expected_index:
            raise AssertionError(
                f"{name}: expected {expected_index}, got {result}"
            )

        if result == -1:
            explanation = "not found (-1)"
        else:
            explanation = f"found at index {result}"

        print(f"{name}: {explanation}; {stats['comparisons']:,} comparisons")

    print("Both algorithms returned the expected result.")


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    print("Store inventory lookup using sorted product IDs.")
    print("A comparison means checking the target against one list value.")
    print("Linear search is O(n); binary search is O(log n) on sorted data.")

    # Keep track of all automated demonstration checks.
    # The helper raises an error if either search returns an unexpected index.
    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    # TODO: Create a small dataset and test both searches.
    # A small, sorted collection of product IDs represents a store inventory.
    # Both methods return indexes, not the product IDs themselves.
    small_ids = [1001, 1005, 1010, 1020, 1035, 1050, 1075]
    print("Product IDs:", small_ids)

    # An existing value and a missing value demonstrate both outcomes.
    run_search_case("Existing ID", small_ids, 1050, 5)
    run_search_case("Missing ID", small_ids, 1040, -1)

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # TODO: Create a larger dataset and compare results.
    # A larger sorted inventory provides a meaningful comparison.
    # The last ID makes linear search check every element.
    large_ids = list(range(100000, 110000))
    print(f"Product IDs: {large_ids[0]} through {large_ids[-1]}")
    run_search_case("Existing last ID", large_ids, 109999, 9999)
    run_search_case("Missing ID", large_ids, 110000, -1)

    # Binary search halves the remaining range, giving O(log n) work.
    # Linear search may check all n values, giving O(n) work.
    print("The large test shows why binary search scales better on sorted data.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # TODO: Demonstrate and explain edge cases.
    # Empty, single-element, boundary, and missing-value cases.
    # The empty list returns -1 without accessing an invalid index.
    run_search_case("Empty list", [], 1050, -1)
    run_search_case("Single element found", [1050], 1050, 0)
    run_search_case("Single element missing", [1050], 9999, -1)
    run_search_case("First position", small_ids, 1001, 0)
    run_search_case("Last position", small_ids, 1075, 6)
    run_search_case("Missing value", small_ids, 9999, -1)

    # Binary search requires sorted data. Linear search can still
    # find an item when a small inventory has not been organized.
    unsorted_ids = [1050, 1001, 1075, 1010]
    result = linear_search(unsorted_ids, 1075)
    if result != 2:
        raise AssertionError("Unsorted linear search returned the wrong index.")
    print(f"\nUnsorted inventory: {unsorted_ids}")
    print(f"Linear search found 1075 at index {result}.")
    print("Binary search was not used because this list is not sorted.")

    print("\nAll 20 sorted-data search checks and the unsorted-data check passed.")


if __name__ == "__main__":
    main()