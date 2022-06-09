# LIFO structure (Last In First Out)

class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass

class stack:
    def __init__(self, maxCap:int) -> None:
        self.stack = [None] * maxCap
        self.stackSize = 0
        self.maxSize = maxCap

    def __repr__(self) -> str:
        return str(self.stack[:self.stackSize])
    
    def push(self,item):
        if self.maxSize == self.stackSize:
            raise StackOverflowError
        self.stack[self.stackSize] = item
        self.stackSize += 1
    
    def pop(self):
        if self.stackSize == 0:
            return StackUnderflowError
        item = self.stack[self.stackSize]
        self.stack[self.stackSize] = None
        self.stackSize -= 1
        return item
    
    def peek(self):
        return self.stack[self.stackSize]
    
    def size(self):
        return self.stackSize
    
    def maxSize(self):
        return self.maxSize

    def contains(self, item):
        return item in self.stack
    
    def isFull(self):
        return self.stackSize == self.maxSize

    def isEmpty(self):
        return self.stackSize == 0
        

