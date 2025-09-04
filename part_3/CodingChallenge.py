'''
Given numbers

Find all the even numbers in the list, and add them all together, return the sum (all the even numbers together)
'''

numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]

# Your code goes here.
new_list = []
for num in numbers:
    if num % 2 == 0:
        new_list.append(num)

return sum(new_list)

# Teachers answer.
# numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]

# total = 0 

# for number in numbers:
#     remainder = number % 2
#     if remainder == 0:
#       total = total + number

# print(total)