"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""
def display_inventory(title, inventory):
    """Display the current inventory in a readable format."""
    print(title)
    if not inventory:
        print("  Inventory is empty.")
        return

    for sku, quantity in inventory.items():
        print(f"  {sku} -> quantity {quantity}")

def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")
    print("Scenario: Warehouse inventory lookup using SKU numbers.")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    #print("TODO: Create a dictionary and add multiple key-value pairs.")
    # A Python dictionary behaves like a hash table. Each SKU is a key and
    # each quantity is its value. Python uses the key's hash value to guide
    # where the key-value pair is stored in the dictionary's internal table.
    # With a good distribution of hashes, insert and lookup operations are
    # O(1) on average.
    inventory = {}

    inventory["P100"] = 15
    inventory["P200"] = 9
    inventory["P300"] = 24
    inventory["P400"] = 7
    inventory["P500"] = 31

    display_inventory("Inventory after inserting 5 items:", inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    #print("TODO: Demonstrate successful key lookups.")
    print("Lookup P100 -> quantity", inventory["P100"])
    print("Lookup P400 -> quantity", inventory["P400"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    #print("TODO: Demonstrate updating an existing key.")
    display_inventory("Before updating P100:", inventory)

    # Assigning a new value to an existing key replaces the old quantity.
    # It does not create a duplicate SKU entry.
    inventory["P100"] = 20

    display_inventory("After updating P100 from 15 to 20:", inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    #print("TODO: Demonstrate deleting a key-value pair.")
    display_inventory("Before deleting P200:", inventory)

    # pop() removes the key-value pair and returns the removed value.
    removed_quantity = inventory.pop("P200")
    print(f"Removed P200, previous quantity was {removed_quantity}.")

    display_inventory("After deleting P200:", inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    #print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: get() safely returns None for a key that does not exist.
    missing_lookup = inventory.get("P999")
    print("Missing SKU lookup P999 ->", missing_lookup)
    print("Explanation: get() returned None instead of causing a KeyError.")

    # Edge case 2: pop(key, default) safely handles a missing key.
    size_before = len(inventory)
    missing_delete = inventory.pop("P999", None)
    size_after = len(inventory)
    print("Delete missing SKU P999 ->", missing_delete)
    print(f"Inventory size stayed {size_before} -> {size_after}.")

    # Edge case 3: An empty dictionary can be searched safely with get().
    empty_inventory = {}
    print("Lookup P100 in empty inventory ->", empty_inventory.get("P100"))
    print("Explanation: the empty dictionary returned None.")

    print("\n=== HASH TABLE PERFORMANCE ===")
    print("Dictionary keys are hashed to guide placement in an internal table.")
    print("Average insert, lookup, update, and delete operations are O(1).")
    print("A collision occurs when different keys compete for the same internal")
    print("location. Python resolves collisions internally, but many collisions")
    print("can require extra work and reduce lookup performance.")

    print("\n=== FINAL INVENTORY ===")
    display_inventory("Stored items:", inventory)


if __name__ == "__main__":
    main()