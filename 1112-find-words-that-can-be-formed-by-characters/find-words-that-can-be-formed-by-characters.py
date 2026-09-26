
class Solution(object):
    def countCharacters(self, words, chars):
        ans = 0
        # Count frequencies of characters in chars using standard dictionary or count method
        for word in words:
            possible = True
            for char in word:
                if word.count(char) > chars.count(char):
                    possible = False
                    break
            if possible:
                ans += len(word)
        return ans
