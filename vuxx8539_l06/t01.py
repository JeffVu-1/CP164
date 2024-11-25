"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from List_linked import List

file_variable = open("/Users/jeffvu/Desktop/164 working on /Lab6/vuxx8539_l06/food.txt", "rt")

foods = read_foods(file_variable)

file_variable.close()

new_list = List()

new_list.append(foods[2])

new_list.prepend(foods[0])

new_list.insert(1, foods[1])

for value in new_list:
    print(value)
    print()

