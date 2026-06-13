# 2. Write a program to fill in a letter template given below with name and date.
#Dear <|Name|>,

#You are selected!

#Date: <|Date|>

name = input("Enter your name: ")
date = input("Enter the date: ")

letter = '''
Dear <|Name|>,

You are selected!

Date: <|Date|>
'''

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter) 

# Example output:
#Enter your name: Rahul
#Enter the date: 14 June 2026

#Dear Rahul,

#You are selected!

#Date: 14 June 2026

# Shorter Solution (Using f-strings)
name = input("Enter your name: ")
date = input("Enter the date: ")

print(f'''
Dear {name},

You are selected!

Date: {date}
''')

# NOTE: The replace() version is usually preferred for this exercise,
# because it demonstrates how to fill placeholders in a template.