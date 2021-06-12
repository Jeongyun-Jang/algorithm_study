class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None #head 만 가지고 있으며, 이를 이용해 삽입삭제할 데이터로 이동하는 과정이 진행됨

    def push(self, value):
        new_head = Node(value) #새로운 헤드의 값을 만들고
        new_head.next = self.head #새로운 헤드의 next가 현재 있는 헤드를 가리키도록
        self.head = new_head
        return

    def pop(self):
        if self.is_empty():
            return "stack id Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "stack id Empty"
        return self.head.data

    def is_empty(self):
        return self.head is None
stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
stack.pop()
print(stack.peek())