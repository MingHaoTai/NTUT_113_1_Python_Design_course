def remove(data, bag):
    for i in bag:
        data.remove(i)  
def findBag(data, index, value, bag):
    if index>=len(data) :
        return False
    elif data[index]>value:
        return False
    elif data[index]==value:
        bag.append(data[index])
        return True
    elif findBag(data, index+1, value, bag)==True:
        return True
    elif findBag(data, index+1, value-data[index], bag)==True:
        bag.append(data[index])
        return True
def compute(data, N):
    if sum(data)%N!=0:
        return False
    value = sum(data)//N
    for i in range(N): #迴圈找N次
        bag = []
        if findBag(data, 0, value, bag) ==False:
            return False
        print('bag=', bag, end=', ')
        remove(data, bag)
    return True
print(compute([4, 3, 2, 3, 5, 2, 1], 4))
print(compute([4, 3, 2, 3, 5, 2, 1], 2))
print(compute([1, 2, 3, 5], 2))
print(compute([1, 5, 11, 5], 2))