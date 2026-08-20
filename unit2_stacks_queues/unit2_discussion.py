"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None

        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO: TECHNICIAN ACTION HISTORY ===")

    action_stack = Stack()

    print("Adding technician actions to the stack:")
    action_stack.push("Open support ticket")
    action_stack.push("Reset user password")
    action_stack.push("Update user account")
    action_stack.push("Close support ticket")

    print("1. Open support ticket")
    print("2. Reset user password")
    print("3. Update user account")
    print("4. Close support ticket")

    print("\nTop action using peek():", action_stack.peek())

    print("\nUndoing actions demonstrates LIFO:")
    while not action_stack.is_empty():
        print("Undo:", action_stack.pop())

    print("\nThe newest action was removed first, demonstrating LIFO.")

    # Test pop on an empty stack
    empty_pop = action_stack.pop()
    if empty_pop is None:
        print("Empty stack pop: No actions are available to remove.")

    # Test peek on an empty stack
    empty_peek = action_stack.peek()
    if empty_peek is None:
        print("Empty stack peek: No action is available to view.")

    # Single-item stack edge case
    single_stack = Stack()
    single_stack.push("Restart server")
    print("\nSingle-item stack contains: Restart server")
    print("Removed:", single_stack.pop())
    print("Is the single-item stack empty?", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: INCOMING SUPPORT TICKETS ===")

    ticket_queue = Queue()

    print("Adding support tickets to the queue:")
    ticket_queue.enqueue("Ticket 101 - Password reset")
    ticket_queue.enqueue("Ticket 102 - Printer problem")
    ticket_queue.enqueue("Ticket 103 - Software update")
    ticket_queue.enqueue("Ticket 104 - Network connection")

    print("1. Ticket 101 - Password reset")
    print("2. Ticket 102 - Printer problem")
    print("3. Ticket 103 - Software update")
    print("4. Ticket 104 - Network connection")

    print("\nNext ticket using front():", ticket_queue.front())

    print("\nProcessing tickets demonstrates FIFO:")
    while not ticket_queue.is_empty():
        print("Process:", ticket_queue.dequeue())

    print("\nThe oldest ticket was processed first, demonstrating FIFO.")

    # Test dequeue on an empty queue
    empty_dequeue = ticket_queue.dequeue()
    if empty_dequeue is None:
        print("Empty queue dequeue: No tickets are available to process.")

    # Test front on an empty queue
    empty_front = ticket_queue.front()
    if empty_front is None:
        print("Empty queue front: No ticket is available to view.")

    # Single-item queue edge case
    single_queue = Queue()
    single_queue.enqueue("Ticket 105 - Email problem")
    print("\nSingle-item queue contains: Ticket 105 - Email problem")
    print("Processed:", single_queue.dequeue())
    print("Is the single-item queue empty?", single_queue.is_empty())

if __name__ == "__main__":
    main()
