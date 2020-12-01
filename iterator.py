nums = [1, 2, 3, 5, 6, 7]

it = iter(nums)
for i in nums:
    print(it.__next__())

    i += 1

# print(next((it)))
print('class topten begin')


class topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = topten()
print(next(values))

for i in values:
    print(i)
