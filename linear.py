# linear search
pos = -1


def search(lst, n):
    i = 0
    # while i < len(lst):
    for i in lst:
        if lst[i] == n:
            globals()['pos'] = i
            return True
        i += 1

    return False


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 7

if search(lst, n):
    print('found at ', pos)
else:
    print('not found')
