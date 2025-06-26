'''
Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
'''
class MyQueue:
    # With a single deque (Time: O(1) / Space: O(n))
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue

    # Solution that uses two deques (Time: O(1) / Space: O(n))
    def __init__(self):
        self.stackin = deque()
        self.stackout = deque()

    def push(self, x: int) -> None:
        self.stackin.append(x)

    def pop(self) -> int:
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.popleft())
        return self.stackout.popleft()

    def peek(self) -> int:
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.popleft())
        return self.stackout[0]

    def empty(self) -> bool:
        return not self.stackin and not self.stackout
