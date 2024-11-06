#2024-11-01
def main():
    num = int(input())
    data = list(None for i in range(num))
    for i in range(num):
        data[i] = list(map(int, input().split()))
    judge(data)

def judge(data : list):
    data_row = int(len(data))
    data_col = int(len(data[0]))
    count = 0
    j = 0
    for i in range(data_row):
        for j in range(data_col):
            if data[i][j] != 1:
                if i != 0:
                    if data[i - 1][j] == 1:
                        count += 1
                if i != data_row - 1:
                    if data[i + 1][j] == 1:
                        count += 1
                if j != 0:
                    if data[i][j - 1] == 1:
                        count += 1
                if j != data_col - 1:
                    if data[i][j + 1] == 1:
                        count += 1
                if i != 0 and j != 0:
                    if data[i - 1][j - 1] == 1:
                        count += 1
                if i != 0 and j != data_col - 1:
                    if data[i - 1][j + 1] == 1:
                        count += 1
                if i != data_row - 1 and j != 0:
                    if data[i + 1][j - 1] == 1:
                        count += 1
                if i != data_row - 1 and j != data_col - 1:
                    if data[i + 1][j + 1] == 1:
                        count += 1
            else:
                count = 0
            print(str(count), end=' ')
            count = 0
        print()

if __name__ == '__main__':
    main()
