# 2024-12-08
def getData():
    n = int(input())
    school = list([] for i in range(n))
    for i in range(n):
        school[i] = input().split()
    m = int(input())
    condition = list([] for i in range(m))
    for i in range(m):
        condition[i] = input().split()
    b = int(input())
    if b == 0:
        for i in range(len(condition)):
            new_condition = sortCondition(condition[i], b)
            b0(school, new_condition)
    else:
        for i in range(len(condition)):
            new_condition = sortCondition(condition[i], b)
            b1(school, new_condition)

def sortCondition(condition : list, b : int):
    new_condition0 = []
    new_condition1 = []
    data = []
    for i in condition:
        if i == '+':
            new_condition0.append(data)
            data = []
        else:
            new_condition1.append(i)
            data.append(i)
    if data != []:
        new_condition0.append(data)
        data = []
    if b == 0:
        return new_condition0
    else:
        return new_condition1

def b0(school : list, condition : list):
    bag = []
    index = 0
    while index < len(school):
        for i in range(len(condition)):
            for j in range(len(condition[i])):
                if condition[i][j] in school[index] and j == len(condition[i])-1:
                    if school[index][0] not in bag:
                        bag.append(school[index][0])
                elif condition[i][j] in school[index]:
                    continue
                else:
                    break
        index += 1
    output(bag)

def b1(school : list, condition : list):
    bag = []
    count = 0
    count_data = []
    for i in range(len(school)):
        for j in school[i][1:]:
            if j in condition:
                count += 1
        count_data.append(count)
        count = 0
    max_count = 0
    for i in range(len(count_data)):
        if count_data[i] > max_count:
            max_count = count_data[i]
    for i in range(len(count_data)):
        if count_data[i] == max_count:
            bag.append(school[i][0])
    output(bag)

def output(data : list):
    for i in data:
        print(i, end=' ')
    print()

getData()