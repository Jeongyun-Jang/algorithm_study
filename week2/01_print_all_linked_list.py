#[3]->[4]
#data, next

class Node:
    def __init__(self,data):
        self.data = data #데이터 주입
        self.next = None #처음 생성시에는 가리키는것이 없으므로

node = Node(3)
first_node = Node(4)
node.next = first_node
#print(node.next.data)#4
#print(node.data)#3

class LinkedList: #only head노드만 가지고 있으면 됨
    def __init__(self,data):
        self.head = Node(data) #생성자만 담기면 됨
    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            return

        #self.head.next = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next #[3]->[4]->[5]
                           #     cur
            print("cur is ", cur.data)#so cur.data가 4가 됨
        cur.next = Node(data)


    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
#[3] -> [4] -> [5] -> [6] -> None

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()
