"""
-------------------------------------------------------
test_func.py
[program description]
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-09"
-------------------------------------------------------

"""
from priority_queue_linked import PriorityQueue

pq = PriorityQueue()
 
i = 0
print("------------------------------------------------------------------")
print("PQ : Insert Data") 
print("Inserting integers from 0 to 10, -1 and 4.")
print("------------------------------------------------------------------")
while i < 11:
    pq.insert(i)
    i+=1

pq.insert(-1)
pq.insert(4)
print("PQ: ", end="")
for i in pq:
    print(str(i) + " ", end="")
print()
print("------------------------------------------------------------------")
print("PQ : Remove Data")
print("Remove the Highest Priority Node")
print("Removed from PQ: " +str(pq.remove()))
print("------------------------------------------------------------------")
print("PQ : Peek")
print("Peek the Highest Priority Node")
print("Peek from PQ: " +str(pq.peek()))
print("------------------------------------------------------------------")
print("PQ : Split")
print("Splits a priority queue into two (PQ2, PQ3) depending on an external priority key. The split is stable.")
print("Let key = 4")
pq2, pq3 = pq.split(4)
string = "PQ2: "
for i in pq2:
    string = string + str(i) + " "
print(string)
string = "PQ3: "
     
for i in pq3:
    string = string + str(i) + " "
print(string)
print("------------------------------------------------------------------")
print("PQ : _move_front")
r = PriorityQueue()
r.insert(7)
print("r: ", end="")
for i in r:
    print(str(i) + " ", end="")
print()
i=0
while i < 11:
    pq.insert(i)
    i+=1

pq.insert(-1)
pq.insert(4)
print("PQ: ", end="")
for i in pq:
    print(str(i) + " ", end="")
print()
pq._move_front(r)
print("PQ: ", end="")
for i in pq:
    print(str(i) + " ", end="")
print()





