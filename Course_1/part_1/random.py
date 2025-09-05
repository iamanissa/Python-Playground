import random

print(random.randint(1,10)) # --> 9

# If you want a float
print(random.random()) # --> 0.839790


# Make your own version of the Magic 8 Ball that prints yes, no, or maybe when you run it.
mylist = ["Yes", "No", "Maybe"]

print(random.choice(mylist)) # --> "Yes"

# Teachers answer
answer = random.randint(1,3) 

if answer == 1:
  print("Yes")
elif answer == 2:
  print("No")
else:
  print("Maybe")
# --> "Maybe"