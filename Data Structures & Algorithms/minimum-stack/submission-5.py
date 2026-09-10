class MinStack:

    def __init__(self):
        self.arr = []
        self.mini = []
        print(self.arr)
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.mini or self.mini[-1] >= val:
            self.mini.append(val)
 
        

    def pop(self) -> None:
        if not self.arr:
            return 
        val = self.arr.pop()
        if val == self.mini[-1]:
            self.mini.pop() 
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        if self.mini:
            return self.mini[-1]
        else:
            return -1