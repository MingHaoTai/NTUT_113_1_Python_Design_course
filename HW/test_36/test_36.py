# 2024-12-18
def getData():
    prize = input().split()
    amount = int(input())
    bill = list(None for i in range(amount))
    for i in range(amount):
        bill[i] = input().split()
    return prize, bill

def checkFormat(bill : list, date : str):
    legal = list(None for i in range(len(bill)))
    for i in range(len(bill)):
        if len(bill[i][0]) != 8:
            legal[i] = 'format false'
        elif bill[i][2][0:4] != date[0:4] or (bill[i][2][5:7] != date[5:7] and bill[i][2][5:7] != date[8:10]):
            legal[i] = 'date false'
        else:
            legal[i] = 'pass'
    return legal

def checkPrize(bill : list, prize : list, legal : list):
    getPrize = list(None for i in range(len(bill)))
    for i in range(len(bill)):
        if legal[i] == 'pass':
            if bill[i][0] in prize[0:2]:
                if prize.index(bill[i][0]) == 0:
                    getPrize[i] = 'special'
                else:
                    getPrize[i] = 'grand'
            else:
                getPrize[i] = normalPrize(bill[i][0], prize[2:])
        elif legal[i] == 'format false':
            getPrize[i] = 'format false'
        else:
            getPrize[i] = 'date false'
    return getPrize

def normalPrize(billNum : str, prize : list):
    for i in range(8, 2, -1):
        for j in range(3):
            if billNum[8-i:] == prize[j][8-i:]:
                return 9-i
    return 0

def prizeName(num : int):
    name = {1:'1st', 2:'2nd', 3:'3rd', 4:'4th', 5:'5th', 6:'6th'}
    return name[num]

def output(bill : list, getPrize : list):
    normal = {'special':10000000, 'grand':2000000, '1st':200000, '2nd':40000, '3rd':10000, '4th':4000, '5th':1000, '6th':200}
    store = {}
    maxStore = [None, 0]
    maxProfit = [None, None, None, None, 0]
    for i in range(len(bill)):
        if getPrize[i] == 0:
            print(f'{bill[i][0]} did not win anything.')
        elif getPrize[i] == 'format false':
            print(f'{bill[i][0]} has an invalid format.')
        elif getPrize[i] == 'date false':
            print(f'{bill[i][0]} is outside the prize period.')
        else:
            store[bill[i][1]] = store.get(bill[i][1], 0) + 1
            if getPrize[i] == 'special':
                name = 'special'
                print(f'{bill[i][0]} won: Special Prize: 10000000 TWD Profit: {10000000-int(bill[i][3])} TWD')
                profit = 10000000-int(bill[i][3])
            elif getPrize[i] == 'grand':
                name = 'grand'
                print(f'{bill[i][0]} won: Grand Prize: 2000000 TWD Profit: {2000000-int(bill[i][3])} TWD')
                profit = 2000000-int(bill[i][3])
            else:
                name = prizeName(getPrize[i])
                print(f'{bill[i][0]} won: {name} Prize: {normal[name]} TWD Profit: {normal[name]-int(bill[i][3])} TWD')
                profit = normal[name]-int(bill[i][3])

            if store[bill[i][1]] > maxStore[1]:
                maxStore = [bill[i][1], store[bill[i][1]]]

            if profit > maxProfit[4]:
                maxProfit = [bill[i][0], bill[i][1], bill[i][2], normal[name], profit] 
    
    if maxStore[0] == None:
        print('No invoices won any prize.')
    else:
        print(f'Store {maxStore[0]} opened the most winning invoices: {maxStore[1]}')
    
    if maxProfit[0] != None:
        print(f'Invoice with the highest profit: {maxProfit[0]}, from store {maxProfit[1]}, purchase date {maxProfit[2]}, total prize {maxProfit[3]} TWD, profit {maxProfit[4]} TWD')

if __name__ == '__main__':
    prize, bill = getData()
    legal = checkFormat(bill, prize[5])
    getPrize = checkPrize(bill, prize[0:5], legal)
    # print(bill)
    output(bill, getPrize)

# checkFormat([['19586605', '04595257', '2024-09-15', '120'], ['23456934', '04595257', '2024-12-01', '300'], ['900285801', '10458574', '2024-09-22', '100']], '2024-09,10')