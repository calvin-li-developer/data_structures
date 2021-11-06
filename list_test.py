"""
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-10-25"
-------------------------------------------------------

"""
from movie_utilities import read_movies
from list_array import List
a = read_movies(open("movies.txt","r"))
b = read_movies(open("movies.txt","r"))

list1 = List()
for x in a:
    list1.insert_front(x)
list2 = List()
for y in b:
    list2.insert_front(y)

i = 0
a = ""
for i in list1:
    a = a + str(i) + ", "
a = a[:-2]
print("----------------LIST ARRAY TESTING----------------")
print("Testing identical method:")
print("List 1: [{}]".format(a))
b = ""
for i in list2:
    b = b + str(i) + ", "
b = b[:-2]

print("List 2: [{}]".format(b))
bool = list1.identical(list2)
print("List 1 and List 2 are identical? {}".format(bool))
print()
list2.append(list1[1])
print("List 1: [{}]".format(a))
b = ""
for i in list2:
    b = b + str(i) + ", "
b = b[:-2]
print("List 2: [{}]".format(b))
bool = list1.identical(list2)
print("List 1 and List 2 are identical? {}".format(bool))
print()
a = ""
for x in list1:
    a = a + str(x) + ", "
a = a[:-2]

print("List 1: [{}]".format(a))
b = ""
for i in list2:
    b = b + str(i) + ", "
b = b[:-2]
print("List 2: [{}]".format(b))

bool = list1.identical(list2)
print("List 1 and List 2 are identical? {}".format(bool))
print()
list2.remove(list1[0])
b = ""
for i in list2:
    b = b + str(i) + ", "
b = b[:-2]
print("List 1: [{}]".format(a))
print("List 2: [{}]".format(b))
bool = list1.identical(list2)
print("List 1 and List 2 are identical? {}".format(bool))

print("____________________________________________________________")
print("Testing remove_many method:")
list1.insert(0, list1[1])
list1.insert(-1, list1[1])
list1.insert(int(len(list1)/2),list1[1])
before = ""
for x in list1:
    before = before + str(x) + ", "
before = before[:-2]
list1.remove_many(list1[1])
after = ""
for x in list1:
    after = after + str(x) + ", "
after = after[:-2]
print("Remove all value that is {}.".format(i))
print("List that contains values of {}: [{}]".format(i,before))
print("List that doesn't contain values of {}: [{}]".format(i,after))
print("____________________________________________________________")
print("Testing __getitem__ method:")
print("Value of the last index in list1 is {}".format(list1[-1]))
print("____________________________________________________________")
print("Testing clean method:")
list1.insert(0, i)
list1.insert(-1, i)
list1.insert(int(len(list1)/2),i)
a = ""
for x in list1:
    a = a + str(x) + ", "
a = a[:-2]
print("List that contains many values of {}: [{}]".format(i,a))
list1.clean()
a = ""
for x in list1:
    a = a + str(x) + ", "
a = a[:-2]

print("List that contains only 1 value of {}: [{}]".format(i,a))
print("____________________________________________________________")
print("Testing intersection method:")
list3 = List()

c = ""
for x in list3:
    c = c + str(x) + ", "
c = c[:-2]
print("List 1 :[{}]".format(a))
print("List 3 :[{}]".format(c))
intersect_list = list1.intersection(list3)
d = ""
for x in intersect_list:
    d = d + str(x) + ", "
d = d[:-2]
print("List 1 intersect List 3:[{}]".format(d))
print("____________________________________________________________")
print("Testing union method:")

print("List 1 :[{}]".format(a))
print("List 3 :[{}]".format(c))
union_list = list1.union(list3)
d = ""
for x in union_list:
    d = d + str(x) + ", "
d = d[:-2]
print("List 1 union List 3:[{}]".format(d))
print("____________________________________________________________")
print("Testing insert_front method:")
print("List 1 :[{}]".format(a))
list1.insert_front(None)
a = ""
for x in list1:
    a = a + str(x) + ", "
a = a[:-2]
print("insert None value to front of List 1: [{}]".format(a))
print("____________________________________________________________")
print("Testing remove_front method:")
print("List 1 :[{}]".format(a))
list1.remove_front()
a = ""
for x in list1:
    a = a + str(x) + ", "
a = a[:-2]
print("remove the front/first value of List 1:[{}]".format(a))
print("____________________________________________________________")
print("Testing combine method:")
list3.clean()
c = ""
for x in list3:
    c = c + str(x) + ", "
c = c[:-2]
print("List 1 :[{}]".format(a))
print("List 3 :[{}]".format(c))
combine_list = list1.combine(list3)
f = ""
for x in combine_list:
    f = f + str(x) + ", "
f = f[:-2]
print("The combined List of List 1 and List 3 is: [{}]".format(f))
c = ""
for x in list3:
    c = c + str(x) + ", "
c = c[:-2]
a = ""
for x in list1:
    a = a + str(x) + ", "
a = a[:-2]
print("New List 1 :[{}]".format(a))
print("New List 3 :[{}]".format(c))
print("____________________________________________________________")
print("Testing split method:")
i=0
while i < 11:
    list3.append(i)
    i+=1
c = ""
for x in list3:
    c = c + str(x) + ", "
c = c[:-2]
print("List 3 :[{}]".format(c))
ls,rs = list3.split()
ls_s = ""
for x in ls:
    ls_s = ls_s + str(x) + ", "
ls_s = ls_s[:-2]
rs_s = ""
for x in rs:
    rs_s = rs_s + str(x) + ", "
rs_s = rs_s[:-2]
print("Left side of List 3: [{}]".format(ls_s))
print("Right side of List 3: [{}]".format(rs_s))
c = ""
for x in list3:
    c = c + str(x) + ", "
c = c[:-2]
print("New List 3 :[{}]".format(c))
print("____________________________________________________________")
print("Testing split_alt method:")
i=0
number = 2
while i < 100:
    list3.append(i)
    list3.append(number)
    list3.append(number*2)
    number +=1
    i = (i+i+2)
c = ""
for x in list3:
    c = c + str(x) + ", "
c = c[:-2]
print("List 3 :[{}]".format(c))
even,odd = list3.split_alt()
even_s = ""
for x in even:
    even_s = even_s + str(x) + ", "
even_s = even_s[:-2]
odd_s = ""
for x in odd:
    odd_s = odd_s + str(x) + ", "
odd_s = odd_s[:-2]
print("Even indexed values in List 3: [{}]".format(even_s))
print("Odd indexed values in List 3: [{}]".format(odd_s))
c = ""
for x in list3:
    c = c + str(x) + ", "
c = c[:-2]
print("New List 3 :[{}]".format(c))






