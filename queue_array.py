"""
-------------------------------------------------------
priority_queue.py
[program description]
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID: 161574090
Email: lixx4090@mylaurier.ca
__updated__ = "2016-09-27"
-------------------------------------------------------
"""
from copy import deepcopy
from stack_array import Stack


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a list.
        Use: q = Queue()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty queue.
        -------------------------------------------------------
        """
        self._values = []
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = q.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = q.is_full()
        -------------------------------------------------------
        Postconditions:
            Returns True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(q)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: q.insert( value )
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the rear of the queue.
        -------------------------------------------------------
        """

        # your code here
        self._values.append(deepcopy(value))
        
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = q.remove()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the front of the queue - the value is
            removed from the queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty queue"

        # your code here
        
        value = self._values.pop(0)
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = q.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the front of the queue -
            the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty queue"

        # your code here
        value = deepcopy(self._values[0])
        
        return value
    
    def identical(self, q2):
        """
        ----------------
        Determines whether two given queues are identical.
        Entries of q1 and q1 are compared and if all contents are identical
        and in the same order, returns True, otherwise returns False.
        Use: b = q1.identical(q1)
        ---------------
        Preconditions:
            q1 - a queue object (Queue)
        Postconditions:
            returns
            is_identical - True if q1 and q1 are identical, False otherwise. 
                Queues are unchanged. (boolean)
        ---------------
        """
        is_identical = True
        q1_temp = self
        q2_temp = q2
        
        if len(self) != len(q2):
            is_identical = False
        
        while is_identical and len(q1_temp) != 0:
            if q1_temp._values.pop(0) == q2_temp._values.pop(0):
                is_identical = True
            else:
                is_identical = False
        
        return is_identical
    
