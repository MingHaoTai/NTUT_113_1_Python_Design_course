#2024-10-11
def judge(a : int):
    if a % 2 == 0:
        return 0
    else:
        return 1

def tri(a : int):
    for i in range(1, a + 1):
        for j in range(a - i, 0, -1):
            print('#', end='')
        for x in range(0, 2 * i - 1):
            print('*', end='')
        print('')

def squ(a : int):
    b = a -2
    for i in range(1, a + 1):
        if i % a == 1 or i % a == 0:
            for j in range(0, a):
                print('*', end='')
            print('')
        else:
            print('*', end='')
            for j in range(0, b):
                print('#', end='')
            print('*', end='')
            print('')

def main():
    a = int(input())
    flag = judge(a)
    if flag == 1:
        tri(a)
    else:
        squ(a)

if __name__ == '__main__':
    main()