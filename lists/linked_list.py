class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next
        print(llstr)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        cnt = 0
        itr = self.head
        while itr:
            cnt += 1
            itr = itr.next
        return cnt
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        elif index == 0:
            self.head = self.head.next
            return
        cnt = 0
        itr = self.head
        while itr:
            if cnt == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            cnt += 1
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_begining(data)
            return
        cnt = 0
        itr = self.head
        while itr:
            if cnt == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            cnt += 1


def main():
    linkedList = LinkedList()

    for i in range(1, 11):
        linkedList.insert_at_end(i)
    linkedList.print()
    print(linkedList.get_length())

    linkedList.insert_at(3, 100)
    linkedList.print()

    linkedList.remove_at(0)
    linkedList.print()


if __name__ == "__main__":
    main()