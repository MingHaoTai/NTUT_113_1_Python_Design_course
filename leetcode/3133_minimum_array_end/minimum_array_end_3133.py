#2024-11-09
#two integers of 'n' and 'x'. Construct an array size of 0~n-1
#The result in the array of the bitwise AND operation between all elements of 'nums' is 'x'

def minEnd():
    n = int(input())
    x = int(input())
    nums = GetSum(n, x)
    print(nums[len(nums)-1])

def GetSum(n, x):
    i = x
    j = 0
    nums = []
    bit = []
    x_2 = bin(x)[2:]
    for i in range(len(x_2)):
        if x_2[-i] == '0':
            bit.append(i)
    binary_data = list(0 for i in range(len(bit)))
    for i in range(1, 2**len(bit)+1):
        binary_data = binary_up(binary_data)
    print(nums)
    return nums

def binary_up(data : list):
    length = len(data)
    x = 0
    new_data = []
    for i in range(1, len(data)+1):
        x = x + data[-i] * (2 ** (i-1))
    x += 1
    x_bin = bin(x)[2:]
    for i in range(len(data)):
        new_data.append(int(x_bin[i]))
    return new_data

# minEnd()
# binary_up([1, 0, 1])
GetSum(4, 18)