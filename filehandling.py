
f = open('myfile', 'r')
for data in f:
    print(data)

print(f.readline(), end='')

f1 = open('licence', 'r')
#f1.write('this is legal infos about how you will use this software')
for data in f1:
   print(data)




