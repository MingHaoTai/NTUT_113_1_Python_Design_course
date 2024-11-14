# 2024-11-14
def getData():
    n = int(input())    # How many people in the country
    m = int(input())    # How many date
    a = int(input())    # How many people sick in First day
    b = float(input())  # How many people inflected by a sick person in sick
    c = int(input())    # How many date will good
    d = float(input())  # Immunization rate
    epidemicAnalyze(n, m, a, b, c, d, 1, [0 for i in range(c)], 0)

def epidemicAnalyze(n, m, a, b, c, d, count, day_new_data, total):
    getGood = 0
    new_sick = 0
    if count <= m:
        if count == 1:
            print('%d %d %d %d' %(count, a, a, getGood))
            day_new_data[0] = a
            total = a
        else:
            new_sick = int((a * (b / c) * (1 - d)) / 1)
            if new_sick + a >= n * (1 - d):
                new_sick = int(n * (1 - d) - a) 
            if count / c > 1:
                getGood = day_new_data[count % c - 1]
                a = a - getGood
            day_new_data[count % c - 1] = new_sick
            d = d + getGood / n
            a = a + new_sick
            total += new_sick
            print('%d %d %d %d' %(count, a, new_sick, getGood))
        count += 1
        epidemicAnalyze(n, m, a, b, c, d, count, day_new_data, total)
    else:
        print(str(int(total)))
        return
# day_new_data = [0 for i in range(7)]    
# epidemicAnalyze(1000, 8, 100, 1.2, 7, 0.7, 1, day_new_data)
if __name__ == '__main__':
    getData()

            
