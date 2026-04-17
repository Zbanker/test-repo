age = int(input('Varsta persoanei: '))

while age != 0 and age < 135:
    if 12 <= age < 18:
        print('Adolescent')
    elif age >= 18:
        print('Adult')
    else:
        print('Copil')
    break