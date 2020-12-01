print("   /|")
print("  / |")
print(" /  |")
print("/___|")
# variables in python
name = "richard"
age = " 21 "
print("once upon a time there was a man called " + name + " ,")
print("he was " + age + "years old ")
name = "RDM"
age = "19"
print("he really liked the name " + name +",")
print("but did not like beeing " + age + " years old.")

# working with string

website = "richprogrammer.com"
print(website)
# functions
print(website.upper())
print(website.isupper())
print(website.islower())
print(website.lower())
print(len(website))
print("rich \n    programmer")
# to index string
print(website[0])
print(website.index("pro"))
print(website.replace("com", "org"))

# working with numbers
from math import *

my_num1 = -4
print(ceil(3.7))
print(sqrt(2))

my_num = -10
print(str(my_num) + " this is my favorite")
# absolute values
print(abs(my_num))
print(pow(2, 2))
print(max(1, 2, 5))
print(min(1, 2, 6))
print(round(3.2))
print(round(3.6))

# getting input from the users
'''
name = input("Enter your name: ")
age = input("enter your age: ")
print("hello " + name + " what's up, \n you are " + age + "years old")

# basics calculator
num1 = input("first number: ")
num2 = input("enter second number: ")
result = float(num1) + float(num2)
print("this is the answer > ")
print(result)
print("thank you")

# mad libs game

color = input("enter a color: ")
plural_noun = input("enter a plural noun: ")
celebrity = input("enter a celebrity: ")

print("Roses are" + color)
print(plural_noun + " are blue")
print("i love " + celebrity)

# working with lists

brothers = ["amos", "josh", "patrick", "bmp", "john"]
brothers[1] = "gift"
print(brothers[0:3])

# list function

friends = ["amos", "josh", "patrick", "bmp", "john", "john"]
lucky_numbers = [2, 4, 6, 8, 10]
friends.extend(lucky_numbers)
friends.append("junior")
friends.insert(1, "kyaruhanga")
friends.count("john")
print(friends)
lucky_numbers.sort()
lucky_numbers.insert(5,12)
print(lucky_numbers)
lucky_numbers.reverse()
lucky_numbers.insert(5,12)
print(lucky_numbers)

# working with tuples don't change

coordinates = [(1, 2, 3), (4, 5)]
print(coordinates)
'''

# functions is a collection of code or tasks

def greetings(name,age):
    print("hello " + name + " you are " + str(age) + "years old")
# calling the function
greetings("rich", 20)
greetings("luya", 25)

# return statement

def square(num):
    return num*num
result = square(3)
print(result)

# if statements in python use and ,or

is_male = True
is_tall = False
if is_male and is_tall:
    print("welcome you are a tall male")
elif is_male or is_tall:
    print("yes you are among")
else:
    print("you are not a tall and  male")

# if statement with comparison

def max_num(num1,num2,num3):

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(num1 = input("enter a number: "),
    num2 = input("enter a number: "),
    num3 = input("enter a number: ")))
# end of first session














