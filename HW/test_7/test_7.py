#2024/09/26

def judge_1_2(data1, data2, flag):
    for i in range(0, 2):
        for j in range(0, 2):
            if data1[i] == data2[j]:
                flag = 1
                if data1[2] < data2[2]:
                    print('%d and %d conflict on %d' %(data1[2], data2[2], data1[i]))
                else:
                    print('%d and %d conflict on %d' %(data2[2], data1[2], data1[i]))
    return flag
def judge_1_3(data1, data3, flag):
    for i in range(0, 2):
        for j in range(0, 2):
            if data1[i] == data3[j]:
                flag = 1
                if data1[2] < data3[2]:
                    print('%d and %d conflict on %d' %(data1[2], data3[2], data1[i]))
                else:
                    print('%d and %d conflict on %d' %(data3[2], data1[2], data1[i]))
    return flag
def judge_2_3(data2, data3, flag):
    for i in range(0, 2):
        for j in range(0, 2):
            if data2[i] == data3[j]:
                flag = 1
                if data2[2] < data3[2]:
                    print('%d and %d conflict on %d' %(data2[2], data3[2], data2[i]))
                else:
                    print('%d and %d conflict on %d' %(data3[2], data2[2], data2[i]))
    return flag

a1 = int(input())               #no
a2 = int(input())               #class
a3 = int(input())               #class
data1 = sorted([a1, a2, a3])    #[class, class, no]
b1 = int(input())
b2 = int(input())
b3 = int(input())
data2 = sorted([b1, b2, b3])
c1 = int(input())
c2 = int(input())
c3 = int(input())
data3 = sorted([c1, c2, c3])

flag = 0
if a1 < b1 and a1 < c1:
    if b1 < c1:
        flag = judge_1_2(data1, data2, flag)
        flag = judge_1_3(data1, data3, flag)
        flag = judge_2_3(data2, data3, flag)
    else:
        flag = judge_1_3(data1, data3, flag)
        flag = judge_1_2(data1, data2, flag)
        flag = judge_2_3(data2, data3, flag)
elif b1 < a1 and b1 < c1:
    if a1 < c1:
        flag = judge_1_2(data1, data2, flag)
        flag = judge_1_3(data1, data3, flag)
        flag = judge_2_3(data2, data3, flag)
    else:
        flag = judge_1_2(data1, data2, flag)
        flag = judge_2_3(data2, data3, flag)
        flag = judge_1_3(data1, data3, flag)
elif c1 < a1 and c1 < b1:
    if a1 < b1:
        flag = judge_1_3(data1, data3, flag)
        flag = judge_1_2(data1, data2, flag)
        flag = judge_2_3(data2, data3, flag)
    else:
        flag = judge_2_3(data2, data3, flag)
        flag = judge_1_3(data1, data3, flag)
        flag = judge_1_2(data1, data2, flag)
if flag == 0:
    print('correct')