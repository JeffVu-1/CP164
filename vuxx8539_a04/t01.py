"""
-------------------------------------------------------
Assignment 4 t01
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from Queue_circular import Queue

q = Queue(4)

q.insert(100)
q.insert(200)
q.insert(300)

print(len(q))
print(q.is_empty())
q.insert(100)
print(len(q))
value = q.peek()
print(value)
removed = q.remove()
print(removed)
print(q.is_full())