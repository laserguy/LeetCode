class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
       self.s1.append(x)
        

    def pop(self) -> int:
        if self.s2: return self.s2.pop()
        while(self.s1):
            self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        x = self.pop()
        self.s2.append(x)
        return x

    def empty(self) -> bool:
        return False if self.s1 or self.s2 else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()