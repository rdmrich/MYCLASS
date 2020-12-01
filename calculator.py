# building a calculator
'''
num1 = float(input("Enter a first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter a second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator!")
'''
# Dictionnaries

month_conversions = {
    "jan": "january",
    "feb": "february",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(month_conversions["Dec"])
print(month_conversions.get("Nov"))
print(month_conversions.get("Nv", "not defined"))

# while loop

i = 1
while i <=10 :
    print(i)
    i = i + 1
print("done ")    


