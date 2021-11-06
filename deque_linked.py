"""
-------------------------------------------------------
deque_linked.py
[program description]
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-09"
-------------------------------------------------------

"""
# Imports
from copy import deepcopy


class _DequeNode:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _DequeNode(value, prev, _next)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            _prev - another deque node (_DequeNode)
            _next - another deque node (_DequeNode)
        Postconditions:
            Initializes a deque node that contains a copy of value
            and links to the previous and next nodes in the deque.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._prev = _prev
        self._next = _next
        return


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty deque.
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = d.empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(d)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of values in the deque.
        -------------------------------------------------------
        """
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: d.insert_front(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the front of the deque.
        -------------------------------------------------------
        """
        
        if self._front is None:
            self._front = _DequeNode(value,None, None)
            self._rear = self._front
        else:
            self._front = _DequeNode(value,None,self._front)
            self._front._next._prev = self._front
                        
        self._count += 1
        
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: d.insert_rear(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the rear of the deque.
        -------------------------------------------------------
        """

        if self._rear is None:
            self._front = _DequeNode(value,None, None)
            self._rear = self._front
        else:
            self._rear = _DequeNode(value,self._rear,None)
            self._rear._prev._next = self._rear
            
        self._count += 1

        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = d.remove_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the front of deque - the value is
                removed from deque.
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty dequeue"

# your code here
        value = deepcopy(self._front._data)
        if self._count == 1:
            self._front = self._front._next
            self._rear = None
        else:
            self._front._next._prev = None
            self._front = self._front._next
        self._count -=1 
           
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = d.remove_rear()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the rear of deque - the value is
                removed from deque.
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty dequeue"

# your code here
        value = deepcopy(self._rear._data)
        if self._count == 1:
            self._rear = self._rear._prev
            self._front = None
        else:
            self._rear._prev._next = None
            self._rear = self._rear._prev
        self._count -=1

        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = d.peek_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the front of deque -
                the value is not removed from deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty dequeue"

# your code here
        value = deepcopy(self._front._data)

        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = d.peek_rear()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the rear of deque -
                the value is not removed from deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty dequeue"

# your code here
        value = deepcopy(self._rear._data)

        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Preconditions:
            l - a pointer to a deque node (_DequeNode)
            r - a pointer to a deque node (_DequeNode)
        Postconditions:
            l has taken the place of r, r has taken the place of l and
            _front and _rear are updated as appropriate
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"

        if l is not r:
            # Swap the parameter node pointers
            l._prev, r._prev, l._next, r._next = r._prev, l._prev, r._next, l._next

            # If nodes are adjacent, previous swaps make nodes point to
            # themselves
            if l._prev is l:
                l._prev = r
            elif l._next is l:
                l._next = r

            if r._prev is r:
                r._prev = l
            elif r._next is r:
                r._next = l

            # Update linked nodes
            # See if front and/or rear have changed
            if l._prev is None:
                # l is the front
                self._front = l
            else:
                l._prev._next = l

            if l._next is None:
                # l is the rear
                self._rear = l
            else:
                l._next._prev = l

            if r._prev is None:
                # r is the front
                self._front = r
            else:
                r._prev._next = r

            if r._next is None:
                # r is the rear
                self._rear = r
            else:
                r._next._prev = r
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the dequeue
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the dequeue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._data
            current = current._next