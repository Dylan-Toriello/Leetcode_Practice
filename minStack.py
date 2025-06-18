class MinStack:

    def init(self):
        #intialize an empty main stack
        #initialize an empy min stack
        self.main_stack = []
        self.min_stack = []



    def push(self, val: int) -> None:
        #push value onto main stack
        #if value is less than or = to top of minstack 
            #push to min stack

        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1] :
            self.min_stack.append(val)

    def pop(self) -> None:
        #is top of main stack = to top of min stack
            #pop value from min stack
        #pop from main stack
        if self.main_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.main_stack.pop()

    def top(self) -> int:
        #return the top element of main stack
        return self.main_stack[-1]

    def getMin(self) -> int:
        #return top of minstack
        return self.min_stack[-1]
