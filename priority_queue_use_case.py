"""
-------------------------------------------------------
asgn04.py
[program description]
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-10-04"
-------------------------------------------------------

"""
from priority_queue_array import PriorityQueue

def pq_split(pq1):
        """
        -------------------------------------------------------
        Moves the contents of a priority queue into two new 
        priority queues. Values are alternated. Split is stable.
        Use: pq2, pq3 = pq_split(pq1)
        -------------------------------------------------------
        Preconditions:
            pq1 - a priority queue (PriorityQueue)
        Postconditions:
            returns
            pq2 - a priority queue containing alternating values
                from pq1(PriorityQueue)
            pq3 - a priority queue containing alternating values
                from pq1 (PriorityQueue)
                pq1 is empty.
        -------------------------------------------------------
        """
        
        pq2 = PriorityQueue()
        pq3 = PriorityQueue()
        while not pq1.is_empty():
            value = pq1.remove()
            pq2.insert(value)
            
            if not pq1.is_empty():
                value = pq1.remove()
                pq3.insert(value)
                   
         
        return pq2,pq3
        



def pq_combine(pq1, pq2):
        """
        -------------------------------------------------------
        Combines contents of two priority queues into a new 
        priority queue. Alternate the values from pq1 and pq2.
        Use: q3 = pq_combine(pq1, pq2)
        -------------------------------------------------------
        Preconditions:
            pq1 - a priority queue (PriorityQueue)
            pq2 - a priority queue (PriorityQueue)
        Postconditions:
            returns
            pq3 - Contents of pq1 and pq2 are moved 
                into pq3 (PriorityQueue)
        -------------------------------------------------------
        """
        pq3 = PriorityQueue()
        
        while not pq1.is_empty() or not pq2.is_empty() :
            if not pq1.is_empty():
                value = pq1.remove()
                pq3.insert(value)
                
            if not pq2.is_empty():
                value = pq2.remove()
                pq3.insert(value)                                        
        return pq3