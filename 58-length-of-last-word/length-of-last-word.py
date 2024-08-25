class Solution(object):
    def lengthOfLastWord(self, s):
        
        words = s.split()

        return len(words[len(words)-1])
        