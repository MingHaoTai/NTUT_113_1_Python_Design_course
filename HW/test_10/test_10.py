#2024-10-11
def total_score(data : list):
    sum = 0
    bonus = 0
    continue_flag = False
    for i in range(0, 6):
        if continue_flag == True:
            continue_flag = False
            continue
        if i % 2 == 0:
            if data[i] == 10:
                continue_flag = True
                if data[i + 2] == 10 and i != 4:
                    bonus = bonus + data[i + 2] + data[i + 4]
                else:
                    bonus = bonus + data[i + 2] + data[i + 3]
        else:
            if data[i - 1] + data[i] == 10:
                bonus = bonus + data[i + 1]

    # if data[4] == 10:
    #     bonus = bonus + data[6] + data[7]
    # elif data[4] + data[5] == 10:
    #     bonus = bonus + data[6]

    for i in range(0, 6):
        sum = sum + data[i]
    sum = sum + bonus
    print(sum)

def input_data():
    continue_flag = False
    data = list(0 for i in range(8))
    for i in range(0, 6):
        if continue_flag == True:
            continue_flag = False
            continue
        else:
            data[i] = int(input())
        if i % 2 == 0:
            if data[i] == 10:
                continue_flag = True

    if data[4] == 10:
        data[6] = int(input())
        data[7] = int(input())
    elif data[4] + data[5] == 10:
        data[6] = int(input())

    return data

def main():
    data = input_data()
    total_score(data)

if __name__ == '__main__':
    main()