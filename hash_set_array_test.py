"""
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-23"
-------------------------------------------------------

"""
from hash_set_array import *
from hash_set_array_use_case import *
hs = HashSet(20)


insert_words(open("miserables.txt", "r"), hs)

total, word, max_comp = comparison_total(hs)

print("""Using array-based list HashSet

Total Comparisons: {:,}
Word with maximum comparisons '{}': {:,}""".format(total,word,max_comp))