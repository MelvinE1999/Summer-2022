# FIFO (First In First Out)

class QueueOverflowError(BaseException):
    pass

class QueueUnderflowError(BaseException):
    pass

class queue:
    def __init__(self, maxCap:int) -> None:
        self.q = []
        self.size = 0
        self.maxSize = maxCap
    
    def __repr__(self) -> str:
        return str(self.q)
    
    def enqueue(self, item):
        if self.size == self.maxSize:
            raise QueueOverflowError

        self.q.append(item)
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            raise QueueUnderflowError
        
        item = self.q.pop(0)
        self.size -= 1
        return item
    
    def peek(self):
        return self.q[0]
    
    def size(self):
        return self.size

    def maxSize(self):
        return self.maxSize
    
    def contains(self, item):
        return item in self.q
    
    def isFull(self):
        return self.size == self.maxSize

    def isEmpty(self):
        return self.size == 0