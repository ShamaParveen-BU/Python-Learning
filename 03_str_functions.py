name = "Shama"

# 1. len() returns the length of the string.
print(len(name))

# 2. endswith() checks if a string ends with given text.
print(name.endswith("ama"))   # output : True 
print(name.endswith("ha"))    # output : False 
print(name.startswith("Sh"))  # output : True
print(name.startswith("sh"))  # output : False  
# endwith function gives Boolean return (i.e: True/False)
# endwith function is Case-Sensitive.

# 3. count() counts total occurrences of a character.
print(name.count("a"))   # output : 2

# 4. capitalize() capitalizes the first character
text = "progress"
print(text.capitalize())  # output : Progress

# 5. find() returns the index of first occurrence.
name = "light up"
print(name.find("up"))  # output : 6

# 6. replace(old word, new word) replaces the old word with the new word in the string.
name = "raju"
print(name.replace("r","k"))  # output : kaju



