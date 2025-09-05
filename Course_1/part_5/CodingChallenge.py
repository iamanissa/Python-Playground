# Create a function named has_remainder(), that takes two ints, and divides the first number by the second number.
# Then the function should return True if there is a remainder, and False if there is not a remainder. 


def has_remainder(int1, int2):
    num = int1 % int2
    if num > 0:
        return True
    else:
        return False

has_remainder(5, 4) #--> True