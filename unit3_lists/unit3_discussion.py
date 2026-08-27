"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # insert() places the new value at the requested index.
    # Elements at and after the index shift one position to the right.
    # Inserting near the beginning can take longer because more items
    # may need to shift. Inserting at the end requires less shifting.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Check that the index is valid before trying to remove an item.
    # This prevents the program from crashing because of an invalid index.
    if index < 0 or index >= len(lst):
        return None

    # pop() removes the item and returns the value that was removed.
    # Items after the removed item shift one position to the left.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because the list is checked one item at a time.
    # The search starts at index 0 and moves forward until the value is found.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return -1 when the entire list has been searched
    # and the requested value was not found.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Create and display the original list.
    numbers = [10, 20, 30, 40]
    print("Original list:", numbers)

    # Insert 5 at the beginning.
    # All existing items shift one position to the right.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Insert 25 into the middle of the list.
    # Items at and after index 3 shift to the right.
    insert_at(numbers, 3, 25)
    print("After inserting 25 in the middle:", numbers)

    # Use len(numbers) to insert 50 at the end.
    insert_at(numbers, len(numbers), 50)
    print("After inserting 50 at the end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Create a new list for the deletion tests.
    delete_list = [100, 200, 300, 400, 500]
    print("Original list:", delete_list)

    # Delete the first item in the list.
    removed = delete_at(delete_list, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", delete_list)

    # Find the current middle index and remove that item.
    middle_index = len(delete_list) // 2
    removed = delete_at(delete_list, middle_index)
    print("Removed from middle:", removed)
    print("Updated list:", delete_list)

    # Delete the last item using length - 1.
    removed = delete_at(delete_list, len(delete_list) - 1)
    print("Removed from end:", removed)
    print("Updated list:", delete_list)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    search_list = [11, 22, 33, 44, 55]
    print("Search list:", search_list)

    # Search for an item that exists in the list.
    found_index = search_value(search_list, 33)
    print("Searching for 33 returned index:", found_index)

    # Search for an item that does not exist.
    # The expected result is -1.
    missing_index = search_value(search_list, 99)
    print("Searching for 99 returned index:", missing_index)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1:
    # Try to delete using an index that does not exist.
    edge_list = [1, 2, 3]
    print("Original edge-case list:", edge_list)

    invalid_removed = delete_at(edge_list, 10)
    print("Delete using invalid index 10 returned:", invalid_removed)
    print("List after invalid deletion:", edge_list)

    # Edge case 2:
    # Try to delete from an empty list.
    empty_list = []

    empty_removed = delete_at(empty_list, 0)
    print("Delete from empty list returned:", empty_removed)

    # Edge case 3:
    # Insert an item into an empty list.
    insert_at(empty_list, 0, "First item")
    print("Empty list after insertion:", empty_list)

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SCENARIO: MUSIC PLAYLIST ===")

    # A music playlist is a real-world example of a list because songs
    # have an order and can be inserted, removed, and searched.
    playlist = ["Song A", "Song B", "Song C"]
    print("Original playlist:", playlist)

    # Insert a new song into the playlist.
    insert_at(playlist, 1, "Song X")
    print("After inserting Song X:", playlist)

    # Search for a song.
    song_index = search_value(playlist, "Song C")
    print("Song C found at index:", song_index)

    # Remove the first song.
    removed_song = delete_at(playlist, 0)
    print("Removed song:", removed_song)
    print("Updated playlist:", playlist)


if __name__ == "__main__":
    main()