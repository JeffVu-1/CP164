"""
-------------------------------------------------------
Array version of the list ADT TESTING
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from List_array import List

print()

# __eq__ #
############################################################################
source_eq1 = List()
source_eq2 = List()

source_eq1.append(1)
source_eq1.append(2)

source_eq2.append(1)
source_eq2.append(2)

print(f"Testing __eq__: {[source_eq1 == source_eq2]}\n")
############################################################################



# __getitem__ #
############################################################################
source_getitem = List()
source_getitem.append(1)
source_getitem.append(2)
source_getitem.append(3)
source_getitem.append(100)

print(f"Testing __getitem__: {source_getitem[3]}\n")
############################################################################


# append #
############################################################################
source_append = List()
source_append.append(1)
source_append.append(2)
source_append.append(3)
source_append.append(999)

print(f"Testing append: {source_append._values}\n")
############################################################################


# clean #
############################################################################
source_clean = List()

source_clean.append(99)
source_clean.append(1)
source_clean.append(2)
source_clean.append(3)
source_clean.append(3)
source_clean.append(3)
source_clean.append(4)
source_clean.append(5)

source_clean.clean()

print(f"Testing clean: {source_clean._values}\n")
############################################################################


# combine #
############################################################################
source1_combine = List()
source2_combine = List()
target_combine = List()

source1_combine.append(1)
source1_combine.append(2)

source2_combine.append(3)
source2_combine.append(4)


target_combine.combine(source1_combine, source2_combine)

print(f"Testing Combine: {target_combine._values}\n")
############################################################################


# intersection #
############################################################################
source1_intersection = List()
source2_intersection = List()

source1_intersection.append(1)
source1_intersection.append(2)
source1_intersection.append(4)
source1_intersection.append(5)

source2_intersection.append(3)
source2_intersection.append(4)
source2_intersection.append(5)

target_intersection = List() 

target_intersection.intersection(source1_intersection, source2_intersection)

print(f"Testing Intersection: {target_intersection._values}\n")
############################################################################


# prepend #
############################################################################
source_prepend = List()

source_prepend.append(1)
source_prepend.append(2)
source_prepend.append(3)

source_prepend.prepend(0)

print(f"Testing prepend: {source_prepend._values}\n")
############################################################################


# remove_front #
############################################################################
source_remove_front = List()
source_remove_front.append(1)
source_remove_front.append(2)
source_remove_front.append(3)
source_remove_front.append(4)
source_remove_front.append(5)

source_remove_front.remove_front()

print(f"Testing remove_front: {source_remove_front._values}\n")
############################################################################

# remove_many #
############################################################################
source_remove_many = List()
source_remove_many.append(1)
source_remove_many.append(2)
source_remove_many.append(3)
source_remove_many.append(3)
source_remove_many.append(4)
source_remove_many.append(5)

source_remove_many.remove_many(3)

print(f"Testing remove_many: {source_remove_many._values}\n")
############################################################################

# split #
############################################################################
source = List()
source.append(100)
source.append(99)
source.append(57)
source.append(22)

target1, target2 = source.split()

print(f"Testing split: {target1._values} | {target2._values}\n")
############################################################################

# split_alternating #
############################################################################
source_split_alternating = List()

source_split_alternating.append(1)
source_split_alternating.append(2)
source_split_alternating.append(3)
source_split_alternating.append(4)
source_split_alternating.append(5)
source_split_alternating.append(6)

target1 , target2 = source_split_alternating.split_alt()

print(f"Testing split_alternating: {target1._values} | {target2._values} \n")
############################################################################

# union #
############################################################################
source1_union = List()
source2_union = List()
target_union = List()

source1_union.append(1)
source1_union.append(2)

source2_union.append(3)
source2_union.append(4)


target_union.union(source1_union, source2_union)

print(f"Testing union: {target_union._values}\n")
############################################################################