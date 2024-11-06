#2024-10-12
def judge(data : list):
    prime_num = [0]
    data_len = len(data)
    for i in range(data_len):
        count = 0
        for j in range(1, data[i] + 1):
            if data[i] % j == 0:
                count = count + 1
            if count > 2:
                break
        if count == 2:
            if prime_num == [0]:
                prime_num[0] = data[i]
            else:
                prime_num.append(data[i])
    if prime_num == [0]:
        print('No prime number')
    else:
        print(sorted(prime_num))

def main():
    data = list(int(i) for i in input().split())
    judge(data)

if __name__ == '__main__':
    main()