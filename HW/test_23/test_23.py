# 2024-11-15
def getData():
    p1 = input().split()
    p2 = input().split()
    com = input().split()
    round1 = input()    # p1 take card from p2
    round2 = input()    # p2 take card from com
    round3 = input()    # com take card from p1
    p1 = tidy(p1)
    p2 = tidy(p2)
    com = tidy(com) 
    p1 = update(p1, p2, round1)
    p2 = update(p2, com, round2)
    com = update(com, p1, round3)
    if p1 == 'Error' or p2 == 'Error' or com == 'Error':
        print('Error')
        return
    output(p1)
    output(p2)
    output(com)

def update(p1 : list, p2 : list, round_x : str):
    if round_x in p2:
        p2.remove(round_x)
        p1.append(round_x)
        p1 = tidy(p1)
    else:
        return 'Error'
    return p1

def tidy(p : list):
    flag = False
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i][1] == p[j][1]:
                flag = True
                p.remove(p[i])
                p.remove(p[j-1])
                break
        if flag == True: 
            p = tidy(p)
            break
    return p

def output(p : list):
    for i in range(len(p)):
        print(p[i], end=' ')
    print()
    return

if __name__ == '__main__':
    getData()