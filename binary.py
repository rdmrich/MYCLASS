# linear search
pos = -1


def search(lst, n):
    l = 0
    u = len(lst) - 1
    while l <= u:
        mid = (l + u) // 2
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


lst = [1, 2, 3, 4, 5, 6]
n = 44

if search(lst, n):
    print('found at ', pos)
else:
    print('not found')
