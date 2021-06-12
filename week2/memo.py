class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 3을 가진 Node 를 만드려면 아래와 같이 하면 됩니다!
node = Node(3) # 현재는 next 가 없이 하나의 노드만 있습니다. [3]

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)  # head 에 시작하는 Node 를 연결합니다.

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print("cur is",cur.data)
            cur = cur.next



linked_list = LinkedList(5)
print(linked_list.head) # <__main__.Node object at 0x0000024B7531B808> 출력
print(linked_list.head.data) # 5가 출력됩니다!
# 현재 LinkedList 는 (5) 만 존재합니다!

linked_list = LinkedList(12)
linked_list.print_all()