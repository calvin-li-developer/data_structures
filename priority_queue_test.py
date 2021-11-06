"""
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-10-04"
-------------------------------------------------------

"""
from utilties import *
from movie import *
from movie_utilities import *
from priority_queue_array import *
from priority_queue_use_case import *

# ======================== USECASE #1 ========================
print('\n======================== USECASE #1 ========================\n')

a = read_movies(open("movies.txt","r"))
b = circular_queue_test(a)

# ======================== USECASE #2 ========================
print('\n======================== USECASE #2 ========================\n')

pq1 = PriorityQueue()
pq1.insert(4)
pq1.insert(1)
pq1.insert(7)
pq1.insert(3)
pq1.insert(9)
pq1.insert(2)
pq1.insert(4)
pq1.insert(1)
pq1.insert(7)
pq1.insert(0)
pq1.insert(9)

for v in pq1:
    print(v, end=" ")
print(" ")
pq2, pq3 = pq1.split()
for v in pq2:
    print(v,end=" ")
print(" ")
for v in pq3:
    print(v,end=" ")

# ======================== USECASE #3 ========================
print('\n======================== USECASE #3 ========================\n')

pq1 = PriorityQueue()
pq2 = PriorityQueue()

pq1.insert(4)
pq1.insert(1)
pq1.insert(7)
pq1.insert(3)
pq1.insert(9)
pq1.insert(2)

pq2.insert(4)
pq2.insert(1)
pq2.insert(7)
pq2.insert(0)
pq2.insert(9)

for v in pq1:
    print(v,end=" ")
print("")
for v in pq2:
    print(v,end=" ")
print("")
pq3 = pq1.combine(pq2)
for v in pq3:
    print(str(v),end=" ")

# ======================== USECASE #4 ========================
print('\n======================== USECASE #4 ========================\n')

pq1 = PriorityQueue()
pq1.insert(4)
pq1.insert(1)
pq1.insert(7)
pq1.insert(3)
pq1.insert(9)
pq1.insert(2)
pq1.insert(4)
pq1.insert(1)
pq1.insert(7)
pq1.insert(0)
pq1.insert(9)

for v in pq1:
    print(v, end=" ")
print(" ")

pq2, pq3 = pq_split(pq1)

for v in pq2:
    print(v,end=" ")
print(" ")
for v in pq3:
    print(v,end=" ")

# ======================== USECASE #5 ========================
print('\n======================== USECASE #5 ========================\n')

pq1 = PriorityQueue()
pq1.insert(4)
pq1.insert(1)
pq1.insert(7)
pq1.insert(3)
pq1.insert(9)
pq2 = PriorityQueue()
pq2.insert(2)
pq2.insert(4)
pq2.insert(1)
pq2.insert(7)
pq2.insert(0)
pq2.insert(9)


pq3 = pq_combine(pq1, pq2)

for v in pq3:
    print(v,end=" ")