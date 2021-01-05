from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)

    def dequeue(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(6)
    queue.enqueue(4)
    queue.enqueue(9)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())
    print(queue.size())
