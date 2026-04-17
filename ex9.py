month = int(input('Introduceti numarul lunii: '))

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]

if month <= 12:
    if month == winter[0] or month == winter[1] or month == winter[2]:
         print('Iarna')
    elif month == spring[0] or month == spring[1] or month == spring[2]:
        print('Primavara')
    elif month == summer[0] or month == summer[1] or month == summer[2]:
        print('Vara, YIPPIE!')
    elif month == fall[0] or month == fall[1] or month == fall[2]:
        print('Toamna')
else:
    print('Nu exista luni mai mari decat 12...')