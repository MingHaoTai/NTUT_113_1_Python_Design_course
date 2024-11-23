# 2024-11-23
import random

def generatePermutation(current : str, results : list):
    if len(current) == 4:
        results.append(current)
        return
    for i in [str(i) for i in range(10)]:
        if i not in current:
            generatePermutation(current + i, results)

def feedback(guess : str, answer : str):
    a, b = 0, 0
    for i in range(4):
        if guess[i] == answer[i]:
            a += 1
        elif guess[i] in answer:
            b += 1
    return a, b

def filterPossibilities(possibilities : list, guess : str, A : int, B : int):
    filterData = []
    for i in possibilities:
        feedback_A, feedback_B = feedback(i, guess)
        if feedback_A == A and feedback_B == B:
            filterData.append(i)
    return filterData

if __name__ == '__main__':
    count = 0
    all_permutations = []
    A, B = 0, 0
    generatePermutation('', all_permutations)
    while True:
        count += 1
        if count == 1:
            guess = '0123'
        else:
            guess = remainingPossibility[random.randint(0, len(remainingPossibility) - 1)]

        print(f'{count} guess: {guess}')
        result = input()
        A = int(result[0])
        B = int(result[2])
        if A == 4:
            print(f'answer: {guess}')
            break

        if count == 1:
            remainingPossibility = filterPossibilities(all_permutations, guess, A, B)
        else:
            remainingPossibility = filterPossibilities(remainingPossibility, guess, A, B)