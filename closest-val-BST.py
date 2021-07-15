# find the closest value to a target in a BST

def findClosestValue(tree, target):
    closest = tree.value
    while tree:
        if abs(target - tree.value) < abs(target - closest):
            closest = tree.value
        if target < tree.value:
            tree = tree.left
        else:
            tree = tree.right
    return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree = BST(4)
tree.left = BST(2)
tree.right = BST(5)
tree.left.left = BST(1)
tree.left.right = BST(3)
tree.right.left = BST(6)
tree.right.right = BST(7)
target = 3.5
print(tree.value, tree.left.value, tree.right.value)
print(findClosestValue(tree, target))