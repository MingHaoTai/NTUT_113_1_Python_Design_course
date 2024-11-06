#2024-10-12
def TwoSum(data : list):
    data_len = len(data)
    data_sum = list(0 for i in range(data_len - 1))
    for i in range(0, data_len - 1):
        data_sum[i] = int(data[i]) + int(data[i + 1])
    print(data_sum)

def main():
    data = list(input().split())
    TwoSum(data)

if __name__ == '__main__':
    main()