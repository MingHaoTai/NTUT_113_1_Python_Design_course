#2024/09/26

def mod_183(data):
    money = data[0] * 0.08 + data[1] * 0.1393 + data[2] * 0.1349 + data[3] * 1.1278 + data[4] * 1.4803
    if money > 183:
        return money
    else:
        return 183

def mod_383(data):
    money = data[0] * 0.07 + data[1] * 0.1304 + data[2] * 0.1217 + data[3] * 1.1127 + data[4] * 1.2458
    if money > 383:
        return money
    else:
        return 383

def mod_983(data):
    money = data[0] * 0.06 + data[1] * 0.1087 + data[2] * 0.1018 + data[3] * 0.9572 + data[4] * 1.1243
    if money > 983:
        return money
    else:
        return 983

voice_in = int(input())
voice_out = int(input())
tele = int(input())
mes_in = int(input())
mes_out = int(input())
data = [voice_in, voice_out, tele, mes_in, mes_out]

if mod_183(data) < mod_383(data) and mod_183(data) < mod_983(data):
    print(int(mod_183(data)))
    print('183')
elif mod_383(data) < mod_183(data) and mod_383(data) < mod_983(data):
    print(int(mod_383(data)))
    print('383')
elif mod_983(data) < mod_183(data) and mod_983(data) < mod_383(data):
    print(int(mod_983(data)))
    print('983')