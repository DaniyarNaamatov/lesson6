def get_list() -> list:
    return list(range(0, 1_000_000_000, 2))

class Solution:
    def find_target(self, list, target):
        min_b = 0
        max_b = len(list)
        pop = 0
        while min_b < max_b:
            pop += 1
            middle = (min_b + max_b) // 2
            if list[middle] == target:
                return pop
            elif list[middle] > target:
                max_b = middle - 1
            elif list[middle] < target:
                min_b = middle + 1
        return pop

p = (Solution().find_target(get_list(), 545635))
print(p)
