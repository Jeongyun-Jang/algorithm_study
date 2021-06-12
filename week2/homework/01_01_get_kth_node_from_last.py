#방법1
# 1)LinkedList 길이 전부 알아내기
# 2)그 길이에서 k 만큼 뺀 길이만큼 이동

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

    def get_kth_node_from_last(self, k):
        #전체 길이 알아낸 후 뒤에서 k번째 까지 이동
        length = 1
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            length += 1
        #--------------
        end_length = length - k
        cur = self.head
        for i in range(end_length):
            cur = cur.next
        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
#[6]->[7]->[8]
print(linked_list.get_kth_node_from_last(2).data)  # 뒤에서 2번째인 7 출력
