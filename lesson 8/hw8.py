arr = [1, 2, 3]


class Solution:
    def PlusOne(digits: list) -> list:
        arr.append(arr[-1] + 1)
        arr.remove(arr[-2])

Solution.PlusOne(arr)
print(arr)
