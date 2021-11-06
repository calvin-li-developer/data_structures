"""
-------------------------------------------------------
utilties.py
[program description]
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID: 161574090
Email: lixx4090@mylaurier.ca
__updated__ = "2016-09-20"
-------------------------------------------------------
"""
from stack_array import *
from queue_array import *
from priority_queue_array import *
from list_array import *
# from food import Food
from queue_circular import CircularQueue

def array_to_stack(s, a):
    """
    -------------------------------------------------------
    Pushes contents of a onto s.
    Use: array_to_stack(s, a)
    -------------------------------------------------------
    Preconditions:
        s - a Stack object (Stack)
        a - a Python list (list)
    Postconditions:
        The contents of a are moved into s, a is empty.
    -------------------------------------------------------
    """
    while len(a) != 0:
        value = a.pop()
        s.push(value)
    
    return
    
def stack_to_array(s, a):
    """
    -------------------------------------------------------
    Pops contents of s into a.
    Use: stack_to_array(s, a)
    -------------------------------------------------------
    Preconditions:
        s - a Stack object (Stack)
        a - a Python list (list)
    Postconditions:
        Contents of s are moved into a, s is empty.
    -------------------------------------------------------
    """
    while not s.is_empty():
        value = s.pop()
        a.append(value)
    
    return

def stack_test(a):
    """
    -------------------------------------------------------
    Tests 
    Use: stack_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of Stack are tested for both empty and 
        non-empty stacks using the data in a:
        is_empty, push, pop, peek
    -------------------------------------------------------
    """
    s = Stack()
    print("Is stack empty?")
    print(s.is_empty())
    
    array_to_stack(s, a)
    print(s.peek())
    print("Is stack empty?")
    print(s.is_empty())
#     while not s.is_empty():
#         print(s.peek())
#         s.pop()
    stack_to_array(s, a)
#     for i in a:
#         print(i)
    
    
    

    # tests for the stack methods go here
    # print the results of the method calls and verify by hand

    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        is_empty, insert, remove, peek
    -------------------------------------------------------
    """
    q = Queue()
    print("Is queue empty?")
    print(q.is_empty())
    for i in a:
        q.insert(i)
    print("Removed value is:")
    print(q.remove())
    print("Peek value is:")
    print(q.peek())

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    return

def pq_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: pq_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of PriorityQueue are tested for both empty and 
        non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    -------------------------------------------------------
    """
    pq = PriorityQueue()
    
    print("Is queue empty?")
    print(pq.is_empty())
    for i in a:
        pq.insert(i)
    print("Removed value is:")
    print(pq.remove())
    print("Peek value is:")
    print(pq.peek())

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    return

def list_test(a):
    """
    -------------------------------------------------------
    Tests list implementation.
    Use: list_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of List are tested for both empty and 
        non-empty lists using the data in a:
        is_empty, insert, remove, append, index, __contains__,
        find, max, min, __getitem__, __setitem__
    -------------------------------------------------------
    """
    l = List()
    
    print("Is queue empty?")
    print(l.is_empty())
    print("----------------------------")
    print("insert")
    print(a[2])
    l.insert(2,a[2])
    for i in a:
        l.append(i)    
    print("----------------------------")
    print("Removed value is (from a[3]:")
    print(l.remove(a[3]))
    print("----------------------------")
    print("Append (a[0]):")
    print(a[0])
    l.append(a[0])
    print("----------------------------")
    print("Index (a[4]):")
    print(l.index(a[4]))
    print("----------------------------")
    print("contains (l[0])")
    b = l[0] in l
    print(b)
    print("----------------------------")
    print("find a[2]")
    print(l.find(a[2]))
    print("----------------------------")

    print("max")
    print(l.max())
    print("----------------------------")

    print("min")
    print(l.min())
    print("----------------------------")
    
    print("getitem")
    print(l[0])
    print("----------------------------")

    print("setitem to None")
    l[3] = None
    
    print(l[3])

    # tests for the List methods go here
    # print the results of the method calls and verify by hand

    return

def list_test_aux(a):
    
    i=0
    
    while i < 6:
        a.append(i)
        i+=1
    
    index = a._linear_search_r_no_aux(5,a._front,0) 
    print(index)
    index = a._linear_search(5)
    print(index)     
    
    return
def linked_list_test(a):
    
    i=0
    
    while i < 6:
        
        a.insert_front(i)
        i+=1
        
    p,c,i = a._linear_search_r_no_aux(6,a._front,0)
    
    print(p,c,i)
    
    p,c,i = a._linear_search(7)
    print(p,c,i)
    
    p,c,i = a._linear_search_r(6)
    
    print(p,c,i)
    
    return
def circular_queue_test(a):
    
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        is_empty, insert, remove, peek
    -------------------------------------------------------
    """
    
    q = CircularQueue(20)
    print("Is queue empty?")
    print(q.is_empty())
    print("count value?")
    print(q._count)
    print("insert values")
    for i in a:
        q.insert(i)

    print("Is queue full? " + str(q.is_full()))
    print("length is " + str(len(q)))
    print("Peek value is:")
    print(q.peek())
    print("Removed value is:")
    print(q.remove())
    print("Is queue full? " + str(q.is_full()))
    return
