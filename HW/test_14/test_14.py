#2024-10-16
def judge(data : list):
    class_count = len(data)
    error_flag = False
    for i in range(class_count - 1):
        data1_len = len(data[i])
        for j in range(i + 1, class_count):
            data2_len = len(data[j])
            for x in range(1, data1_len):
                for y in range(1, data2_len):
                    if data[i][x] == data[j][y]:
                        print(data[i][0] + ',' + data[j][0] + ',' + data[i][x])
                        error_flag = True
    if error_flag == False:
        print('correct')

def InClass():
    error_flag = False
    num = int(input())
    class_data = list(None for i in range(num))
    for i in range(num):
        class_name = input()
        hour = int(input())
        if hour < 0 or hour > 3:
            error_flag = True
        data = list(None for x in range(hour + 1))
        data[0] = class_name
        for j in range(1, hour + 1):
            data[j] = input()
            if int(data[j][0]) < 1 or int(data[j][0]) > 5:
                error_flag = True
            if data[j][1] != 'a' and data[j][1] != 'b' and data[j][1] != 'c' and data[j][1] != '1' and data[j][1] != '2' and data[j][1] != '3' and data[j][1] != '4' and data[j][1] != '5' and data[j][1] != '6' and data[j][1] != '7' and data[j][1] != '8' and data[j][1] != '9' :
                    error_flag = True
        class_data[i] = data

    if error_flag == True:
        print('-1')
    else:
        judge(class_data)

InClass()