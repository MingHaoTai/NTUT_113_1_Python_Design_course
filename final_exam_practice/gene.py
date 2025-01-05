def getData():
    start = input()
    end = input().split()
    data = input()
    return start, end, data

def findGene(start : str, end : list, data : str):
    i = 0
    gene = []
    while i < len(data)-len(start):
        if data[i:i+len(start)] == start:
            shortest = ['', len(data)]
            for a in end:
                if data.find(a, i+len(start)) < shortest[1] and data.find(a, i+len(start)) != -1:
                    shortest = [a, data.find(a, i+len(start))]
            gene.append(data[i+4:shortest[1]])
        i += 1
    return gene

def determinePrimeNum(num : int):
    count = 1
    for i in range(2, num+1):
        if num % i == 0:
            count += 1
        if count > 2:
            return False    # Not prime num
    if count == 2:
        return True     # Prime num
    else:
        return False    # Not prime num

def delPrimeNums(gene : list):
    for i in gene:
        if determinePrimeNum(len(i)) == False:
            gene.remove(i)

def output(data : list):
    for i in data:
        print(i)

if __name__ == '__main__':
    start, end, data = getData()
    gene = findGene(start, end, data)
    delPrimeNums(gene) 
    if gene == []:
        print('no gene')
    else:
        gene = sorted(gene, key=lambda x : len(x))
        length = 0
        index = 0
        for i in range(len(gene)):
            if len(gene[i]) > length or i == len(gene)-1:
                length = len(gene[i])
                if i == len(gene)-1:
                    gene[index : i+1] = sorted(gene[index : i+1])
                else:
                    gene[index : i] = sorted(gene[index : i])
                index = i
        output(gene)