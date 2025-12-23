import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item} | Queue: {self.items}")

    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            print(f"Dequeued: {item} | Queue: {self.items}")
            return item
        else:
            print("Queue is empty, cannot dequeue.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            print("Queue is empty, no winner can be selected.")
            return None
        winner_index = random.randint(0, len(self.items) - 1)
        winner = self.items[winner_index]
        print(f"Winner selected: {winner}")
        for _ in range(winner_index + 1):
            self.dequeue()
        return winner
