'''
A dictionary in Python is a collection of key-value pairs, where each key is unique and maps to a specific value. 
It's similar to a real-life dictionary where you look up a word (the key) to find its definition (the value).

Here's a basic example:
python
cats = {
"Jane": 6,
"Tom": 14,
"Sara": 8
}

In this example, "Jane", "Tom", and "Sara" are keys, and 6, 14, and 8 are their respective values. 
You can access a value by using its key, like this:
python
print(cats["Tom"]) # Output: 14

Dictionaries are created using curly brackets {} and are very useful for organizing and retrieving data efficiently.
Mental Note 🧠: this is the same as a Ruby Hash
'''


movies = {
    "The Little Princess": 1995, 
    "The King and I": 1956, 
    "The Lego Movie": 2014
    }

# Use the Key to show the value
print(f'The King and I was released in {movies["The King and I"]}')
#--> The King and I was release in 1956

# Add
movies["Pride and Prejudice"] = 2005
#--> {'The Little Princess': 1995, 'The King and I': 1956, 'The Lego Movie': 2014, 'Pride and Prejudice': 2005}

print(movies)

del(movies["Pride and Prejudice"])

print(len(movies)) #--> 3
print(movies) #--> {'The Little Princess': 1995, 'The King and I': 1956, 'The Lego Movie': 2014}

# Challenge
# Make dictionary with Ints for keys and booleans for values




