import random 

lucky_number = random.randint(1, 100)

messages = ["You will have a great day!", "Today will be tough...but worth it!", "You will get married this year!"]

fortune_messages = random.choice(messages)

print(f'{fortune_messages} Your lucky number is: {lucky_number}')
#--> You will get married this year! Your lucky number is: 6
#--> Today will be tough...but worth it! Your lucky number is: 15