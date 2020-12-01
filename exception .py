"""
Errors
    compile time
        syntactical errors#
            eg missing (:)
            wrong spelling
    logical error
        eg wrong output
    runtime error
        eg divide by zero

"""

a = 3
b = 2

try:
    print('resource open')
    print(a/b)
    k = int(input("enter a number : "))
    print(k)
except ZeroDivisionError as e:
    print('hey you can '
          'not divide '
          'a number by zero', e)
except ValueError as e:
    print('invalid input')

except Exception as e:
    print('something went wrong')
finally:
    print('resource closed ')
print("bye")