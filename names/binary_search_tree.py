"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

# from queue import LLQueue
# from stack import LLStack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value and self.left != None:
                return self.left.contains(target)
            elif target > self.value and self.right != None:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        self.value = fn(self.value)
        if self.left != None:
            self.left.for_each(fn)
        if self.right != None:
            self.right.for_each(fn)
            

#     # Part 2 -----------------------

#     # Print all the values in order from low to high
#     # Hint:  Use a recursive, depth first traversal
#     def in_order_print(self):
#         if self.left != None:
#             self.left.in_order_print()
#         print(self.value)
#         if self.right != None:
#             self.right.in_order_print()

#     # Print the value of every node, starting with the given node,
#     # in an iterative breadth first traversal
#     def bft_print(self):
#         q = LLQueue()
#         q.enqueue(self)

#         while len(q) > 0:
#             n = q.dequeue()
#             print(n.value)
#             if n.left != None:
#                 q.enqueue(n.left)
#             if n.right != None:
#                 q.enqueue(n.right)

#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
#     def dft_print(self):
#         s = LLStack()
#         s.push(self)

#         while len(s) > 0:
#             n = s.pop()
#             print(n.value)
#             if n.left != None:
#                 s.push(n.left)
#             if n.right != None:
#                 s.push(n.right)

#     # Stretch Goals -------------------------
#     # Note: Research may be required

#     # Print Pre-order recursive DFT
#     def pre_order_dft(self):
#         print(self.value)
#         if self.left != None:
#             self.left.pre_order_dft()
#         if self.right != None:
#             self.right.pre_order_dft()

#     # Print Post-order recursive DFT
#     def post_order_dft(self):
#         if self.left != None:
#             self.left.post_order_dft()
#         if self.right != None:
#             self.right.post_order_dft()
#         print(self.value)

# """
# This code is necessary for testing the `print` methods
# """
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_print()
# print("post order")
# bst.post_order_dft()  
