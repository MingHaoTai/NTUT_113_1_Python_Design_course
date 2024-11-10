# 2024-11-10
# Roman to Integer
# I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
# ex: III = 3, IV = 4, VI = 6

class Solution(object):
    def romanToInt(self, s : str) -> int:
        lib = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        total = lib[s[0]]
        for i in range(1, len(s)):
            if lib[s[i]] > lib[s[i-1]]:
                total += lib[s[i]] - lib[s[i-1]] - lib[s[i-1]]
            else:
                total += lib[s[i]]
        return total
x = Solution()
print(x.romanToInt('III'))
print(x.romanToInt('LVIII'))
print(x.romanToInt('MCMXCIV'))