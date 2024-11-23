import random

def generate_permutations(current, length, results):
    if len(current) == length:
        results.append(current)
        return
    
    for digit in [str(i) for i in range(10)]:
        if digit not in current:
            generate_permutations(current + digit, length, results)

def feedback(guess, answer):
    a, b = 0, 0
    for i in range(4):
        if guess[i] == answer[i]:
            a += 1
        if guess[i] in answer:
            b += 1
    b -= a
    return a, b

def filter_possibilities(possibilities, guess, A, B):
    filtered = []
    for possibility in possibilities:
        result_A, result_B = feedback(guess, possibility)
        if result_A == A and result_B == B:
            filtered.append(possibility)
    return filtered

def generate_answer(length):
    elements = [str(i) for i in range(10)]
    answer = []
    for i in range(length):
        answer.append(elements.pop(random.randint(0, len(elements)-1)))

    return ''.join(answer)

if __name__ == "__main__":
    answer = generate_answer(4)
    print("answer:", answer)
    length, times = 4, 0
    all_permutations = []

    generate_permutations("", length, all_permutations)

    while True:
        times += 1
        if times == 1:
            guess = "1234"
        else:
            guess = remaining_possibilities[random.randint(0, len(remaining_possibilities)-1)]

        print("Guess", times, ":", guess)
        A, B = feedback(guess, answer)
        if A == 4:
            print("times:", times)
            break

        if times == 1:
            remaining_possibilities = filter_possibilities(all_permutations, guess, A, B)
        else:
            remaining_possibilities = filter_possibilities(remaining_possibilities, guess, A, B)