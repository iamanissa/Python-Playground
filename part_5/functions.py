def bark():
  print('Woof woof!')

def hello_nick():
  print('Hello Nick!')

bark() #--> Woof woof!
hello_nick() #--> Hello Nick!

# With parameters
def hello(name):
  print(f'Hello {name}!')

hello("World") #--> Hello World!
hello("Sarah") #--> Hello Sarah!

# With multiple params
def add_numbers(num1, num2):
  print(num1+num2)

add_numbers(1,2) #--> 3
add_numbers(10,2) #--> 12

# Challenge: Create a function called dog_info that takes in a dogs age and name and prints a sentence about the dog
def dog_info(age, name):
  print(f"{name} is a cute dog and is {age} years old")

dog_info(2, "Bella") #--> Bella is a cute dog and is 2 years old

# Return values
def double(num):
  return num * 2

print(double(5))

new_number = double(10)

print(new_number)

# Challenge: Create a function that returns a string in all Caps
def caps_lock(string):
  return string.upper()

print(caps_lock("I don't think you're ready for this!")) #--> I DON'T THINK YOU'RE READY FOR THIS!

# With a list of names 
names = ["John", "Jane", "Doe", "Joe", "Bob", "Alice"]

for name in names:
  print(caps_lock(name))

#--> JOHN
# JANE
# DOE
# JOE
# BOB
# ALICE