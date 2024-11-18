def f(data : str) -> str:
    for i in range(len(data)):
        x = data[i]
        y = data[:i] + data[i+1:]
        print(x+y)
f('ABC')