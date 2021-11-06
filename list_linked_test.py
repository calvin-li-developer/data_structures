"""
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-02"
-------------------------------------------------------

"""
from movie_utilities import read_movies
from list_linked import List
from movie import Movie
print("identical METHOD TEST:")


a = read_movies(open("movies.txt","r"))

list1 = List()
list2 = List()
identical = list1.identical(list2)
print("When list 1 and list 2 are the same empty list identical is: "+ str(identical))
i = 0
while i < 3:
    list1.insert_front(a[i])
    i+=1
i = 0
while i < 3:
    list2.insert_front(a[i])
    i+=1

identical = list1.identical(list2)
print("When list 1 and list 2 are the same non-empty list identical is: "+ str(identical))
list2.insert_front(0)
identical = list1.identical(list2)
print("When list 1 and list 2 are the different non-empty list identical is: "+ str(identical))
list2.remove_front()



print("remove_many METHOD TEST:")
a = Movie("None", 1990, "None", 3.3, None)
list2.insert_front(a)
list2.insert_front(a)
list2.insert_front(a)
for x in list2:
    print(x)
    print("============================================================")

print("============================================================")
print("============================================================")
print("Remove ALL VALUE that has movie name None in List 2")
list2.remove_many(a)
print("============================================================")
print("============================================================")
print("============================================================")

for y in list2:
    print(y)
    print("============================================================")

    
print("__getitem__ METHOD TEST:")

print("Get the 2nd element of the list 2")
print(list2[1])

print("clean METHOD TEST:")

list2.insert_front(a)
list2.insert_front(a)
list2.insert_front(a)
for x in list2:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
print("Clean ALL VALUES in List 2")
print("============================================================")
print("============================================================")
print("============================================================")
list2.clean()
for x in list2:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
print("intersection METHOD TEST:")

a = Movie("Test", 1990, "None", 3.3, None)
list2.insert_front(a)

print("List 1:")
for x in list1:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
print("List 2:")
for x in list2:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")

intersection = list1.intersection(list2)

print("intersection List:")
for x in intersection:
    print(x)
    print("============================================================")
    
print("============================================================")
print("============================================================")

print("union METHOD TEST:")

a = Movie("Test_List1", 1990, "None", 3.3, None)
list1.insert_front(a)
print("List 1:")
for x in list1:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
print("List 2:")
for x in list2:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")

union = list1.union(list2)
print("union List:")
for x in union:
    print(x)
    print("============================================================")
    
print("============================================================")
print("============================================================")

print("insert_front METHOD TEST:")

a = Movie("insert_front", 1990, "None", 3.3, None)

print("insert front of union list:")
union.insert_front(a)
print("union List:")
for x in union:
    print(x)
    print("============================================================")
    
print("============================================================")
print("============================================================")
print("combine METHOD TEST:")
a = read_movies(open("movies.txt","r"))
list1 = List()
list2 = List()
i = 0
while i < 3:
    list1.insert_front(a[i])
    i+=1
i = 2
while i < 4:
    list2.insert_front(a[i])
    i+=1
print("List 1:")
for x in list1:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
print("List 2:")
for x in list2:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
combine = list1.combine(list2)
print("combine list:")
for x in combine:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
    
print("split METHOD TEST:")

print("Splitting combine list")
ls, rs = combine.split()
print("left side list:")
for x in ls:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
print("right side list:")

for x in rs:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
print("split_alt METHOD TEST:")

combine = ls.combine(rs)
print("Split even odd index in combine list")

print("Current combine list:")
for x in combine:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
even,odd = combine.split_alt()
print("even list:")
for x in even:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
print("odd list:")
for x in odd:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
