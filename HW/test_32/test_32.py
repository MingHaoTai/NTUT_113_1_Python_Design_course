# 2024-12-09
def happy(n : int, found : list):
    if n == 1:
        return True
    count = 0
    for i in range(len(str(n))):
        count += int(str(n)[i]) ** 2
    if count in found:
        return False
    else:
        found.append(count)
    return happy(count, found)

def narcissistic(n : int):
    count = 0
    for i in range(len(str(n))):
        count += int(str(n)[i]) ** len(str(n))
    if count == n:
        return True
    else:
        return False

def f(n : int):
    fibonacci = []
    for i in range(n):
        if i == 0 or i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
    return fibonacci[n-1]

def factorial(n : int):
    if n == 0:
        count = 0
    else:
        count = 1
    for i in range(2, n+1):
        count *= i
    return count

if __name__ == '__main__':
    n = int(input())
    if happy(n, []) == True and narcissistic(n) == True:
        print(f'{n} is both a happy number and a narcissistic number.')
        flag = True
    elif happy(n, []) == True:
        print(f'{n} is a happy number.')
        flag = True
    elif narcissistic(n) == True:
        print(f'{n} is a narcissistic number.')
        flag = False
    else:
        print(f'{n} is neither a happy number nor a narcissistic number.')
        flag = False
    a = n
    if flag == True:
        while True:
            count = 0
            for i in range(len(str(a))):
                count += int(str(a)[i])
            if count / 10 < 1:
                break
            a = count
        print(f'F({count}) = {f(count)}')
    else:
        while True:
            count = 0
            for i in range(len(str(a))):
                count += int(str(a)[i])
            if count / 10 < 1:
                break
            a = count
        print(f'{count}! = {factorial(count)}')

    # print(happy(56, []))
    # print(narcissistic(372))
    # print(f(7))