import sys
# recursion
sys.setrecursionlimit(500)

print(sys.getrecursionlimit())
i = 0
def greet():
    global i
    i += 1
    print("hey", i)
    greet()
greet()