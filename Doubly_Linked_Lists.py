class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        if self.head == None:
            self.head = Node(data, self.head, None)
            return
        
        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node
        return
    

    def insert_at_end(self, data):
        if self.head == None:
            self.insert_at_start(data)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)
        return
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr
    

    def insert_at(self, data, index):
        if index < 0  or index > self.get_length():
            raise Exception("Index out of range")
        
        if index == 0:
            self.insert_at_start(data)

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

        return

    def insert_values(self, arr):
        for i in arr:
            self.insert_at_end(i)
        
        return
    
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

        return


    def print_forward(self):
        if self.head == None:
            print('List is empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        
        print(llstr)

    
    def print_backward(self):
        if self.head == None:
            print("List is empty")
            return
        
        itr = self.get_last_node()
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.prev

        print(llstr)

if  __name__ == "__main__":
    dll = DoublyLinkedList()
    # Inserting elements at the start of the list
    dll.insert_at_start(5)
    dll.insert_at_start(66)
    dll.print_forward()

    dll.insert_at_end(21)
    dll.insert_at_end(11)
    dll.print_forward()

    print("Length of the list is: ", dll.get_length())

    dll.insert_at(32, 1)
    dll.print_forward()

    dll.insert_values(["banana","mango","grapes","orange"])
    dll.print_forward()

    dll.remove_at(2)
    dll.print_forward()
    dll.print_backward()

    print("-------------------- TEST CASES -----------------------")
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at("jackfruit", 0)
    ll.print_forward()
    ll.insert_at("dates", 6)
    ll.print_forward()
    ll.insert_at("kiwi", 2)
    ll.print_forward()