class MinStack:

    def __init__(self):
        self.minElem = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack or self.minElem[-1] > val:
            self.minElem.append(val)
            self.stack.append(val)
        else:
            self.minElem.append(self.minElem[-1])
            self.stack.append(val)

    def pop(self) -> None:
        self.minElem.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minElem[-1]
