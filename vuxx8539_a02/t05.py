"""
-------------------------------------------------------
Assignment 2
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from Food_utilities import food_search, read_foods, food_table

file = open("foods.txt", "rt")

foods = read_foods(file)

file.close()

result = food_search(foods, 1, 200, False)

food_table(result)
