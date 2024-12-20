"""
-------------------------------------------------------
[Speed Test]
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from Letter import Letter
from VUXX8539_data_structures.BST_linked import BST
from functions import do_comparisons, comparison_total, letter_table


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

def create_bst(s):
    new_tree = BST()
    for i in s:
        new_tree.insert(Letter(i))
    return new_tree

bst1 = create_bst(DATA1)
bst2 = create_bst(DATA2)
bst3 = create_bst(DATA3)

file_variable = open("gibbon.txt", "r")
do_comparisons(file_variable, bst3)
file_variable.close()

letter_table(bst3)

