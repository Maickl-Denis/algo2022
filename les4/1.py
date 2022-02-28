class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minVal = val
        else:
            if self.minVal <= val:
                self.stack.append(val)
            else:
                self.stack.append(2 * val - self.minVal)
                self.minVal = val
        return None


    def pop(self) -> None:
        if len(self.stack) != 0:
            if self.stack[-1] >= self.minVal:
                self.stack.pop()
            else:
                self.minVal = 2 * self.minVal - self.stack[-1]
                self.stack.pop()
        return None

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            if self.stack[-1] >= self.minVal:
                return self.stack[-1]
            else:
                return self.minVal


    def getMin(self) -> int:
        return self.minVal