user_text = input('Enter some text: ')

print(user_text.upper())

#--> Enter some text: Hello
#--> HELLO

user_text = input('Enter some text: ')

print(user_text.upper()) #--> BOB

user_number = input('What do you want to double? ')

# print(user_number * 2) #--> 22
print(int(user_number) * 2) #--> 4*2=8

# Challenge:
# First ask for some text, and then prompt
# "Enter 1 to uppercase and 2 to lowercase: " and 
# and then either upper or lower case it.

sentence = input("Please enter a some text: ")
user_case_change = input("Enter 1 to uppercase and 2 to lowercase: ")

if int(user_case_change) == 1:
  print(sentence.upper())
else:
  print(sentence.lower())

#--> 
# Please enter a some text: Boogers for losers!
# Enter 1 to uppercase and 2 to lowercase: 1
# BOOGERS FOR LOSERS!