class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node #'index 번째 노드를 반환해보세요!' == 'next node'로 가는걸 index번 해야함을 뜻 함
    #  index   next_node
    # ["자갈"]->["밀가루"]->["우편"]
    #           new_node
    #         ->["흑연"]->
    # index.next = new_node
    # new_node = next_node
    def add_node(self, index, value):#이 함수는 index번째에 원소값 가진 node 넣기. so 인덱스 위치, 넣을 값 모두 받아와야함
        new_node = Node(value) #흑연칸
        if index == 0: #index가 0일 때 예외처리
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index-1) #흑연칸을 놓고 싶은 위치가  index라면 /  index-1인 자갈칸의 위치를 가져와야 원하는 곳에 넣을 수 있음
        next_node = node.next #next_node가 사라질 수 있어 '현재 노드의 다음것'으로 저장해두어야 함
        node.next = new_node #밀가루칸
        new_node.next = next_node
        return node
    #           index-1 ->  next_node -> next_node.next
    #["자갈"] -> ["흑연"] -> ["밀가루"] -> ["우편"] 에서 밀가루 빼기 위해서는 흑연.next를 우편으로 지정

    def delete_node(self,index):
        #[3] -> [5] -> [4]
        #head   head.next
        #[5] -> [4]
        #head
        if index == 0:
            self.head = self.head.next
            return

        node = self.get_node(index-1)
        node.next = node.next.next

linked_list = LinkedList(5)
linked_list.append(12)
#0번째 1번째 2번째 인덱스
#[5]->[12]->[8] 상황에 1번째에 6 삽입
linked_list.add_node(0,3)
linked_list.print_all()
linked_list.delete_node(0)
linked_list.print_all()