# 2024-12-01
import random

def possible(num : str, data : list):
    if len(num) == 5:
        data.append(num)
        return
    for x in [str(i) for i in range(10)]:
        if x not in num:
            possible(num + x, data)

def generateNum(guess : str, possible : list, A : int, B : int):
    new_possible = []
    for i in possible:
        f_A, f_B = feedback(guess, i)
        if f_A == A and f_B == B:
            new_possible.append(i)
    return new_possible

def feedback(answer : str, guess : str):
    a, b = 0, 0
    # print(guess)
    for i in range(5):
        if guess[i] == answer[i]:
            a += 1
        elif guess[i] in answer:
            b += 1
    # print(a, b)
    return a, b

if __name__ == '__main__':
    answer = input()
    times = 1
    possibleNum = []
    possible('', possibleNum)
    # print(possibleNum)
    while True:
        if times == 1:
            guess = '01234'
        else:
            guess = possibleNum[random.randint(0, len(possibleNum)-1)]
        A, B = feedback(answer, guess)
        # print(A, B)
        if A == 5:
            print(answer)
            break
        else:
            possibleNum = generateNum(guess, possibleNum, A, B)
            times += 1
        if times >= 10:
            print('Error')
            break
