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
from Hash_Set_sorted import Hash_Set
from functions import insert_words, comparison_total

hs = Hash_Set(10)

file = open('otoos610.txt', 'r')
insert_words(file, hs)
file.close()
total, max_value = comparison_total(hs)

print(f"Total Comparisons: {total:,}")
print(f"Word with maximum comparisons '{max_value.word}': {max_value.comparisons:,}")


