# 2024-12-15
def findGene(start : str, end : list, gene : str):
    index = 0
    i = 0
    getGene = []
    while i < len(gene):
        if gene[index : index + 4] == start:
            i += 3
            index = i + 1
        elif gene[i : i + 3] in end:
            getGene.append(gene[index : i])
            i += 2
            index = i + 1
        i += 1
    return getGene

def primeNum(num : int):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def mySort(data : list):
    data.sort(key = lambda i : len(i), reverse=False)
    length = 0
    sortData = []
    j = -1
    for i in range(len(data)):
        if len(data[i]) > length:
            length = len(data[i])
            sortData.append([])
            j += 1
        if primeNum(len(data[i])) == True: 
            sortData[j].append(data[i])          
        else:
            return []
    for i in range(len(sortData)):
        sortData[i].sort()
    return sortData

def output(data : list):
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j])

if __name__ == '__main__':
    start = input()
    end = input().split()
    gene = input()
    data = findGene(start, end, gene)
    data = mySort(data)
    if data == []:
        print('No gene')
    else:
        output(data)