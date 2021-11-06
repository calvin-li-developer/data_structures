"""
-------------------------------------------------------
hash_set_sorted.py
[program description]
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-11-23"
-------------------------------------------------------

"""
# Imports
# Use any appropriate data structure here.
from sorted_list_array import SortedList
# Define the new_slot slot creation function.
new_slot = SortedList

# Constants
SEP = '-' * 40


class HashSet:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, size):
        """
        -------------------------------------------------------
        Initializes an empty HashSet of size slots.
        Use: hs = HashSet(slots)
        -------------------------------------------------------
        Precondition:
            size - number of initial slots in hashset (int > 0)
        Postconditions:
            Initializes an empty HashSet.
        -------------------------------------------------------
        """
        self._size = size
        self._slots = []
        i = 0

        while i < self._size:
            self._slots.append(new_slot())
            i += 1
        self._count = 0
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the hashset.
        Use: n = len( hs )
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the hashset.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the hashset is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the hashset is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot( key )
        -------------------------------------------------------
        Postconditions:
            returns:
            slot - list at the position of hash key in self._slots
        -------------------------------------------------------
        """
        hashkey = hash(key) % self._size
        slot = self._slots[hashkey]
        return slot

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the hashset contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            Returns True if the hashset contains key, False otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        return key in slot

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the hashset, allows only one copy of value.
        Calls _rehash if the hashset _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert( value )
        -------------------------------------------------------
        Preconditions:
            value - a comparable data element (?)
        Postconditions:
            returns
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """

        # your code here
        inserted = True
        slot = self._find_slot(value)
        
        if value in slot:
            inserted = False
        else:
            inserted = True
        
            slot.insert(value)
            self._count += 1
        
            if self._count > HashSet._LOAD_FACTOR * self._size:
                self._rehash()

        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        value = slot.find(key)
        return value

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the hashset, if it exists.
        Use: value = hs.remove( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        value = slot.remove(key)
        if value is not None:
            self._count -= 1        
        
        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the hashset and reallocates the
        existing data within the hashset to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Postconditions:
            Existing data is reallocated amongst the hashset table.
        -------------------------------------------------------
        """
        temp = self._slots
        self._size = (self._size*2) + 1
        self._slots = []
        i = 0
        
        while i < self._size:
            self._slots.append(new_slot())
            i += 1
        while len(temp) > 0:
            temp_slot = temp.pop(0)
            while not temp_slot.is_empty():
                value = temp_slot.pop(0)
                slot = self._find_slot(value)
                slot.insert(value)
        return

    def debug(self):
        """
        ---------------------------------------------------------
        Prints the contents of the hashset starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Postconditions:
            The contents of the hashset are printed and the slots identified.
        -------------------------------------------------------
        """
#         obj = type(self._slots[0][0])
        i = 0
        while i < self._size:
            print(SEP)
            print("Slot {}".format(i))
            print()
            x = 0
            while x < len(self._slots[i]):
                print(self._slots[i][x])
                print()
                x +=1
            i +=1

        return