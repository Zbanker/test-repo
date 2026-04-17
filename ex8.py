hour = int(input('Introduceti ora dvs: '))

if hour < 24:
    if 6 <= hour <= 9:
        print('Este Dimineata, TREZIREA!')
    elif 10 <= hour <= 12:
        print('Este Amiaza')
    elif 13 <= hour <= 16:
        print('Este Ziua.')
    elif 17 <= hour <= 23:
        print('Este Seara, Noapte Buna!')
    else:
        print('Este Noapte, NANI IMEDIAT!')
else:
    print('Conusti systemul de 24 ore nu-i asa?')


