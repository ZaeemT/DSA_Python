# Implementation of Hash Tables using Linear Probing

class HashTable:
    
    def __init__(self):
        self.MAX = 10
        self.arr = [ None for i in range(self.MAX) ]

    def get_hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)

        return (sum % self.MAX)
    
    def __setitem__(self, key, value):
        index = self.get_hash(key)
        
        element = self.arr[index]
        if self.arr[index] is None:
            self.arr[index] = [key, value]
        else:
            while self.arr[index] is not None:     # Space already occupied
                if element[0] == key:
                    element[1] = value          # Update the existing pair
                    return
                else:                           #  Move to next slot
                    index = (index + 1) % self.MAX
                
            self.arr[index] = [key, value]   # Insert new pair at empty slot
            return
        
    def __getitem__(self, key):
        index = self.get_hash(key)

        if self.arr[index] is not None:
            element = self.arr[index]
            if element[0] == key:   # Matches the key
                return element[1]
            else: 
                while self.arr[index][0] != key:    
                    """
                    Means the element is stored at next index or may be even
                    further. Thus iterates through the space until key is matches.
                    """
                    index = (index + 1) % self.MAX
                
                return element[1]
            
    def __delitem__(self, key):
        index = self.get_hash(key)

        while self.arr[index] is not None:
            if self.arr[index][0] == key:
                del self.arr[index]
                return
            else:
                index = (index + 1) % self.MAX
            


if __name__ == "__main__":
    t = HashTable()
    
    t["mar 6"] = 120
    t["mar 6"] = 23
    t["mar 9"] = 34
    t["mar 17"] = 11
    del t["mar 17"]
    print(t.arr)