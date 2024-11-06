#2024-10-16
def nStar(n : int):
    for i in range(n):
        print('*', end='')

def Num(n : int):
    for i in range(1, n + 1, 2):
        print(i, end='')
    for i in range(n - 2, 0, -2):
        print(i, end='')

def main():
    n = int(input())
    if n <= 0:
        print('Error')
    else:
        for i in range(1, n + 1):
            nStar(n - i)
            Num(i * 2 - 1)
            print('')
        for i in range(n - 1, 0, -1):
            nStar(n - i)
            Num(i * 2 - 1)
            print('')

main()