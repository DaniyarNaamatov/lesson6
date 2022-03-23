def get_list() -> list:
  return list(range(0,1_000_000, 2))

class Solution:
    def find_target(self,list,target):
        floor_index = -1
        ceiling_index = len(list)
        while floor_index + 1 < ceiling_index:
            distance = floor_index + ceiling_index
            half_distance = distance/2
            guess_index = floor_index + half_distance
            guess_value = list[guess_index]
            if guess_value == target:
                return True
            if guess_value > target:
                ceiling_index = guess_index
            else:
                floor_index = guess_index
            return False

Solution().binarySearch(get_list(), 13131)