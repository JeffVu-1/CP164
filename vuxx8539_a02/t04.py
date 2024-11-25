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
from Food_utilities import food_table, read_foods

file = open("foods.txt", "rt")

foods = read_foods(file)

file.close()

food_table(foods)
