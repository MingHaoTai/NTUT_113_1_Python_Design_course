#2024/09/26

def point(data):
    point = 0
    for i in range(0, 3):
        if data[i] == 'A':
            point = point + 1
        elif data[i] == '2':
            point = point + 2
        elif data[i] == '3':
            point = point + 3
        elif data[i] == '4':
            point = point + 4
        elif data[i] == '5':
            point = point + 5
        elif data[i] == '6':
            point = point + 6
        elif data[i] == '7':
            point = point + 7
        elif data[i] == '8':
            point = point + 8
        elif data[i] == '9':
            point = point + 9
        elif data[i] == '10':
            point = point + 10
        else:
            point = point + 0.5
    # for i in range(0, 3):
    #     match data[i]:
    #         case 'A':
    #             point = point + 1
    #         case '2':
    #             point = point + 2
    #         case '3':
    #             point = point + 3
    #         case '4':
    #             point = point + 4
    #         case '5':
    #             point = point + 5
    #         case '6':
    #             point = point + 6
    #         case '7':
    #             point = point + 7
    #         case '8':
    #             point = point + 8
    #         case '9':
    #             point = point + 9
    #         case '10':
    #             point = point + 10
    #         case _:
    #             point = point + 0.5
    if point > 10.5:
        point = 0
    if (point % 1) == 0:
        return int(point)
    else:
        return float(point)

a1 = input()
a2 = input()
a3 = input()
data1 = [a1, a2, a3]
b1 = input()
b2 = input()
b3 = input()
data2 = [b1, b2, b3]

if point(data1) == point(data2):
    print(point(data1))
    print(point(data2))
    print('Tie')
elif point(data1) > point(data2):
    print(point(data1))
    print(point(data2))
    print('X Win')
elif point(data1) < point(data2):
    print(point(data1))
    print(point(data2))
    print('Y Win')