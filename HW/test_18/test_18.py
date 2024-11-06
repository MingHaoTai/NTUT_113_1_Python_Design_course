#2024-10-24

def judge(data : list, target : int):
    data_len = len(data)
    two_sum_index = [None]
    for i in range(data_len - 1):
        for j in range(i + 1, data_len):
            if data[i] + data[j] == target:
                if two_sum_index[0] == None:
                    two_sum_index[0] = i
                    two_sum_index.append(j)
                else:
                    two_sum_index.append(i)
                    two_sum_index.append(j)
    return two_sum_index

def answer(data : list):
    data_len = len(data)
    max_value = 0
    max_value_index = [None, None]
    for i in range(0, data_len, 2):
        if data[i] * data[i + 1] > max_value:
            max_value = data[i] * data[i + 1]
            if data[i] > data[i + 1]:
                max_value_index = [data[i], data[i + 1]]
            else:
                max_value_index = [data[i + 1], data[i]]
    print(max_value_index)

def main():
    data = input().split()
    target = int(input())
    for i in range(len(data)):
        data[i] = int(data[i])
    data = judge(data, target)
    answer(data)

if __name__ == '__main__':
    main()