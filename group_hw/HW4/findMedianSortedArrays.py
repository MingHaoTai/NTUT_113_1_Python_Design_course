class Solution(object):
    def findMedianSortedArrays(self, num1 : list[int], num2 : list[int]):
        data = num1 + num2
        data.sort()
        length = len(data)
        if length % 2 == 1:
            return float(data[length // 2])
        else:
            return float((data[length // 2 -1]) + float(data[length // 2])) / 2

x = Solution()
print(x.findMedianSortedArrays([1, 3], [2]))
print(x.findMedianSortedArrays([1, 2], [3, 4]))
