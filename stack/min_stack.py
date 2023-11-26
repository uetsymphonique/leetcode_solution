class MinStack:
    def __init__(self):
        self.stack = list()
        self.min_element = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_element = val
        elif val >= self.min_element:
            self.stack.append(val)
        else:
            self.stack.append(val - (self.min_element - val))
            self.min_element = val

    def pop(self) -> None:
        popped_element = self.stack.pop(-1)
        if popped_element < self.min_element:
            self.min_element = self.min_element + (self.min_element - popped_element)

    def top(self) -> int:
        top_element = self.stack[-1]
        if top_element < self.min_element:
            return self.min_element
        return top_element

    def getMin(self) -> int:
        return self.min_element
