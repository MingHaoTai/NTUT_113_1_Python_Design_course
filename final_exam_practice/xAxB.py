import random

def possible(s : str, possible_nums : list):
    if len(s) == 5:
        possible_nums.append(s)
    else:
        for x in [str(i) for i in range(10)]:
            if x not in s:
                possible(s+x, possible_nums)

def feedback(guess : str, answer : str):
    A, B = 0, 0
    for i in range(5):
        if guess[i] == answer[i]:
            A += 1
        elif guess[i] in answer:
            B += 1
    return A, B

def generate(guess : str, possible_nums : list, a : int, b : int):
    new_possible_nums = []
    for i in possible_nums:
        f_a, f_b = feedback(guess, i)
        if f_a == a and f_b == b:
            new_possible_nums.append(i)
    return new_possible_nums

if __name__ == '__main__':
    answer = input()
    times = 1
    possible_nums = []
    possible('', possible_nums)
    while True:
        if times == 1:
            guess = '01234'
        else:
            guess = possible_nums[random.randint(0, len(possible_nums)-1)]

        A, B = feedback(guess, answer)
        if A == 5:
            print(guess)
            break
        else:
            possible_nums = generate(guess, possible_nums, A, B)
            times += 1
        if times > 10:
            print('ERROR')
            break
        
