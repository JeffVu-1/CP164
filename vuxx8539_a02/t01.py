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
from Food import Food
from Food_utilities import read_foods, by_origin

file = open("foods.txt", "rt")

foods = read_foods(file)

file.close()

origin = int(input(f"Enter a origin as an int\n{Food.origins()}: "))

origin_foods = by_origin(foods, origin)

for food in origin_foods:
    print(food, end="\n\n")
