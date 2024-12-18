# 2024-12-17

def area(a : str):
    idArea = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14,
              'F' : 15, 'G' : 16, 'H' : 17, 'I' : 34, 'J' : 18,
              'K' : 19, 'L' : 20, 'M' : 21, 'N' : 22, 'O' : 35,
              'P' : 23, 'Q' : 24, 'R' : 25, 'S' : 26, 'T' : 27,
              'U' : 28, 'V' : 29, 'W' : 32, 'X' : 30, 'Y' : 31, 'Z' : 33}
    if a not in idArea: 
        return False
    else:
        return str(idArea[a])

def num(s : str):
    mul = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    count = 0
    for i in range(10):
        count += int(s[i]) * mul[i]
    if 10 - (count % 10) == int(s[10]):
        return True
    else:
        if count % 10 == 0 and s[10] == '0':
            return True
        return False

def gender(s : str):
    if s != '1' and s != '2':
        return False
    else:
        return True

def IDCheck(ID : str):
    if area(ID[0]) == False:
        print('Wrong area code')
        return False
    else:
        ID = area(ID[0]) + ID[1:]

    if gender(ID[2]) == False:
        print('Wrong gender code')
        return False

    if num(ID) == False:
        print('Illegal')
        return False 
    
    print('Pass')

def passwordCheck(pa : str):
    score = 0
    for i in range(len(pa)):
        if pa[i].islower() == True:
            score += 1
        elif pa[i].isupper() == True:
            score += 3
        elif pa[i].isdigit() == True:
            score += 2
        else:
            score += 5
    count = 0
    i = 0
    numFlag = False
    while i < len(pa):
        if pa[i].isdigit() == True and numFlag == False:
            numFlag = True
            count += 1
        else:
            numFlag = False
        i += 1
    if count >= 5:
        score += 15
    
    if score >= 30:
        print(score)
    else:
        print(f'{score} Not strong enough')

if __name__ == '__main__':
    ID = input()
    password = input()
    IDCheck(ID)
    passwordCheck(password)