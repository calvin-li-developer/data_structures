"""
-------------------------------------------------------
test_functions.py
[program description]
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-16"
-------------------------------------------------------

"""

from bst_linked import *
from bst_linked_use_case import *
from letter import *

# ======================== USECASE #1 ========================
print('\n======================== USECASE #1 ========================\n')

a = [11, 7, 15, 6, 9, 8 , 12, 18]
bst = BST()
for i in a:
    bst.insert(i)
print(a)
print("Inorder method: {}".format(bst.inorder()))


print("Preorder method: {}".format(bst.preorder()))

print("Postorder method: {}".format(bst.postorder()))

print("levelorder method: {}".format(bst.levelorder()))

bst_test = BST()

# ======================== USECASE #2 ========================
print('\n======================== USECASE #2 ========================\n')

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
for v in DATA1:
    bst1.insert(Letter(v))
bst2 = BST()
for v in DATA2:
    bst2.insert(Letter(v))
bst3 = BST()
for v in DATA3:
    bst3.insert(Letter(v))
    
do_comparisons(open("miserables.txt", "r"), bst1)
print("Comparing by order: " + DATA1)
print("Total Comparisons: {:,d}".format(comparison_total(bst1)))
do_comparisons(open("miserables.txt", "r"), bst2)
print("Comparing by order: " + DATA2)
print("Total Comparisons: {:,d}".format(comparison_total(bst2)))
do_comparisons(open("miserables.txt", "r"), bst3)
print("Comparing by order: " + DATA3)
print("Total Comparisons: {:,d}".format(comparison_total(bst3)))
#bst1: 31,762,167
#bst2: 8,854,330
#bst3: 8,208,847

# ======================== USECASE #3 ========================
print('\n======================== USECASE #3 ========================\n')


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
for v in DATA1:
    bst1.insert(Letter(v))
bst2 = BST()
for v in DATA2:
    bst2.insert(Letter(v))
bst3 = BST()
for v in DATA3:
    bst3.insert(Letter(v))


do_comparisons(open("miserables.txt", "r"), bst3)
letter_table(bst3)