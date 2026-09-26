"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


from dataclasses import dataclass
from random import Random
from time import perf_counter


@dataclass(frozen=True)
class RatedTitle:
    """A sample streaming title compared only by its viewer rating."""
    title: str
    rating: int

    # Compare ratings, not names. Equal-rated titles retain input order in
    # both stable sorting algorithms implemented below.
    def __lt__(self, other):
        return self.rating < other.rating

    def __gt__(self, other):
        return self.rating > other.rating

    def __le__(self, other):
        return self.rating <= other.rating


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Sort a COPY so callers can reuse their original viewing-score list.
    result = lst.copy()
    n = len(result)

    # After each pass, the greatest remaining value is at the end.
    for end in range(n - 1, 0, -1):
        swapped = False
        for index in range(end):
            # Strict > avoids moving equal-rated titles past one another:
            # the sort is stable. Each comparison is between neighbors.
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        # An entire pass without a swap means the list is sorted already.
        if not swapped:
            break
    return result


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # A zero- or one-element list is already sorted. Return a fresh list.
    if len(lst) <= 1:
        return lst.copy()

    # Divide and conquer: recursively sort each half, then merge them.
    midpoint = len(lst) // 2
    left = merge_sort(lst[:midpoint])
    right = merge_sort(lst[midpoint:])
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    merged = []
    left_pos = 0
    right_pos = 0

    # Take the smaller front element from the two already-sorted halves.
    while left_pos < len(left) and right_pos < len(right):
        if left[left_pos] <= right[right_pos]:
            # On a tie, take LEFT first to retain original relative order.
            merged.append(left[left_pos])
            left_pos += 1
        else:
            merged.append(right[right_pos])
            right_pos += 1

    # Only one half can have remaining elements; both are already sorted.
    merged.extend(left[left_pos:])
    merged.extend(right[right_pos:])
    return merged


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    # Original TODO prompt retained: print("TODO: Create an unsorted dataset and test both sorting algorithms.")
    # Real-world example: popularity scores for a small streaming playlist.
    small_scores = [88, 42, 95, 70, 42, 61, 99, 35, 70]
    original_small = small_scores.copy()
    bubble_small = bubble_sort(small_scores)
    merge_small = merge_sort(small_scores)
    print("Scenario: sorting a small streaming playlist by popularity score.")
    print("Original popularity scores:", small_scores)
    print("Bubble Sort result:      ", bubble_small)
    print("Merge Sort result:       ", merge_small)
    assert bubble_small == merge_small == sorted(small_scores)
    assert small_scores == original_small  # Both methods preserve the original.
    print("Both methods matched the expected ascending order; input unchanged.")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    # Original TODO prompt retained: print("TODO: Create a second dataset and compare sorting results.")
    # A larger streaming trending list with 2,000 DISTINCT view counts.
    # These counts differ from the small dataset's 0-100 popularity scores.
    large_view_counts = list(range(10_000, 12_000))
    Random(315).shuffle(large_view_counts)  # Reproducible random ordering.
    original_large = large_view_counts.copy()

    bubble_start = perf_counter()
    bubble_large = bubble_sort(large_view_counts)
    bubble_elapsed = perf_counter() - bubble_start

    merge_start = perf_counter()
    merge_large = merge_sort(large_view_counts)
    merge_elapsed = perf_counter() - merge_start

    assert bubble_large == merge_large == sorted(large_view_counts)
    assert large_view_counts == original_large
    print("Scenario: 2,000 trending-video view counts in random order.")
    print("Dataset size:", len(large_view_counts))
    print("Original first 10:", large_view_counts[:10])
    print("Bubble sorted first 10:", bubble_large[:10])
    print("Merge sorted first 10: ", merge_large[:10])
    print(f"Bubble Sort time: {bubble_elapsed:.6f} seconds")
    print(f"Merge Sort time:  {merge_elapsed:.6f} seconds")
    print("Both methods returned the same correct result; input unchanged.")
    print("Timing depends on the computer and is illustrative, not a guarantee.")
    print("Bubble Sort: O(n^2) average/worst; Merge Sort: O(n log n) worst.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Original TODO prompt retained: print("TODO: Demonstrate and explain edge cases.")
    cases = [
        ("Empty list", [], "Both functions should return an empty list."),
        ("One item", [42], "One item is already sorted."),
        ("Already sorted", [1, 2, 3, 4, 5], "Bubble Sort can stop after one swap-free pass."),
        ("Reverse sorted", [9, 7, 5, 3, 1], "Bubble Sort needs many adjacent swaps."),
        ("Duplicate scores", [7, 3, 7, 3, 7], "Equal values remain present in sorted order."),
        ("Nearly sorted", [10, 20, 30, 50, 40, 60], "Only a small adjustment is needed."),
    ]
    for label, values, explanation in cases:
        before = values.copy()
        bubble_result = bubble_sort(values)
        merge_result = merge_sort(values)
        assert bubble_result == merge_result == sorted(values)
        assert values == before
        print(f"\n{label}: {values}")
        print("  Bubble Sort:", bubble_result)
        print("  Merge Sort: ", merge_result)
        print("  Explanation:", explanation)
        print("  Result: PASS")

    # Stability matters in recommendation systems: identical ratings should
    # keep the content's earlier display order, rather than be rearranged.
    titles = [
        RatedTitle("Show A", 90),
        RatedTitle("Show B", 80),
        RatedTitle("Show C", 90),
        RatedTitle("Show D", 80),
    ]
    expected_title_order = ["Show B", "Show D", "Show A", "Show C"]
    for algorithm_name, algorithm in (("Bubble Sort", bubble_sort), ("Merge Sort", merge_sort)):
        result = algorithm(titles)
        names = [entry.title for entry in result]
        assert names == expected_title_order
        print(f"{algorithm_name} stable tie order: {names} - PASS")

    print("\nAll dataset, edge-case, and stability checks passed.")




if __name__ == "__main__":
    main()