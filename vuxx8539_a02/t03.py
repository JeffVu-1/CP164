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
from Food_utilities import calories_by_origin, read_foods

file = open("foods.txt", "rt")

foods = read_foods(file)

file.close()

cal_by_org = calories_by_origin(foods, 2)

print(f"Cal by origin: {cal_by_org}")
