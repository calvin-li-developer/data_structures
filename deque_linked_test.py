"""
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-09"
-------------------------------------------------------

"""
from deque_linked import Deque

print("------------------------------------------------------------------")
print("Deque : Insert Front Data") 
print("Inserting integers data to the front")
print("------------------------------------------------------------------")
d = Deque()
d.insert_front(1)
d.insert_front(2)
d.insert_front(3)
d.insert_front(5)
d.insert_front(4)
print("d : ", end="")
for i in d:
    print(str(i) + " ", end="")
print()
print("------------------------------------------------------------------")
print("Deque : Insert Rear Data") 
print("Inserting integers data to the rear")
print("------------------------------------------------------------------")
d.insert_rear(7)
d.insert_rear(12)
d.insert_rear(8)
print("d : ", end="")
for i in d:
    print(str(i) + " ", end="")
print()
print("------------------------------------------------------------------")
print("Deque : Remove Front Data") 
print("Remove Front Data from d")
print("------------------------------------------------------------------")
print("Removed data that was in front of d: " + str(d.remove_front()))
print("------------------------------------------------------------------")
print("Deque : Remove Rear Data") 
print("Remove Rear Data from d")
print("------------------------------------------------------------------")
print("Removed data that was at the end of d: " + str(d.remove_rear()))
print("------------------------------------------------------------------")
print("Deque : Peek Rear Data") 
print("Peek Rear Data from d")
print("------------------------------------------------------------------")
print(d.peek_rear())
print("------------------------------------------------------------------")
print("Deque : Peek Front Data") 
print("Peek Front Data from d")
print("------------------------------------------------------------------")
print(d.peek_front())
print("------------------------------------------------------------------")
print("Deque : Swap Elements in Data") 
print("Swap Elements in Data d: Swapping first and last elements of d")
print("------------------------------------------------------------------")

node1 = d._front
node2 = d._rear
 
print("Swapping the integers " + str(node1._data) + " and " + str(node2._data) + " from d: ")
for i in d:
    print(str(i) + " " , end="")
     
print()

d._swap(node1, node2)
 
for i in d:
    print(str(i) + " " , end="")
     
print()
