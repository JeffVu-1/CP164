"""
-------------------------------------------------------
Array version of the Sorted_List ADT TESTING
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from Sorted_List_array import Sorted_List

print()

# __contains__ #
############################################################################
source_contains = Sorted_List()
source_contains.insert(1)
source_contains.insert(2)
source_contains.insert(3)

print(f"Testing __contains__: {[source_contains.__contains__(6)]}\n")
############################################################################


# __eq__ #
############################################################################
source_eq1 = Sorted_List()
source_eq2 = Sorted_List()

source_eq1.insert(1)
source_eq1.insert(2)

source_eq2.insert(2)
source_eq2.insert(1)

print(f"Testing __eq__: {[source_eq1 == source_eq2]}\n")
############################################################################


# __getitem__ #
############################################################################
source_getitem = Sorted_List()
source_getitem.insert(1000)
source_getitem.insert(10001)

print(f"Testing __getitem__: {source_getitem[1]}\n")
############################################################################


# clean #
############################################################################
source_clean = Sorted_List()

source_clean.insert(99)
source_clean.insert(100)
source_clean.insert(101)
source_clean.insert(102)
source_clean.insert(103)
source_clean.insert(103)
source_clean.insert(103)
source_clean.insert(103)
source_clean.insert(103)
source_clean.insert(8)

source_clean.clean()

print(f"Testing clean: {source_clean._values}\n")
############################################################################


# count #
############################################################################
source_count = Sorted_List()

source_count.insert(1)
source_count.insert(1)
source_count.insert(1)
source_count.insert(2)
source_count.insert(2)
source_count.insert(2)
source_count.insert(3)
source_count.insert(3)

print(f"Testing count: {source_count.count(1)}\n")
############################################################################


# find #
############################################################################
source_find = Sorted_List()

source_find.insert(1)
source_find.insert(100)
source_find.insert(3)

print(f"Testing find: {source_find.find(2)}\n")
############################################################################

# index #
############################################################################
source_index = Sorted_List()

source_index.insert(10)
source_index.insert(23)
source_index.insert(99)
source_index.insert(107)

print(f"Testing index: {source_index.index(107)}\n")
############################################################################


# intersection #
############################################################################
source_intersection1 = Sorted_List()
source_intersection2 = Sorted_List()
target_intersection = Sorted_List()

source_intersection1.insert(1)
source_intersection1.insert(2)
source_intersection1.insert(200)

source_intersection2.insert(2)
source_intersection2.insert(3)
source_intersection2.insert(200)

target_intersection.intersection(source_intersection1, source_intersection2)

print(f"Testing intersection: {target_intersection._values}\n")
############################################################################

# max #
############################################################################
source_max = Sorted_List()

source_max.insert(1)
source_max.insert(2)
source_max.insert(999)
source_max.insert(1000)

print(f"Testing max: {source_max.max()}\n")
############################################################################


# min #
############################################################################
source_max = Sorted_List()

source_max.insert(1)
source_max.insert(2)
source_max.insert(999)
source_max.insert(1000)

print(f"Testing min: {source_max.min()}\n")
############################################################################


# peek #
############################################################################
source_peek = Sorted_List()

source_peek.insert(100)
source_peek.insert(109)
source_peek.insert(27)

print(f"Testing peek: {source_peek.peek()}\n")
############################################################################


# remove #
############################################################################
source_remove = Sorted_List()

source_remove.insert(1)
source_remove.insert(2)
source_remove.insert(3)
source_remove.insert(4)

source_remove.remove(3)

print(f"Testing remove: {source_remove._values}\n")
############################################################################


# remove_front #
############################################################################
source_remove_front = Sorted_List()

source_remove_front.insert(99)
source_remove_front.insert(100)
source_remove_front.insert(101)

source_remove_front.remove_front()

print(f"Testing remove_front: {source_remove_front._values}\n")
############################################################################


# remove_many #
############################################################################
source_remove_many = Sorted_List()

source_remove_many.insert(1)
source_remove_many.insert(2)
source_remove_many.insert(3)
source_remove_many.insert(4)
source_remove_many.insert(4)
source_remove_many.insert(4)

source_remove_many.remove_many(4)

print(f"Testing remove_many: {source_remove_many._values}\n")
############################################################################


# split #
############################################################################
source_split = Sorted_List()

source_split.insert(100)
source_split.insert(102)
source_split.insert(200)
source_split.insert(300)

target1 , target2 = source_split.split()

print(f"Testing split: {target1._values} | {target2._values}\n")
############################################################################


# split_alt #
############################################################################
source_split_alt = Sorted_List()

source_split_alt.insert(500)
source_split_alt.insert(1000)
source_split_alt.insert(1500)
source_split_alt.insert(2000)

target1 , target2 = source_split_alt.split_alt()

print(f"Testing split_alt: {target1._values} | {target2._values}\n")
############################################################################


# split_key #
############################################################################
source_split_key = Sorted_List()

source_split_key.insert(1190)
source_split_key.insert(2090)
source_split_key.insert(2560)
source_split_key.insert(3120)
source_split_key.insert(4120)

target1 , target2 = source_split_key.split_key(2560)

print(f"Testing split_key: {target1._values} | {target2._values}\n")
############################################################################

# union #
############################################################################
source_union1 = Sorted_List()
source_union2 = Sorted_List()
target_union = Sorted_List()

source_union1.insert(9000)
source_union1.insert(10000)

source_union2.insert(12000)
source_union2.insert(13000)

target_union.union(source_union1, source_union2)

print(f"Testing union: {target_union._values}\n")
############################################################################
