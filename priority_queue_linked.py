"""
-------------------------------------------------------
priority_queue_linked.py
[program description]
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-09"
-------------------------------------------------------

"""
import copy
from copy import deepcopy


class _PQNode:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node.
        Use: node = _PQNode(value, _next)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            _next - another priority queue node (_PQNode)
        Postconditions:
            Initializes a priority queue node that contains a copy of value
            and a link to the next node in the priority queue.
        -------------------------------------------------------
        """
        self._data = copy.deepcopy(value)
        self._next = _next
        return


class PriorityQueue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = PriorityQueue()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty priority queue.
        -------------------------------------------------------
        """
        self._front = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(q)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the priority queue.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the priority queue.
        Use: pq.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the priority queue.
        -------------------------------------------------------
        """
        previous = None
        if self._front is None:
            self._front = _PQNode(value, None)
        elif value < self._front._data:
            self._front = _PQNode(value, self._front)
        else:
            current = self._front            
            while current is not None and value >= current._data:
                previous = current
                current = current._next
       
            previous._next = _PQNode(value,current)
        self._count += 1

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the priority queue.
        Use: v = pq.remove()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the highest priority value in the priority queue -
            the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"
        
        value = self._front._data
        self._front = self._front._next
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the highest priority value in the priority queue -
            the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"

        value = deepcopy(self._front._data)
        
        return value

    def split(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The split is stable.
        Use: pq2, pq3 = pq1.split(key)
        -------------------------------------------------------
        Preconditions:
            key - a data object (?)
        Postconditions:
            returns
            pq2 - a priority queue that contains all values
                with priority less than key (PriorityQueue)
            pq3 - priority queue that contains all values with
                priority greater than or equal to key (PriorityQueue)
            The current priority queue is empty
        -------------------------------------------------------
        """

# your code here
        pq2 = PriorityQueue()
        pq3 = PriorityQueue()
        while self._front is not None and self._front._data <= key:
            pq3.insert(self._front._data)
            self._front = self._front._next
        
        while self._front is not None and self._front._data > key:
            pq2.insert(self._front._data)
            self._front = self._front._next
            
        return pq2, pq3

    def _move_front(self, rs):
        """
        -------------------------------------------------------
        Moves the front node from the rs PriorityQueue to the front
        of the current PriorityQueue.
        Use: self._move_front(rs)
        -------------------------------------------------------
        Preconditions:
            rs - a linked PriorityQueue (PriorityQueue)
        Postconditions:
            The current PriorityQueue contains the old front of the rs PriorityQueue and
            its count is updated. The rs PriorityQueue front and count are updated.
        -------------------------------------------------------
        """
        assert rs._front is not None, \
            "Cannot move the front of an empty List"

        temp = rs._front
        rs._front = rs._front._next
        rs._count -= 1
        self._front = _PQNode(temp._data, self._front)
        self._count += 1
        
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._data
            current = current._next