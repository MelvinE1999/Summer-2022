
class node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self) -> str:
        return str(self.data)


class singleLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def __iter__(self):
        n = self.head
        while n:
            yield n.data
            n = n.next
    
    def __len__(self):
        return len(tuple(iter(self)))

    def insertHead(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def insertTail(self,data):
        newNode = node(data)
        tempHead = self.head
        for n in range(len(self) - 1):
            tempHead = tempHead.next
        newNode.next,tempHead.next = tempHead.next, newNode.next
    
    def popHead(self):
        node = self.head
        self.head = self.head.next
        return node

    def popTail(self):
        node = self.head
        tempHead = self.head
        for n in range(len(self) - 1):
            tempHead = tempHead.next
        node = tempHead.next
        tempHead.next = None
        return node
    
    def isEmpty(self):
        return self.head is None



