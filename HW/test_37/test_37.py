# 2024-12-22
import math
from decimal import Decimal
def getData():
    amount = int(input())   # course amount
    course = list(None for i in range(amount))  # course data
    courseStu = {}  # every course students data
    for i in range(amount):
        course[i] = input().split()
        courseStu[course[i][0]+course[i][1]] = []
        for j in range(int(course[i][2])):
            courseStu[course[i][0]+course[i][1]].append(input().split())
    searchCourse = input()
    return course, courseStu, searchCourse

def allSort(courseStu : dict, course : list):
    department = []
    admission = []
    courseYear = []
    for i in courseStu:
        for j in range(len(courseStu[i])):
            if courseStu[i][j][0][3:6] not in department:
                department.append(courseStu[i][j][0][3:6])
            if courseStu[i][j][0][0:3] not in admission:
                admission.append(courseStu[i][j][0][0:3])
    for i in range(len(course)):
        if course[i][1][0:3] not in courseYear:
            courseYear.append(course[i][1][0:3])
    return department, admission, courseYear

def outputPart1(course : list, courseStu : dict, department : str, admission : str, courseYear : str):
    findCourse = []
    for i in range(len(course)):
        if courseYear == course[i][1][0:3] and course[i][0] not in findCourse:
            findCourse.append(course[i][0])
    legal = {}
    for i in courseStu:
        if i[0:4] in findCourse and i[4:7] == courseYear:
            legal[i] = []
            for j in range(len(courseStu[i])):
                if courseStu[i][j][0][3:6] == department and courseStu[i][j][0][0:3] == admission:
                    legal[i].append(courseStu[i][j])
    print(department, admission, courseYear)
    topThree = findTopThree(legal)
    wPercent = withdrawPercentStu(legal)
    nPercent = noPercentStu(legal, True)
    for i in range(3):
        print(f'{topThree[i][0]} {topThree[i][1]} {round(nPercent[i]*100)}% {wPercent[topThree[i][0]]}%')

def withdrawPercentStu(legal : dict):
    withdraw = {}
    select = {}
    wPercent = {}
    for i in legal:
        for j in range(len(legal[i])):
            if legal[i][j][0] not in withdraw and legal[i][j][0] not in select:
                withdraw[legal[i][j][0]] = 0
                select[legal[i][j][0]] = 0
            
            if legal[i][j][1] == 'w':
                withdraw[legal[i][j][0]] += 1
            select[legal[i][j][0]] += 1
    for i in select:
        wPercent[i] = math.ceil((withdraw[i]/select[i])*100)
    return wPercent

def noPercentStu(legal : dict, flag :bool):
    nPercent = [0, 0, 0]
    count = 0
    for i in legal:
        if len(legal[i]) > count:
            count = len(legal[i])
    x = Decimal('0.01')
    i = 0
    while x < 1:
        if i == 3:
            break
        if math.ceil(count*x) - math.ceil(count*(x-Decimal('0.01'))) == 1:
            if (count * (x//Decimal('0.01'))*Decimal('0.01')) % 1 == 0 and x != Decimal('0.01') and flag == True:
                x += Decimal('0.01')
            nPercent[i] = x
            i += 1
        x += Decimal('0.01')
    return nPercent
    
def findTopThree(legal : dict):
    totalScore = {}
    credit = {}
    for i in legal:
        for j in range(len(legal[i])):
            if legal[i][j][1] == 'w':
                continue
            elif legal[i][j][0] not in totalScore:
                totalScore[legal[i][j][0]] = 0
                credit[legal[i][j][0]] = 0
            if len(legal[i][j]) == 3:
                totalScore[legal[i][j][0]] = totalScore[legal[i][j][0]] + math.ceil(int(legal[i][j][1]) * 0.7 + int(legal[i][j][2]) * 0.3) * int(i[3])
            else:
                totalScore[legal[i][j][0]] = totalScore[legal[i][j][0]] + int(legal[i][j][1]) * int(i[3])
            credit[legal[i][j][0]] = credit[legal[i][j][0]] + int(i[3])
    scoreList = []
    for i in totalScore:
        scoreList.append([i, int(totalScore[i]/credit[i])])
    scoreList = sorted(scoreList, key=lambda x:x[1], reverse=True)
    return scoreList[0:3]

def outputPart2(courseStu : dict, key : list):
    maxScore, minScore, aveScore = 0, 0, 0
    legal = {}
    for i in key:
        print(f'{i[0:4]} {i[4:7]}')
        maxScore, minScore, aveScore = getMaxMin(courseStu[i])
        withdrawPercent = courseWithdraw(courseStu[i])
        print(f'{maxScore} {aveScore} {minScore} {withdrawPercent}%')
        legal[i] = courseStu[i]
        topThree = findTopThree(legal)
        noP = noPercentStu(legal, False)
        for j in range(3):
            print(f'{topThree[j][0]} {topThree[j][1]} {round(noP[j]*100)}%')
        del legal[i]

def courseWithdraw(courseStu : list):
    withdraw = 0
    for i in range(len(courseStu)):
        if courseStu[i][1] == 'w':
            withdraw += 1
    return int((withdraw / len(courseStu))*100)
        
def getMaxMin(courseStu : list):    # max, min, ave
    maxScore, minScore, aveScore, total = 0, 100, 0, 0
    people = len(courseStu)
    if len(courseStu[0]) == 3:
        for i in range(len(courseStu)):
            if courseStu[i][1] != 'w':
                score = math.ceil(int(courseStu[i][1]) * 0.7 + int(courseStu[i][2]) * 0.3)
                if score > maxScore:
                    maxScore = score
                if score < minScore:
                    minScore = score
                total += score
            else:
                people -= 1
    else:
        for i in range(len(courseStu)):
            if courseStu[i][1] != 'w':
                score = int(courseStu[i][1])
                if score > maxScore:
                    maxScore = score
                if score < minScore:
                    minScore = score
                total += score
            else:
                people -= 1
    aveScore = int(total / people)
    return maxScore, minScore, aveScore

def dictSort(courseStu : dict):
    key = list(courseStu.keys())
    for i in range(len(key)-1):
        for j in range(i+1, len(key)):
            if int(key[i]) > int(key[j]):
                key[i], key[j] = key[j], key[i]
    return key

def findMostDepartment(courseStu : list):
    department = {}
    for i in range(len(courseStu)):
        if courseStu[i][0][3:6] not in department:
            department[courseStu[i][0][3:6]] = 1
        else:
            department[courseStu[i][0][3:6]] += 1
    most = [None, 0]
    for i in department:
        if department[i] > most[1]:
            most = [i, department[i]]
    return most[0]

def outputPart3(courseStu : dict, searchCourse : str):
    legal = {}
    for i in courseStu:
        if i[0:4] == searchCourse:
            legal[i] = courseStu[i]
            topThree = findTopThree(legal)
            most = findMostDepartment(courseStu[i])
            print(f'{topThree[0][0]} {topThree[1][0]} {most}')
            break
    
if __name__ == '__main__':
    course, courseStu, searchCourse = getData()
    department, admission, courseYear = allSort(courseStu, course)
    department.sort()
    admission.sort()
    courseYear.sort()
    for i in department:
        for j in admission:
            for k in courseYear:
                outputPart1(course, courseStu, i, j, k)
    key = dictSort(courseStu)
    outputPart2(courseStu, key)
    outputPart3(courseStu, searchCourse)
    # -----noPercent Bug!!!!!!!!!
    