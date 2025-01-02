def twoMul(num : list, target : int):
    num = sorted(num)
    i, j = 0, len(num) - 1
    while True:
        if num[i] * num[j] > target:
            j -= 1
        elif num[i] * num[j] < target:
            i += 1
        else:
            return [i + 1, j + 1]

print(twoMul(num = map(int, input().split()), target = int(input())))