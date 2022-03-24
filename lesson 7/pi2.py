def isPalindrome_convert(self, x):
    x = str(x)
    x_len = len(x)
    i = 0
    j = x_len - 1
    while i <= j:
        char_l = x[i]
        char_r = x[j]
        if char_r != char_l:
            return False
        else:
            i += 1
            j -= 1
    return True



    @staticmethod
    def isPalindrome_convert(x):
        x = str(x)
        x_len = len(x)
        i = 0
        j = x_len - 1
        while i <= j:
            char_l = x[i]
            char_r = x[j]
            if char_r != char_l:
                return False
            else:
                i += 1
                j -= 1
        return True