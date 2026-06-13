# 3. Write a program to detect double space in a string.

string = input("Enter a string: ")

position = string.find("  ")

if position != -1:
    print("Double space found at index:", position)
else:
    print("No double space found")

# Example   
# Input: I love  Python
#Output: Double space found at index: 6

# NOTE: find() returns the index of the first occurrence of " " and returns -1 if no double space exists.