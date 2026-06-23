import __main__
from inspect import stack


class Node:
    data = 0
    next = None
    def __init__(self, val):
        self.data = val

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        newnode = Node(val)
        if self.top == None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode
        self.size += 1
        return self.top

    def pop(self):
        if self.top == None:
            print("Stack is Underflow")
            return self.top
        temp = self.top
        self.top = self.top.next
        return temp
    
    def peek(self, top): 
        if self.top == None:
            return -1
        return self.top.data
    
    def reverse(self, top):
        turtle = None
        curr = self.top
        while curr != None:
            hare = curr.next
            curr.next = turtle
            turtle = curr
            curr = hare
        self.top = turtle
    
    def contains(self, top, key):
        if self.top == None:
            return False
        temp = top
        while temp != None:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def IsEmpty(self, top):
        if self.top == None:
            return True
        return False
    
    def IsFull(self, top):
        return False
    
    def mergetwostacks(self, st1, st2):
        if st1.top == None:
            return st2
        if st2.top == None:
            return st1
        top2 = st2.reverse(st2)      
        temp = top2
        while temp != None:
            node = temp.pop(temp)
            st1.push(st1,node.data)
            temp = temp.next
        return st1
    
    def display(self, top):
        if self.top == None:
            return
        temp = top  
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

    def middleOfStack(self, top):
        if top == None:
            return -1
        slow = top
        fast = top
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    #def AddTwoStack(self, top):

if __name__  == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.display(s.top)

    s2 = Stack()
    s2.push(12)
    s2.push(24)
    s2.push(36)
    s2.display(s2.top)

    s3 = Stack()

    s3 = s.mergetwostacks(s, s2)
    s3.display(s3.top)

    s.pop()
    print()
    s.display(s.top)
    print()

    print(s.peek(s.top))
    
    print()
    s.reverse(s.top)
    s.display(s.top)
    print()
    print(s.contains(s.top, 20))
    print(s.contains(s.top, 100))

    print(s.middleOfStack(s.top).data)

  
    
    
    