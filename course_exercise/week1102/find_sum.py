# 2024-11-18
# use LOOP to find sum = N from a num list
def remove(data : list, bag : list):
    for i in bag:
        data.remove(i)

def compute(data : list, n : int):
    for i in range(sum(data) // n):
        bag = [] 
        if findBag(data, 0, n, bag) == False:
            return False
        print('bag=', bag, end=',')
        remove(data, bag)
    return True

def findBag(data : list, index : int, value : int, bag : list):
    if index >= len(data):
        return False
    elif data[index] > value:
        return False
    elif data[index] == value:
        bag.append(data[index])
        return True
    elif findBag(data, index + 1, value, bag) == True:
        return True
    elif findBag(data, index + 1, value - data[index], bag) == True:
        bag.append(data[index])
        return True
    
compute([1, 2, 3, 4, 5], 5)
