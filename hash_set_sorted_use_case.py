
"""
-------------------------------------------------------
asgn09.py
[program description]
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-23"
-------------------------------------------------------

"""
from word import Word
def insert_words(file_variable, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a HashSet.
    -------------------------------------------------------
    Preconditions:
        file_variable - the already open file containing data to evaluate (file)
        hash_set - the HashSet to insert the words into (HashSet)
    Postconditions:
        Each Word object in hash_set contains the number of comparisons
        required to insert that Word object from file_variable into hash_set.
    -------------------------------------------------------
    """
    line = file_variable.readline()
    while line != "":
        for word in line.split():
            if word.isalpha():
#                 print(word.lower())
                hash_set.insert(Word(word.lower()))
        line = file_variable.readline()

def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    -------------------------------------------------------
    Preconditions:
        hash_set - a hash set of Word objects (HashSet)
    Postconditions:
        returns
        total - the total of all comparison fields in the HashSet
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_comp = 0
    word = ""
    i = 0
    #Not sure how to write this function without using the underlying ADT of _slots
    #unless this is the right way to do it
    while i < 20:
        while not hash_set._slots[i].is_empty():
            index_temp = hash_set._slots[i].pop(0)
            if index_temp.comparisons > max_comp:
                max_comp = index_temp.comparisons
                word = index_temp.word
            total = total + index_temp.comparisons
        i +=1 
    
    return total, word, max_comp

def comparison_total_bst(hash_set):
    total = 0
    max_comp = 0
    word = ""
    i = 0
    #Not sure how to write this function without using the underlying ADT of _slots
    #unless this is the right way to do it
    while i < 20:
        temp_slot_list = hash_set._slots[i].inorder()
        for x in temp_slot_list:
            if x.comparisons > max_comp:
                max_comp = x.comparisons
                word = x.word
                total = total + x.comparisons
        i +=1 
    
    return total, word, max_comp
    