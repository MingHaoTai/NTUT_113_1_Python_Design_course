#2024-10-24

def out_mark(n : int, mark : str):
    for i in range(n):
        print(mark, end='')

def out_num(start : int, end : int, step : int):
    if step > 0:
        for i in range(start, end + 1, step):
            print(i, end='')
    else:
        for i in range(start, end - 1, step):
            print(i, end='')

def fish_right(n : int):
    for i in range(n):
        out_mark(i + 1, '*')
        out_mark(n - i - 1, '_')
        out_mark(n - i - 1, '_')
        out_mark(i*2 + 1, '*')
        out_mark(n - i - 1, '_')
        print()
    for i in range(n - 2, -1, -1):
        out_mark(i + 1, '*')
        out_mark(n - i - 1, '_')
        out_mark(n - i - 1, '_')
        out_mark(i*2 + 1, '*')
        out_mark(n - i - 1, '_')
        print()

def fish_left(n : list):
    for i in range(n):
        out_mark(n - i - 1, '_')
        out_mark(i*2 + 1, '*')
        out_mark(n - i - 1, '_')
        out_mark(n - i - 1, '_')
        out_mark(i + 1, '*')
        print()
    for i in range(n - 2, -1, -1):
        out_mark(n - i - 1, '_')
        out_mark(i*2 + 1, '*')
        out_mark(n - i - 1, '_')
        out_mark(n - i - 1, '_')
        out_mark(i + 1, '*')
        print()

def tri_up(n : int):
    for i in range(n):
        out_mark(n - i - 1, '_')
        out_num(i + 1, 1, -1)
        out_num(2, i + 1, 1)
        out_mark(n - i - 1, '_')
        print()

def tri_down(n : int):
    for i in range(n - 1, -1, -1):
        out_mark(n - i - 1, '_')
        out_num(i + 1, 1, -1)
        out_num(2, i + 1, 1)
        out_mark(n - i - 1, '_')
        print()

def judge(n : int, m : int, c : int):
    if c == 1:
        if m % 2 == 0:
            fish_right(n)
        else:
            fish_left(n)
    elif c == 2:
        if m % 2 == 0:
            tri_down(n)
        else:
            tri_up(n)

def main():
    n = int(input())
    m = int(input())
    c = int(input())
    judge(n, m ,c)

if __name__ == '__main__':
    main()