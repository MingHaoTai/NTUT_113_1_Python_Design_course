#2024/09/25

def judge(abc):     #判斷是否為三角形
    if (abc[0] + abc[1]) > abc[2] and (abc[1] + abc[2]) > abc[0] and (abc[0] + abc[2]) > abc[1]:
        return 1
    else:
        return 0

def equ_tri(abc):    #判斷是否為正三角形
    if abc[0] == abc[1] and abc[1] == abc[2]:
        return 1
    else:
        return 0

def iso_tri(abc):   #判斷是否為等腰三角形
    if abc[0] == abc[1] or abc[1] == abc[2] or abc[2] == abc[0]:
        return 1
    else:
        return 0

def obt_tri(abc):   #判斷是否為鈍角三角形
    if (abc[2] ** 2) > ((abc[0] ** 2) + (abc[1] ** 2)):
        return 1
    else:
        return 0

def acu_tri(abc):   #判斷是否為銳角三角形
    if (abc[2] ** 2) < ((abc[0] ** 2) + (abc[1] ** 2)):
        return 1
    else:
        return 0

def rig_tri(abc):   #判斷是否為直角三角形
    if (abc[2] ** 2) == ((abc[0] ** 2) + (abc[1] ** 2)):
        return 1
    else:
        return 0

a = int(input())
b = int(input())
c = int(input())
abc = sorted([a, b, c])
if judge(abc) == 0:
    print('Not Triangle')
else:
    if equ_tri(abc) == 1:
        print('Equilateral Triangle')
    if iso_tri(abc) == 1:
        print('Isosceles Triangle')
    if obt_tri(abc) == 1:
        print('Obtuse Triangle')
    if acu_tri(abc) == 1:
        print('Acute Triangle')
    if rig_tri(abc) == 1:
        print('Right Triangle')