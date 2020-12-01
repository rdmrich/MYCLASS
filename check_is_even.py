"""
Write a function is_even that takes 
in a number and returns True if it is even,
otherwise false.

HINT:
Question: What does it mean for a number 
to be divisible by another number?

Answer: number % another_number == 0 
# Gives you true

Ex: 12 % 3 == 0  --> True  
--> This means 12 is divisble by 3.

BONUS CHALLENGE:
Write the function solution in 1 line 
of code without using if statements.
"""

# Make sure to un-comment the function line below when you are done.
# Remember to name your function is_even
# WRITE YOUR CODE HERE...
def is_even(number):
  if number % 2 == 0:
    return True
  else:
    return False
#second way of doing

def is_even(number):
    return number % 2 == 0

#check if is odd
def is_odd(number):
  return number % 2 != 0
  
 


# DO NOT remove lines below here,
# this is designed to test your code.

def test_is_even():
  assert is_even(2) == True
  assert is_even(3) == False
  assert is_even(8) == True
  assert is_even(100) == True
  assert is_even(101) == False
  print("YOUR CODE IS CORRECT!")
  
# test your code by un-commenting the line(s) below
test_is_even()
