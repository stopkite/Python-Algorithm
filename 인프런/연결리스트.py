class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value





ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

ll.insert(2, 9)
