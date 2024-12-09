# 2024-12-09
def engTest(s : str):
    illegal = ['FUC', 'FUG', 'FUQ', 'FUT', 'GPU', 'KGB', 'KKK', 'KMT', 'DPP', 'PUG', 'PUP', 'CAT', 'ANT', 'APE', 'MAD', 'NUN', 'SEX', 'SLY', 'BAD', 'GAY', 'ASS', 'BUM', 'BRA', 'CRY']
    if len(s) != 3:
        return False
    elif s in illegal:
        return False
    elif 'O' in s:
        return False
    elif 'I' in s:
        return False
    else:
        return True

def numTest(s : str):
    if len(s) != 4:
        return False
    elif '4' in s:
        return False
    else:
        return True

if __name__ == '__main__':
    s = input()
    if engTest(s[0:3]) == True and numTest(s[4:]) == True and s[3] == '-':
        print(f'{s} is Valid license plate number.')
    else:
        print(f'{s} is Invalid license plate number.')