class Solution:

    @staticmethod
    def isPalindrome(x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        x_revers = 0
        while x_revers < x:
            x_revers = x_revers * 10 + x % 10
            x = x // 10
            if x_revers == x:
                return True
        if x_revers == x or x_revers // 10 == x:
            return True
        return False


if __name__ == '__main__':
    print(Solution.isPalindrome(14411))
