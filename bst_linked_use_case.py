"""
-------------------------------------------------------
asgn08.py
[program description]
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-16"
-------------------------------------------------------

"""
from bst_linked import BST
from letter import *

# DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects.
    -------------------------------------------------------
    Preconditions:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 letter objects 
            to retrieve data from (BST)
    Postconditions:
        Each letter object in bst contains the number of comparisons
        found by searching for that letter object in file_variable.
    -------------------------------------------------------
    """

    line = file_variable.readline()
    while line != "":
        line = line.strip()
        i = 0
        while i < len(line):
            if line[i].isalpha():
                lettered = Letter(line[i].upper())
                bst.retrieve(lettered)
            i += 1
        line = file_variable.readline()
    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all letter objects in bst.
    -------------------------------------------------------
    Preconditions:
        bst - a binary search tree of letter objects (BST)
    Postconditions:
        returns
        total - the total of all comparison fields in the bst
            letter objects (int)
    -------------------------------------------------------
    """
    return comparison_total_aux(bst._root)


def comparison_total_aux(node):
    total = 0
    if node is not None:
        total = node._data.comparisons + \
            comparison_total_aux(node._left) + \
            comparison_total_aux(node._right)
    return total


def count_total(bst):
    return count_total_aux(bst)


def count_total_aux(node):
    total = 0
    if node is not None:
        total = node._data.count + \
            count_total_aux(node._left) + count_total_aux(node._right)
    return total


def letter_table_aux(node, t):
    if node is not None:
        print('     {}  {:>9,d}  {:>5.2%}'.format(node._data.letter,
                                  node._data.count, node._data.count / t))
        letter_table_aux(node._left, t)
        letter_table_aux(node._right, t)
    return


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts.
    -------------------------------------------------------
    Preconditions:
        bst - a binary search tree of letter objects (BST)
    Postconditions:
        Prints a table of letter counts for each letter object
        in bst
    -------------------------------------------------------
    """
    print("letter Count/Percent Table")
    total = count_total(bst._root)
    print('\nTotal Count: {}'.format(total))
    print("""Letter      Count       %""")
    
    return letter_table_aux(bst._root, total)

