class Stack:
    def __init__(self):
        self.stack = []

    # Push
    def push(self, val):
        self.stack.append(val)

    # Pop
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return -1
        return self.stack.pop()

    # Peek
    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]

    # Is Empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Is Full
    def isFull(self):
        return False  # Dynamic array in Python

    # Size
    def size(self):
        return len(self.stack)

    # Search / Contains
    def contains(self, key):
        return key in self.stack

    # Reverse Stack
    def reverse(self):
        self.stack.reverse()

    # Display
    def display(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(*self.stack)

    # Middle Element
    def middle(self):
        if self.isEmpty():
            return -1
        return self.stack[len(self.stack) // 2]

    # Merge Two Stacks
    def merge(self, other):
        merged = Stack()
        merged.stack = self.stack + other.stack
        return merged


if __name__ == "__main__":

    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)

    print("Stack:")
    s.display()

    print("Pop:", s.pop())

    print("Peek:", s.peek())

    print("Contains 20:", s.contains(20))
    print("Contains 100:", s.contains(100))

    print("Middle Element:", s.middle())

    s.reverse()
    print("After Reverse:")
    s.display()

    s2 = Stack()
    s2.push(60)
    s2.push(70)
    s2.push(80)

    print("Second Stack:")
    s2.display()

    s3 = s.merge(s2)

    print("Merged Stack:")
    s3.display()