from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        return self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        if len(self.buffer())==0:
            return True
        else:
            return False
        
    def front(self):
        return self.buffer[-1]
    
def produce_binary(num):
    num_queue = Queue()
    num_queue.enqueue("1")

    for i in range(num):
        front = num_queue.front()
        print(" ", front)

        num_queue.enqueue(front + "0")
        num_queue.enqueue(front + "1")

        num_queue.dequeue()

    return


if __name__ == "__main__":
    produce_binary(10) 
