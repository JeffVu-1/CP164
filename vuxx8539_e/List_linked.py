"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author: Jeff Vu
ID:     169058539
Email:  vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from copy import deepcopy

class List:
    """
    A linked List class.
    """

    def split_count(self, count):  # this is done
        """
        -------------------------------------------------------
        Splits source into separate target lists based on count.
        At finish target1 contains count nodes, target2 contains 
        remaining nodes from source, and source is empty.
        Order of source values is preserved.
        Use: target1, target2 = source.split_count(count)
        -------------------------------------------------------
        Parameters:
            count - the number of nodes in target1 (int >= 0)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​​‌‌‌​‌​‌‌:
            target1 - contains count nodes from source (List)
            target2 - contains remaining nodes from source (List)
        -------------------------------------------------------
        """

        target1 = List()
        target2 = List()

        if count > self._count:
            count = self._count

        for _ in range(count):
            target1.append(self._front._value)
            self._front = self._front._next

        while self._front is not None:
            target2.append(self._front._value)
            self._front = self._front._next

        self._front = None
        self._rear = None
        self._count = 0

        return target1, target2

    def replace_many(self, key, value):
        """
        -------------------------------------------------------
        Replace every occurrence of key in source with value.
        List is otherwise unchanged.
        Use: source.replace_many(key, value)
        -------------------------------------------------------
        Parameters:
            key - a key that may be in source (?)
            value - the replacement for key (?)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​​‌‌‌​‌​‌‌:
            None.
        -------------------------------------------------------
        """
        current = self._front
        while current is not None:
            if current._value == key:
                current._value = value
            current = current._next

        return

    def rotate_rear(self):
        """
        -------------------------------------------------------
        Moves the rear node to the front of the List.
        Use: source.rotate_rear()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​​‌‌‌​‌​‌‌:
            None
        -------------------------------------------------------
        """
        if self._count > 1:
            current = self._front
            while current._next is not self._rear:
                current = current._next
            current._next = None
            self._rear._next = self._front 
            self._front = self._rear
            self._rear = current

        return

    def has_loop(self):
        """
        -------------------------------------------------------
        Determines if source contains a circular reference/loop.
        Use: loop = source.has_loop()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​​‌‌‌​‌​‌‌:
            loop - True if source contains a circular reference,
                False otherwise (bool)
        -------------------------------------------------------
        """

        status = False
        slow_pointer = self._front
        fast_pointer = self._front
        while slow_pointer is not None and fast_pointer is not None and fast_pointer._next is not None:
            slow_pointer = slow_pointer._next
            fast_pointer = fast_pointer._next._next
            if slow_pointer == fast_pointer:
                status = True
                break

        return status

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​​‌‌‌​‌​‌‌:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​​‌‌‌​‌​‌‌:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​​‌‌‌​‌​‌‌:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​​‌‌‌​‌​‌‌:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​​‌‌‌​‌​‌‌:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        count = 0
        current = self._front

        while current is not None and count < self._count:
            yield current._value
            current = current._next
            count += 1


class _List_Node:
    """
    A linked List Node class.
    """

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns‌​‌​​​​‌​​‌‌‌​‌​​​​​‌‌‌​‌​‌‌:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
