"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from BST_linked import BST

bst = BST()

arr = [11, 7, 15, 6, 9, 12, 18, 8]
for value in arr:
    bst.insert(value)
zero, one, two = bst.node_counts()

print(zero)
print(one)
print(two)