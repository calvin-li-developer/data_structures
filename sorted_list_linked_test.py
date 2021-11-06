"""
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-02"
-------------------------------------------------------

"""
from sorted_list_linked import SortedList
from movie_utilities import read_movies
from movie import Movie
print("insert METHOD TEST:")


a = read_movies(open("movies.txt","r"))

list1 = SortedList()
list2 = SortedList()

i = 0
while i < 4:
    list1.insert(a[i])
    i+=1
i = 0
while i < 3:
    list2.insert(a[i])
    i+=1

print("inserted 4 movies from the first 4 lines in movies.txt:")
print("Sorted List 1")
for x in list1:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
print("_linear_search METHOD TEST:")
a = list1 [2]
print("Search list 1 that contains key:")
p,c,i = list1._linear_search(a)
a = Movie("Test", 1990, "None", 3.3, None)

print(c._data)
print("index: " + str(i))
print("============================================================")
print("============================================================")
print("Search list 1 that doesn't contains key:")
p,c,i = list1._linear_search(a)
print(p,c)
print("index: " + str(i))

print("============================================================")
print("============================================================")
print("remove METHOD TEST:")
a = list1[2]
print("remove index 2 in list 1")
list1.remove(a)
print("Sorted List 1")
for x in list1:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")
print("remove_front METHOD TEST:")
print("remove front in list 1")
list1.remove_front()
print("Sorted List 1")
for x in list1:
    print(x)
    print("============================================================")
print("============================================================")
print("============================================================")

print("index METHOD TEST:")
a = list1[-1]

print("Find the last element index of list 1:")
index = list1.index(a)
print("index: " + str(index))
print("============================================================")
print("============================================================")
print("find METHOD TEST:")
print("Find a movie not in list 1")
a = Movie("Test", 1990, "None", 3.3, None)
find = list1.find(a)
print("Result: " + str(find))

print("Find a movie that is in list 1")
a = list1[0]
find = list1.find(a)
print("Result: " + str(find))
print("============================================================")
print("============================================================")
print("peek METHOD TEST:")
print("Peek list 1:")
print(list1.peek())

print("============================================================")
print("============================================================")
print("count METHOD TEST:")
print("How many elements that are the same as index 0 in list 1?")
print("Result: " + str(list1.count(a)))
print("============================================================")
print("============================================================")
print("min METHOD TEST:")
list1 = SortedList()
a = read_movies(open("movies.txt","r"))

for x in a:
    list1.insert(x)
print("New List 1:")
for x in list1:
    print(x)
    print("============================================================")
    
print("The minimum value of list 1 is ")
print(list1.min())
print("============================================================")
print("============================================================")
print("The maximum value of list 1 is ")
print(list1.max())
print("============================================================")
print("============================================================")
print("__contains__ METHOD TEST:")
a = Movie("Test", 1990, "None", 3.3, None)
b = a in list1
print("is it true that Test movie in list 1?")
print(b)
print("is it true that Jason and the Argonauts movie in list 1?")
a = Movie("Jason and the Argonauts", 1963, "Don Chaffey", 7.4, [1,6])
b = a in list1
print(b)

print("__getitem__ METHOD TEST:")

print("Get the 2nd element of the list 1")
print(list1[1])
print("============================================================")
print("============================================================")
print("clean METHOD TEST:")
list2 = SortedList()
list2.insert(Movie("Test", 1990, "None", 3.3, None))
a = Movie("Jason and the Argonauts", 1963, "Don Chaffey", 7.4, [1,6])
list2.insert(a)
list2.insert(a)
list2.insert(a)
print("List 2")
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
list1.insert(a)
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