# String is data type in Python.
# string is a sequence of characters enclosed in qoutes.
# primarily,we can write a string in Three ways.

a = "shinchan"       # doble qouted 
b = '''shinchan'''   # triple qouted 
c = 'shinchan'       # single qouted 

#FACTZZZ:A String is Immutable.

#SRING SLICING 

# Definition:
# Slicing is used to extract a portion of a sequence.
#(Srting,list,or tuple) without changing the original sequence.

# Syntex: 
# Sequence[start:end:step]

# Example:

name = "shinchan"

# Extract characters from index 0 to 3 
print(name[0:4]) 
# From index 2 to end
print(name[2:])
# From beginning to index 3 
print(name[:4])
# Skip every second character
print(name[::2])
# Reverse a string 
print(name[::-1])

# NOTE:Slicing creates a new sequence,the original one remains unchanged.
# Useful for extracting, copying, and reversing data.
