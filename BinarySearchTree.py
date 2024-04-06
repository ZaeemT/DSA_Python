class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            # Means that data already exists and it cannot repeat.
            return

        if data < self.data:
            # Add data to left subtree.
            if self.left:   # Checking in left node exists
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # Add data to right subtree.
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def in_order_traversal(self):
        elements = []
        # Visit left subtree first
        if self.left:
            elements += self.left.in_order_traversal()
        # Visit base node
        elements.append(self.data)
        # Visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements  


    def pre_order_traversal(self):
        elements = []
        # Visit root node first
        elements.append(self.data)
        # Visit left subtree
        if self.left:
            elements += self.left.pre_order_traversal()
        # Visit right subtree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        # Visit left subtree first
        if self.left:
            elements += self.left.post_order_traversal()
        # Visit right subtree
        if self.right:
            elements += self.right.post_order_traversal()
        # Visit base node
        elements.append(self.data)
        return elements


    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
        # Search left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
        # Search right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def calculate_sum(self):
        sum = self.data

        # Calculate sum of left subtree
        if self.left:
            sum += self.left.calculate_sum()

        # Calculate sum of right subtree
        if self.right:
            sum += self.right.calculate_sum()

        return sum

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min() 
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min = self.right.find_min()
            self.data = min
            self.right = self.right.delete(min)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [88, 23, 14, 7, 20, 15, 12, 27]
    numbers = [15,12,7,14,27,20,23,88 ]

    numbers_tree = build_tree(numbers)
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]