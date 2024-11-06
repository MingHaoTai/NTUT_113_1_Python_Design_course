#2024-10-22
def GetNum(data : str):
    data_len = len(data)
    data_num = [None]
    for i in range(data_len):
        if data[i].isdigit() == True:
            if data_num[0] == None:
                data_num[0] = data[i]
            else:
                data_num.append(data[i])
    return data_num

def determine(data : list):
    data_len = len(data)
    data_new = [None]
    flag = True
    if data_len % 2 == 0:
        x = int(data_len / 2)
    else:
        x = int(data_len / 2 + 1)
    for i in range(x):
        if data[i] == data[data_len - 1 - i]:
            if data_new[0] == None:
                data_new[0] = data[i]
            else:
                data_new.append(data[i])
        else:
            flag = False
            break
    if flag == True:
        data_new_len = len(data_new)
        data_new = sorted(data_new)
        for i in range(data_new_len):
            if data_new[i] == data_new[0]:
                continue
            else:
                return data_new
        return [data_new[0]]
    else:
        for i in range(data_len):
            if data[i] in data_new:
                continue
            for j in range(i + 1, data_len):
                if data[i] == data[j]:
                    if data[i] not in data_new:
                        if data_new[0] == None:
                            data_new[0] = data[i]
                        else:
                            data_new.append(data[i])
                        break
        data_new = sorted(data_new)
        data_new_len = len(data_new)
        for i in range(int(data_new_len / 2)):
            temp = data_new[i]
            data_new[i] = data_new[data_new_len - 1 - i]
            data_new[data_new_len - 1 - i] = temp
        return data_new

def main():
    data = input()
    data = GetNum(data)
    data = determine(data)
    data_len = len(data)
    if data[0] == None:
        print('[]')
    else:
        for i in range(data_len):
            data[i] = int(data[i])
        print(data)

main()