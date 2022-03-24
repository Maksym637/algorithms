# LIFO
# The Last-in, First-out

class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        return None
    
    def __str__(self):
        return str(self.stack)

def main():
    stack = Stack()

    for i in range(1, 6):
        stack.push(i)
    
    print(stack)

    for i in range(1, 3):
        stack.pop()
    
    print(stack)
    print(stack.peek())

if __name__ == "__main__":
    main()