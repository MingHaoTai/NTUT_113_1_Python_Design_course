# 2024-11-10
# Longest Common Prefix
# Find the longest common prefix string amongst an array of strings
# ex: ["flower", "flow", "flight"] => "fl", ["dog", "racecar", "car"] => ""

class Solution(object):
    def longestCommonPrefix(self, strs : list[str]) -> str:
        shortest_len = len(strs[0])
        common_prefix = ""
        for i in range(1, len(strs)):
            if len(strs[i]) < shortest_len:
                shortest_len = len(strs[i])
        for i in range(shortest_len):
            for j in range(1, len(strs)):
                if strs[j-1][i] != strs[j][i]:
                    return common_prefix
            common_prefix = common_prefix + strs[0][i]
        return common_prefix

x = Solution()
print(x.longestCommonPrefix(["flower","flow","flight"]))
print(x.longestCommonPrefix(["dog","racecar","car"]))