class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def tree_sum(root):
    if root is None:
        return 0
    else:
        left_sum = tree_sum(root.left)
        right_sum = tree_sum(root.right)
    return root.data + left_sum +right_sum

def maximum(root):
    if root is None:
        return float("-inf")
    else:
        left_max = maximum(root.left)
        right_max = maximum(root.right)
    return max(root.data,left_max,right_max)

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
    print(left_height,right_height)
    return 1+max(left_height,right_height)

def exists_in_tree(root,val):
    if root is None:
        return False
    else:
        in_left = exists_in_tree(root.left,val)
        in_right = exists_in_tree(root.right,val)
    return root.data == val or in_left or in_right
    
def reverse_tree(root):
    if root is None:
        return 
    else:
        reverse_tree(root.left)
        reverse_tree(root.right)
        root.left ,root.right = root.right,root.left

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
   
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())

    # print(tree_sum(numbers_tree))

    # print(maximum(numbers_tree))
    print(height(numbers_tree))
    # print(exists_in_tree(numbers_tree,4))
    # reverse_tree(numbers_tree)
    # print(numbers_tree.in_order_traversal())