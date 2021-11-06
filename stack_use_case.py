"""
-------------------------------------------------------
Author:  Chang Xing (Calvin) Li
ID:      161574090
Email:   lixx4090@mylaurier.ca
__updated__ = "2017-09-27"
-------------------------------------------------------

"""
from stack_array import Stack
# Constants
BALANCED = 0
MORE_LEFT = 1
MORE_RIGHT = 2
MISMATCHED = 3


def balanced_brackets(string):
    """
    -------------------------------------------------------
    Determines if a string contains balanced brackets or not. Non-bracket
    characters are ignored. Uses a stack. Brackets include {}, [], (), <>.
    Use: is_balanced = balanced_brackets(string)
    -------------------------------------------------------
    Preconditions:
        string - the string to test (str)
    Postconditions:
        returns
        is_balanced (int) -
            BALANCED if the brackets in string are balanced
            MISMATCHED if the brackets in string are mismatched
            MORE_RIGHT if there are more right brackets than left in string
            MORE_LEFT if there are more left brackets than right in string
    -------------------------------------------------------
    """
    stack = Stack()
    is_balanced = None
    i = 0
    while i < len(string) and is_balanced == None:
        if string[i] == "(" or string[i] == "[" or string[i] == "{":
            stack.push(string[i])
        elif string[i] == ")" or string[i] == "]" or string[i] == "}":
            if string[i] == ")":
                temp_s = "("
            elif string[i] == "]":
                temp_s = "["
            elif string[i] == "}":
                temp_s = "{"

            if stack.is_empty():
                is_balanced = MORE_RIGHT
            elif temp_s != stack.peek():
                is_balanced = MISMATCHED
            elif temp_s == stack.peek():
                stack.pop()
        i += 1

    if not stack.is_empty() and is_balanced == None:
        is_balanced = MORE_LEFT
    elif is_balanced == None:
        is_balanced = BALANCED
    return is_balanced


def palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, spaces, and
    punctuation in string. Uses a stack.
    Use: is_palindrome = palindrome_stack(string)
    -------------------------------------------------------
    Preconditions:
        string - a string (str)
    Postconditions:
        returns
        is_palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    is_palindrome = None
    stack = Stack()
    temp_string = ""
    sum_constant = 1
    '''
    only takes alphabets and storing into temp_string
    '''
    for i in range(len(string)):
        if string[i].isalpha():
            temp_string = temp_string + string[i].lower()

    '''
    If dividing temp_string gives me remainders then start from 2(odd number)
    '''
    if len(temp_string) % 2 != 0:
        sum_constant = 2
    '''
    add the first half of temp_string into the stack
    '''
    for x in range(int(len(temp_string)/2)):
        stack.push(temp_string[x])

    '''
    x will be at a position on the last half of temp_string
    '''
    x = int(len(temp_string)/2 - 1) + sum_constant
    '''
    comparing stack(first half of string to temp_string(second half)
    '''

    while x < int(len(temp_string)) and is_palindrome == None:
        if temp_string[x] == stack.peek():
            stack.pop()
            x += 1
        else:
            is_palindrome = False

    if stack.is_empty():
        is_palindrome = True

    return is_palindrome


def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Preconditions:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Postconditions:
        returns
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns 
            None (list of ?)
    -------------------------------------------------------
    """
    stack = Stack()
    templist = []
    values_out = []
    i = 0
    while len(values_in):
        value = values_in.pop()
        templist.append(value)

    while i < len(opstring) and not values_out == None:

        if opstring[i] == "S":
            if len(templist) != 0:
                value = templist.pop()
                stack.push(value)
        elif opstring[i] == "X":
            if not stack.is_empty():
                value = stack.pop()
                values_out.append(value)
            else:
                values_out = None
        i += 1

    return values_out


def stack_split(s1):
    """
    -------------------------------------------------------
    Splits the given stack into separate stacks. s1 is empty when
    function is done. Items are alternately pushed onto the returned stacks.
    Order is not significant.
    Use: s2, s3 = stack_split(s1)
    -------------------------------------------------------
    Preconditions:
        s1 - the stack to split into two parts (Stack)
    Postconditions:
        returns
        s2 - contains alternating values from given stack (Stack)
        s3 - contains other alternating values from given stack (Stack)
    -------------------------------------------------------
    """
    s2 = Stack()
    s3 = Stack()
    
    while not s1.is_empty():
        value = s1.pop()
        s2.push(value)
        if not s1.is_empty():
            value = s1.pop()
            s3.push(value)

    return s2, s3
