#2024-11-09
#week1001
#recursion page7
#Fibonacci sequence

def fibonacci(n : int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input())
    print(fibonacci(n))

main()