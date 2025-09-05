# Receive an input from a user and allow them to guess the number until they correctly guess the number
# 1. After that works, also monitor how many times they have guessed.
# 2. Tell user if they should guess higher or lower
# 3. Make it so the correct_number changes
# 4. Make the game robot feel a little more real with pauses

# guess = int(input("What is your guess?: "))
# correct_number = 5
# guess_count = 1

# while guess != correct_number:
#   guess_count += 1
#     guess = int(input("What is your guess?: "))

# print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses")

#-->
# What is your guess?: 1
# What is your guess?: 5
# Congrats! The right answer was 5. It took you 2 guesses

######################################## 2 and 3 ######################################################
# import random

# print("Hi! Welcome to the guessing game. Please guess a number between 1 and 100")
# guess = int(input("What is your guess?: "))
# correct_number = random.randint(1,100)
# guess_count = 1

# while guess != correct_number:
#   guess_count += 1
#   if guess < correct_number:
#       guess = int(input("Wrong. You need to guess higher. What is your guess?: "))
#   else: 
#       guess = int(input("Wrong. You need to guess lower. What is your guess?: "))


# print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses")

#-->
#  Hi! Welcome to the guessing game. Please guess a number between 1 and 100
# What is your guess?: 2
# Wrong. You need to guess higher. What is your guess?: 5
# Wrong. You need to guess higher. What is your guess?: 80
# Wrong. You need to guess lower. What is your guess?: 40
# Wrong. You need to guess lower. What is your guess?: 30
# Wrong. You need to guess lower. What is your guess?: 20
# Wrong. You need to guess lower. What is your guess?: 15
# Wrong. You need to guess lower. What is your guess?: 12
# Wrong. You need to guess lower. What is your guess?: 10
# Wrong. You need to guess lower. What is your guess?: 8
# Wrong. You need to guess lower. What is your guess?: 7
# Wrong. You need to guess lower. What is your guess?: 6
# Congrats! The right answer was 6. It took you 12 guesses

############################################ and 4 ####################################################
import random
import time

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100")
time.sleep(3)
print("Piking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
    time.sleep(1)
  guess_count += 1
  if guess < correct_number:
      guess = int(input("Wrong. You need to guess higher. What is your guess?: "))
  else: 
      guess = int(input("Wrong. You need to guess lower. What is your guess?: "))


print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses")

#--> Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100
# Piking a number...
# What is your guess?: 50
# Wrong. You need to guess higher. What is your guess?: 80
# Wrong. You need to guess lower. What is your guess?: 60
# Wrong. You need to guess higher. What is your guess?: 70
# Congrats! The right answer was 70. It took you 4 guesses