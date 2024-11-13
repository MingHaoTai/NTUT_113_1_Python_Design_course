# 2024-11-14
# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
class Solution(object):
    def isValid(self, s : str):
        data = []
        for x in s:
            if x in '([{':
                data.append(x)
            else:
                if data == [] or (x == ')' and data[-1] != '(') or (x == ']' and data[-1] != '[') or (x == '}' and data[-1] != '{'):
                    return False
                else:
                    data.pop()
        return not data # if data == [] => data = False, else => data = True
    
y = Solution()
print(y.isValid('()'))
print(y.isValid('()[]{}'))
print(y.isValid('(['))