class HashTables:
    def  __init__(self):
        self.MAX = 10
        self.arr = [ [] for i in range(self.MAX) ]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        return (hash % self.MAX)
    
    # Implementing chaining
    def __setitem__(self, key, val):
        index = self.get_hash(key)

        found  = False
        for idx, element in enumerate(self.arr[index]):
            if len(element) == 2 and  element[0] == key:
                self.arr[index][idx] = (key,val)
                found = True
                break

        if not found:
            self.arr[index].append((key,val))

        return

    def __getitem__(self, key):
        index = self.get_hash(key)

        for element in self.arr[index]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        index = self.get_hash(key)

        for idx, element in enumerate(self.arr[index]):
            if element[0] == key:
                del self.arr[index][idx]
                return

if __name__ ==  "__main__":
    t = HashTables()
    t["mar 6"] = 120
    t["mar 6"] = 23
    t["mar 9"] = 34
    t["mar 17"] = 11
    del t["mar 17"]
    print(t.arr)