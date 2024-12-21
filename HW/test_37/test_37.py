# 2024-12-20
import math
def getData():
    courseAmount = int(input())
    course = {}
    courseStu = {}
    for i in range(courseAmount):
        course[i] = input().split()
        courseStu[course[i][0]] = []
        for j in range(int(course[i][2])):
            courseStu[course[i][0]].append(input().split())
    searchCourse = input()
    return course, courseStu, searchCourse

def outputFirst(course : dict, courseStu : dict, department : list, admission : list, courseYear : list):
    for i in department:
        for j in admission:
            for k in courseYear:
                topThreeData, noPercent = getTopThree(course, courseStu, i, j, k)
                print(topThreeData)
                # for l in range(len(topThreeData)):
                #     w = withdraw(course, courseStu, k, topThreeData[l][0])
                #     e = elective(course, courseStu, k, topThreeData[l][0])
                #     print(f'{topThreeData[l][0]} {topThreeData[l][1]} {math.ceil(noPercent[l]*100)}% {math.ceil((w/e)*100)}%')

def withdraw(course : dict, courseStu : dict, courseYear : str, stu : str): # count student withdraw the course
    w = 0
    for i in range(len(course)):
        if course[i][1][0:3] == courseYear:
            for j in courseStu:
                for k in range(len(courseStu[j])):
                    if courseStu[j][k][0] == stu and courseStu[j][k][1] == 'w':
                        w += 1
    return w

def elective(course : dict, courseStu : dict, courseYear : str, stu : str): # count student choose the course
    e = 0
    for i in range(len(course)):
        if course[i][1][0:3] == courseYear:
            for j in courseStu:
                for k in range(len(courseStu[j])):
                    if courseStu[j][k][0] == stu:
                        e += 1
    return e
    
def chiEng(Stu : list): 
    stuScore = []
    score = 0
    for i in Stu:
        score = math.ceil(int(i[1])*0.7 + int(i[2])*0.3)
        stuScore.append([i[0], score])
    return stuScore

def getTopThree(course : dict, courseStu : dict, department : str, admission : str, courseYear : str):
    courseScore = {}
    legalStu = []
    studentCount = 0
    for i in range(len(courseStu)):
        if course[i][1][0:3] == courseYear:
            for j in range(len(courseStu[course[i][0]])):
                if courseStu[course[i][0]][j][0][0:6] == admission + department:                   
                    studentCount += 1
                    if courseStu[course[i][0]][j][1] != 'w':
                        legalStu.append(courseStu[course[i][0]][j]) 
            if course[i][0][0:3] == '101' or course[i][0][0:3] == '201':
                courseScore[course[i][0]] = chiEng(legalStu)
            else:
                courseScore[course[i][0]] = legalStu
            courseScore[course[i][0]] = sorted(courseScore[course[i][0]], key=lambda score : int(score[1]))
        legalStu = []
    student = {} 
    credit = {}
    for i in courseScore:   # total scores
        for j in range(len(courseScore[i])):
            if courseScore[i][j][0] not in student:
                student[courseScore[i][j][0]] = int(courseScore[i][j][1]) * int(i[3])
                credit[courseScore[i][j][0]] = int(i[3])
            else:
                student[courseScore[i][j][0]] += int(courseScore[i][j][1]) * int(i[3])
                credit[courseScore[i][j][0]] += int(i[3])
    averageScore = []
    for i in student:   # average scores
        averageScore.append([i, round(student[i]/credit[i])])
    averageScore.sort(key=lambda stu:stu[1], reverse=True)

    noPercent = [0, 0, 0]
    x = 0.01
    i = 0
    # while True:
    #     if noPercent[2] != 0:
    #         break
    #     if math.ceil(studentCount * x) - math.ceil(studentCount * (x-0.01)) >= 1:
    #         noPercent[i] = x
    #         i += 1
    #     x += 0.01
    #     # print(noPercent)
    return averageScore[0:3], noPercent
    # print(courseScore)
    # print(student)
    # print(credit)
    # print(averageScore)

# getTopThree({0:['1011', '1121', '2'], 1:['1111', '1121', '2']},
#             {'1011':[['11159053', '60', '60'], ['11159054', '70', '100']], '1111': [['11159053', '90'], ['11159054', '80']]},
#             '590', '111', '112')

# print(chiEng([['101', '59', '63'], ['102', '68', '72'], ['103', '39', '64']]))

if __name__ == '__main__':
    course, courseStu, searchCourse = getData()
    department = []
    admission = []
    courseYear = []
    for i in range(len(course)):
        for j in range(len(courseStu[course[i][0]])):
            if courseStu[course[i][0]][j][0][3:6] not in department:
                department.append(courseStu[course[i][0]][j][0][3:6])
            if courseStu[course[i][0]][j][0][0:3] not in admission:
                admission.append(courseStu[course[i][0]][j][0][0:3])
        if course[i][1][0:3] not in courseYear:
            courseYear.append(course[i][1][0:3])
    outputFirst(course, courseStu, department, admission, courseYear)
#     print(course)
#     print(courseStu)
    print(department)
    print(admission)
    print(courseYear)