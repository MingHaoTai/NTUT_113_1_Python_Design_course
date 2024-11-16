def f(data : str):
    if len(data) <= 1:
        return data
    else:
        for i in range(len(data)):
            x = data[i]
            y = data[0:i] + data[i+1:]
            r = x + f(y)
            print(r)
        return r

f('AB')