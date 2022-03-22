def get_list() -> list:
    return list(range(0 , 1_000_000, 2))

class Solution:
    def find_target(self,list,target):
        left = -1
        right = len(list)
        while right > left + 1:
            middle = (left + right) // 2
            if list[middle] >= target:
                right = middle
            else:
                left = middle
        return right

Solution().find_target(get_list(), 13131)