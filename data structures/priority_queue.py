# FIFO (First In First Out)
# follows by priority
# uses a two priority system

class QueueOverflowError(BaseException):
    pass

class QueueUnderflowError(BaseException):
    pass

class InvalidPriorityNumber(BaseException):
    pass

class queue:
    def __init__(self, maxCap:int) -> None:
        self.q = [
            [],
            []
            ]
        self.size = [
            0,
            0
        ]
        self.maxSize = [
            maxCap,
            maxCap
        ]
    
    def __repr__(self) -> str:
        return str(self.q)
    
    def enqueue(self, item, priority):
        if self.size[priority] == self.maxSize[priority]:
            raise QueueOverflowError

        if priority > 1 or priority < 0:
            raise InvalidPriorityNumber

        self.q[priority].append(item)
        self.size[priority] += 1
    
    def dequeue(self):
        for i, queue in enumerate(self.q):
            if queue:
                self.size[i] -= 1
                return queue.pop(0)
            
        raise QueueUnderflowError

    
    def peek(self):
        for queue in self.q:
            if queue:
                return queue[0]
        raise QueueUnderflowError
    
    def size(self):
        return self.size

    def maxSize(self):
        return self.maxSize
    
    def contains(self, item):
        return item in self.q[0] or item in self.q[1] 
    
    def isFull(self, priority):
        return self.size[priority] == self.maxSize[priority]

    def isEmpty(self, priority):
        return self.size[priority] == 0