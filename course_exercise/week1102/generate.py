# 2024-11-18
# Input a string(ex:0~9), and M, choose 4 char from string to combination
# Output all possible
def chooseNum(num : str, s : str, m : int, data : list):    
    if len(num) == m:
        data.append(num)
    for i in range(len(s)):
        chooseNum(num + s[i], s[i+1:], m, data)
    return data

def combination(s : str):
    if len(s) == 1:
        return s
    data = []
    for i in range(len(s)):
        for j in combination(s[:i] + s[i+1:]):
            data.append(s[i] + j)
    return data

def main():
    data = chooseNum('', input(), int(input()), [])
    all_comb = []
    for i in range(len(data)):
        all_comb.append(combination(data[i])) 
    print(all_comb)

if __name__ == '__main__':
    main()