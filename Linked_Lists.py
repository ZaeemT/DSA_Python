class Node: 
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head == None:   # That is list is blank
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:     # while we are not at end of the list and itr.next != none
            itr = itr.next  # iterate

        itr.next = Node(data, None)

    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count


    def print_list(self):
        if self.head == None:
            print("List is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next

        print(llstr)


    def insert_values(self, arr):
        for i in arr:
            self.insert_at_end(i)

    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Index out of range')
        
        if index == 0:
            self.insert_at_start(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node

            itr = itr.next
            count += 1

    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if  index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1 

    def insert_after_value(self, data_after, data_insert):
        if  self.head is None:
            print("List is empty")
            return
        
        if self.head == data_after:
            self.head.next = Node(data_insert, self.head.next)
            return
        
        count = 0
        itr = self.head
        while itr:
            if data_after == itr.data:
                itr.next = Node(data_insert, itr.next)
                break
            
            itr = itr.next
        
        return    

    def remove_by_value(self, data):
        if  self.head is None:
            print("List is empty")
            return
        
        if  self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            
            itr = itr.next

        return
    
if __name__ == '__main__':
    ll_1 = LinkedList()
    ll_1.insert_at_end(5)
    ll_1.insert_at_end(34)
    ll_1.print_list()
    
    ll_2 = LinkedList()
    ll_2.insert_at_start(43)
    ll_2.insert_at_start(21)
    ll_2.print_list()

    ll_3 = LinkedList()
    array = ["Monday", "Tuesday", "Wednesday", "Thursday"]
    ll_3.insert_values(array)
    ll_3.print_list()

    print("Length of link list 3 is: ", ll_3.get_length())

    ll_3.remove_at(2)
    ll_3.print_list()

    ll_3.insert_at(1, "figs")
    ll_3.print_list()
    ll_3.insert_at(0, "days")
    ll_3.print_list()

    ll_3.insert_after_value("figs", "new-figs")
    ll_3.print_list()

    ll_3.remove_by_value("days")
    ll_3.print_list()

    print("-------------------- TEST CASES -----------------------")
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_list()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_list()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_list()
    ll.remove_by_value("figs")
    ll.print_list()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_list()