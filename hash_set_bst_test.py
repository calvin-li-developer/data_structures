"""
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-23"
-------------------------------------------------------

"""
from hash_set_bst import HashSet
from hash_set_bst_use_case import insert_words, comparison_total_bst
hs = HashSet(20)


insert_words(open("miserables.txt", "r"), hs)

total, word, max_comp = comparison_total_bst(hs)

print("""Using linked BST HashSet

Total Comparisons: {:,}
Word with maximum comparisons '{}': {:,}""".format(total,word,max_comp))