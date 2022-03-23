def get_list() -> list:
    return list(range(0, 1_000, 2))

class Solution:
    def find_target(self,list,target):
    low = 0
    high = len(list) - 1
    while low <= high:
        midle = (low + high)
        guess = list[midle]
        if guess == find_target():
            return midle
        if guess > find_target():
            high = midle - 1
        else:
            low = midle + 1
    return None


print(Solution().find_target(get_list(),426))
