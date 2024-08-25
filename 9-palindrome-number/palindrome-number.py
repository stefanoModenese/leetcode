class Solution(object):
    def isPalindrome(self, x):
        
        num = list(str(x))
        i = 0
        j = len(num) - 1

        while (i < j):
            if (num[i] == num[j]):
                i = i + 1
                j = j - 1
            else:
                return False
        
        return True
        