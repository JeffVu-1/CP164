"""
-------------------------------------------------------
Assignment 3 Task 7 Maze
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import stack_maze

maze = {
    'Start': ['A'],
    'A': ['B', 'C'],
    'B': ['X'],
    'C': ['D'],
    'D': ['X'],
    'X': []
       }

path = stack_maze(maze)
print(path)
