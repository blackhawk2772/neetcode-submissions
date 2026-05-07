class MinStack:

    def __init__(self):
        self.array = []
        self.min = []

    def push(self, val: int) -> None:
        self.array.append(val)
        
        if not self.min or self.min[-1] > val:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.array.pop()        
        self.min.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.min[-1]