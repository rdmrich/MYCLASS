if True:
    print("i m rich")
print("checking user")
x = 6  #int(input('enter a number'))
r = x % 2
if r == 0:
    print("Even")
    if x > 3:
        print("greater")
    else:
        print("not greater")
elif r != 0:
    print("Odd")
else:
    print("nor even nor odd")

# while loop
print("While loop")
days_week = 7#initialisation
hours_day = 24
while days_week <= 7: #condition
    print("i am looping in days", days_week) #expression
    while hours_day <= 24:
        print("real time", hours_day)
        hours_day += 1#increment or decrement
    days_week += 1
print()
#for loop
print("for loop")
name = {"dush", "mud", "rich"}
for i in name:
    print(i)
    for i in range(10):
        if i % 10:
            print(i)
print()
# break continue
print("break pass")
stock = 5
a = int(input("how many capati do u want ?"))
i = 1
while i <= a:
    if i >= stock:
        print("out of stock")
        break
    print("capati")
    i +=1
    #break continue
print("break continue")
for b in range(1, 10):
    if b % 2:
        break
    print(i)
    b += 1
for t in range(5):
    if t == 3:
        continue
        #pass
    print("hello", t)

# printing patterns
for h in range(4):
    for j in range(4):
        print("#", end="")
    print()
# triangle
for h in range(4):
    for j in range(h):
        print("*", end="")
    print()
# tr
for h in range(4):
    for j in range(4-h):
        print("#", end="")
    print()

# for else
y = [1, 2, 3, 4, 5]
for y in y:
    if y % 2 == 0:
        print(y)
    else:
        print("not found")









