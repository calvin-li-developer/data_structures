from stack_use_case import *
from stack_array import *

# ======================== USECASE #1 ========================
print('======================== USECASE #1 ========================')
# Constants
BALANCED = 0
MORE_LEFT = 1
MORE_RIGHT = 2
MISMATCHED = 3
string = "{a × 2 - [(c - d) × 4]} × sin(x - y)"

is_balanced = balanced_brackets(string)
if is_balanced == BALANCED:
    print("'{}' has balanced brackets.".format(string))
elif is_balanced == MORE_LEFT:
    print("'{}' has more left brackets.".format(string))
elif is_balanced == MORE_RIGHT:
    print("'{}' has more right brackets.".format(string))
else:
    print("'{}' has been mismatched.".format(string))

string2 = "{a × 2 - [(c - d) × 4}]"
is_balanced = balanced_brackets(string2)

if is_balanced == BALANCED:
    print("'{}' has balanced brackets.".format(string2))
elif is_balanced == MORE_LEFT:
    print("'{}' has more left brackets.".format(string2))
elif is_balanced == MORE_RIGHT:
    print("'{}' has more right brackets.".format(string2))
else:
    print("'{}' has been mismatched.".format(string2))

# ======================== USECASE #2 ========================
print('======================== USECASE #2 ========================')

string = "racecar"

is_palindrome = palindrome_stack(string)

print("is '{}' a palindrome:".format(string))
print(is_palindrome)

string2 = "A man, a plan, a canal, Panama!"

is_palindrome = palindrome_stack(string2)

print("is '{}' a palindrome:".format(string2))
print(is_palindrome)

# ======================== USECASE #3 ========================
print('======================== USECASE #3 ========================')

values_in = ["1"]
opstring="SX"
values_out = reroute(opstring, values_in)
print(values_out)

values_in = ["1","2","3"]
opstring="SXSSXX"
values_out = reroute(opstring, values_in)
print(values_out)

# ======================== USECASE #4 ========================
print('======================== USECASE #4 ========================')

s1 = Stack()
s1.push(1)
s1.push(5)
s1.push(7)
s1.push(8)
s1.push(9)
s1.push(12)
s1.push(14)
s1.push(8)
s2, s3 = stack_split(s1)
print("s2:")
print("Top")
while not s2.is_empty():
    print(s2.pop())
print("Bottom")
print("s3:")
print("Top")
while not s3.is_empty():
    print(s3.pop())
print("Bottom")

# ======================== USECASE #5 ========================
print('======================== USECASE #5 ========================')

s1 = Stack()
s1.push(1)
s1.push(5)
s1.push(7)
s1.push(8)
s1.push(9)
s1.push(12)
s1.push(14)
s1.push(8)

s2, s3 = s1.split()
print("s2:")
print("Top")
while not s2.is_empty():
    print(s2.pop())
print("Bottom")
print("s3:")
print("Top")
while not s3.is_empty():
    print(s3.pop())
print("Bottom")