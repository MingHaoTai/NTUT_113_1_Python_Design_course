# 2024-11-19
# use binary to do recursion
def remove(data : list, bag : list):
    for i in bag:
        data.remove(i)

def findBag(data : list, code : int, value : int):
    N = len(data)
    bag = []
    for i in range(N):
        index = code % 2
        code = code // 2
        if index == 1:
            value -= data[i]
            bag.append(data[i])
    if value != 0: bag = []
    return bag

def compute(data : list, N : int):
    if sum(data) % N != 0:
        return False
    value = sum(data) // N
    for i in range(2 ** len(data)):
        bag = findBag(data, i, value)
        if len(bag) > 0:
            print('bag=', bag, end=',')
            remove(data, bag)
            print(data)
    return True

print(compute([4, 3, 2, 3, 5, 2, 1], 4))