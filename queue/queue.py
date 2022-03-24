# FIFO
# The First-in, First-out

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def inQueue(self, item):
        self.items.insert(0, item)
    
    def outQueue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def printQueue(self):
        print(self.items)

def main():
    q = Queue()

    for i in range(1 , 6):
        q.inQueue(i)
    
    q.printQueue()

    for i in range(1, 3):
        q.outQueue()
    
    q.printQueue()

if __name__ == "__main__":
    main()