# 2024-11-18 
def comb(s : str):
    if len(s) <= 1:
        return s
    data = [] 
    for i in range(len(s)):
        for j in comb(s[:i] + s[i+1:]):
            data.append(s[i] + j)
    return data

print(comb('abc'))