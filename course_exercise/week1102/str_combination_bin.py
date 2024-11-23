# 2024-11-19
# 'a    b   c   d'  
# '0    0   0   0'  0   
# '1    0   0   0'  1
# '1    1   0   0'  2
# 0~15 find whose binary has 2 bits of '1'
def compute(s : str, n : int):
    for i in range(2**len(s)):
        comb = []
        count = i
        for j in range(len(s)):
            if count % 2 == 1:
                comb.append(s[j]) 
            count = count // 2
        if len(comb) == n: 
            print(comb)

compute('abcd', 3)