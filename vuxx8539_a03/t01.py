"""
-------------------------------------------------------
Assignment 3 Task 1
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack
from functions import stack_combine

source1 = Stack()
source2 = Stack()

list1 = [5,8,12,8]

array_to_stack(source1, list1)

list2= [3,6,1,7,9,14]

array_to_stack(source2, list2)

target = stack_combine(source1, source2)

print(target._values)