class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.minstack)==0:
            self.minstack.append(value)
        elif value<=self.minstack[-1]:
            self.minstack.append(value)

    def pop(self) -> None:
        x=self.stack.pop()
        if len(self.minstack)!=0 and x==self.minstack[-1]:
            self.minstack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.minstack)==0:
            return 0
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()