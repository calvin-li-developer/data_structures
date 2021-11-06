"""
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-10-26"
-------------------------------------------------------

"""
from sorted_list_array import SortedList
from movie_utilities import read_movies

a = read_movies(open("movies.txt","r"))
b = read_movies(open("movies.txt","r"))


list_m1 = SortedList()
for x in a:
    list_m1.insert(x)
list_m2 = SortedList()
for y in b:
    list_m2.insert(y)


list = SortedList()

list.insert(2)
list.insert(2)
list.insert(2)
list.insert(2)

list.insert(1)
list.insert(1)
list.insert(1)
list.insert(1)

list.insert(3)
list.insert(3)
list.insert(3)

list.insert(4)
list.insert(4)

list2 = SortedList()

list2.insert(2)
list2.insert(2)
list2.insert(2)
list2.insert(2)

list2.insert(1)
list2.insert(1)
list2.insert(1)

list2.insert(3)
list2.insert(3)
list2.insert(3)

list2.insert(4)
list2.insert(4)


list

print("----------------SORTEDLIST ARRAY TESTING----------------")

print("Testing remove method:")

string = "["
for i in list:
    string = string + str(i) + ", "
print("List before removing value 1 from it:{}]".format(string[:-2]))
list.remove(1)
string = "["
for i in list:
    string = string + str(i) + ", "
print("List after removing value 1 from it:{}]".format(string[:-2]))
print("____________________________________________________________")
print("Testing index method:")
n = list.index(2)
print("index of the list that contain value of 2: {}".format(n))
print("____________________________________________________________")
print("Testing find method:")
n = list.find(3)
print("Finds the value 3 in the sorted list and returns the matching value: {}".format(n))
print("____________________________________________________________")
print("Testing peek method:")
print("The first value in the list is {}".format(list.peek()))
print("____________________________________________________________")
print("Testing identical method:")
b = list_m1.identical(list_m2)
print("List Movie 1:" )
for i in list_m1:
    print(i)
print()
print("List Movie 2: ")

for i in list_m2:
    print(i)
print()
print("Is True that list Movie 1 and List Movie 2 is the same? {}".format(b))
print("____________________________________________________________")
print("Testing remove_front method:")
string2 = "["
for i in list2:
    string2 = string2 + str(i) + ", "
print("List 2: {}]".format(string2[:-2]))
list2.remove_front()
string2 = "["
for i in list2:
    string2 = string2 + str(i) + ", "
print("First value of List 2 is removed: {}]".format(string2[:-2]))
print("____________________________________________________________")
print("Testing remove_front method:")
print("List 2: {}]".format(string2[:-2]))
list2.remove_many(2)
string2 = "["
for i in list2:
    string2 = string2 + str(i) + ", "
print("All the values of 2 in List 2 is removed: {}]".format(string2[:-2]))
print("____________________________________________________________")
print("Testing count, min, max method:")
print("List 1: {}]".format(string[:-2]))
num = list.count(1)
print("There are {} 1's in List 1".format(num))
min = list.min()
max = list.max()
print("The max value is {} and min value is {} in List 1".format(max,min))
print("Testing contains method:")
bool = 4 in list
print("Is it true that the value 4 is in List 1? {}".format(bool))
print("Testing getitem method:")
item4 = list[4]
print("The 4th index in List 1 is {}".format(item4))
print("____________________________________________________________")
print("Testing clean method:")
string = "["
for i in list:
    string = string + str(i) + ", "

print("List 1: {}]".format(string[:-2]))

list.clean()
string = "["
for i in list:
    string = string + str(i) + ", "
print("The cleaned List 1 is: {}]".format(string[:-2]))


print("____________________________________________________________")
print("Testing intersect method:")
list.remove_front()
string = "["
for i in list:
    string = string + str(i) + ", "
print("List 1: {}]".format(string[:-2]))
print("List 2: {}]".format(string2[:-2]))
list3 = list.intersection(list2)
string3 = "["
for i in list3:
    string3 = string3 + str(i) + ", "
print("The intersection of List 1 and List 2 is: {}]".format(string3[:-2]))



print("____________________________________________________________")
print("Testing union method:")
print("List 1: {}]".format(string[:-2]))
print("List 2: {}]".format(string2[:-2]))

list4 = list.union(list2)
string4 = "["
for i in list4:
    string4 = string4 + str(i) + ", "

print("The union of List 1 and List 2 is: {}]".format(string4[:-2]))


