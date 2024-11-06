#2024-10-24
def main():
    data = input().split()
    data_kind = list(None for i in range(5))
    data_flush = list(None for i in range(5))
    card_kind = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_flush = ['S', 'H', 'D', 'C']
    for i in range(5):
        card_len = len(data[i])
        if card_len == 2:
            if data[i][0] not in card_kind or data[i][1] not in card_flush:
                print('Error input')
                return
            else:
                data_kind[i] = card_kind.index(data[i][0]) + 1
                data_flush[i] = data[i][1]
        elif card_len == 3:
            if (data[i][0] + data[i][1]) != '10' or data[i][2] not in card_flush:
                print('Error input')
                return
            else:
                data_kind[i] = card_kind.index(data[i][0] + data[i][1]) + 1
                data_flush[i] = data[i][2]
        else:
            print('Error input')
            return
    for i in range(3):
        for j in range(i + 1, 5):
            if data[i] == data[j]:
                print('Duplicate deal')
                return

    if Straight_flush(data_kind, data_flush) == True:
        print('9')
    elif Four_of_a_kind(data_kind) == True:
        print('8')
    elif Full_house(data_kind) == True:
        print('7')
    elif Flush(data_flush) == True:
        print('6')
    elif Straight(data_kind) == True:
        print('5')
    elif Three_of_a_kind(data_kind) == True:
        print('4')
    elif Two_pairs(data_kind) == True:
        print('3')
    elif one_pair(data_kind) == True:
        print('2')
    else:
        print('1')
    return

def Straight_flush(data_kind : list, data_flush : list):
    data_kind = sorted(data_kind)
    for i in range(5):
        if data_flush[i] != data_flush[0]:
            return False
    if data_kind[4] == 13 and data_kind[0] == 1:
        for i in range(1, 4):
            if data_kind[i - 1] + 1 != data_kind[i] and data_kind[i] + 1 != data_kind[i + 1]:
                return False
    else:
        for i in range(1, 5):
            if data_kind[i - 1] + 1 != data_kind[i]:
                return False
    return True

def Four_of_a_kind(data_kind : list):
    data_kind = sorted(data_kind)
    if data_kind[0] == data_kind[1]:
        for i in range(0, 4):
            if data_kind[0] != data_kind[i]:
                return False
    elif data_kind[1] == data_kind[2]:
        for i in range(1, 5):
            if data_kind[1] != data_kind[i]:
                return False
    else:
        return False
    return True

def Full_house(data_kind :list):
    count = 0
    data_kind = sorted(data_kind)
    for i in range(5):
        if data_kind[0] == data_kind[i]:
            count = count + 1
    if count == 2:
        count = 0
        if data_kind[2] == data_kind[3] and data_kind[2] == data_kind[4]:
            return True
        else:
            return False
    elif count == 3:
        if data_kind[3] == data_kind[4]:
            return True
        else:
            return False
    else:
        return False

def Flush(data_flush : list):
    count = 0
    for i in range(5):
        if data_flush[0] == data_flush[i]:
            count = count + 1
    if count == 5:
        return True
    else:
        return False

def Straight(data_kind : list):
    data_kind = sorted(data_kind)
    if data_kind[4] == 13 and data_kind[0] == 1:
        for i in range(1, 4):
            if data_kind[i - 1] + 1 != data_kind[i] and data_kind[i] != data_kind[i + 1]:
                return False
    else:
        for i in range(1, 5):
            if data_kind[i - 1] + 1 != data_kind[i]:
                return False
    return True

def Three_of_a_kind(data_kind : list):
    data_kind = sorted(data_kind)
    count = 0
    for i in range(3):
        for j in range(i, i + 3):
            if data_kind[i] == data_kind[j]:
                count = count + 1
            if count == 3:
                return True
        count = 0
    return False

def Two_pairs(data_kind : list):
    data_kind = sorted(data_kind)
    count_pairs = 0
    for i in range(4):
        if data_kind[i] == data_kind[i + 1]:
            count_pairs = count_pairs + 1
        if count_pairs == 2:
            return True
    return False

def one_pair(data_kind : list):
    data_kind = sorted(data_kind)
    for i in range(4):
        if data_kind[i] == data_kind[i + 1]:
            return True
    return False

if __name__ == '__main__':
    main()