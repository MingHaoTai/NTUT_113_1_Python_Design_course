def permutation(s : str, current : str, data : list):
    if len(current) == len(s):
        data.append(current)
        return 
    for i in s:
        if i not in current:
            permutation(s, current+i, data)

def combination(s : str, n : int):
    count = 0
    data = []
    while count < 2 ** len(s):
        count_b = bin(count)[2:]
        count_b = count_b.zfill(len(s))
        current = ''
        if count_b.count('1') == n:
            for i in range(len(s)):
                if count_b[i] == '1':
                    current += s[i]
            data.append(current)
        count += 1
    return data

if __name__ == '__main__':
    s = input()
    n = int(input())
    data = []
    permutation(s, '', data)
    print(data)
    data = combination(s, n)
    data = data[::-1]
    print(data)