# 2024-11-14
def getData():
    data = []
    while True: 
        x = input()
        if x != '-1':
            data.append(x)
        else:
            break
    for i in range(len(data)):
        y = circuit(bin_dec(data[i]))
        print(bin(y)[2:].zfill(4))   

def circuit(x): 
    if x == 0 or x == 1:
        return 0 
    elif x % 2 == 0:
        return 1 + circuit(x / 2)
    else:
        return 1 + circuit((x + 1) / 2)

def bin_dec(s):
    x = 0
    for i in range(len(s)):
        x += int(s[-i-1]) * (2**i)
    return x

if __name__ == '__main__':
    getData()