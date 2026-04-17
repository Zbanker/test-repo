nr1 = int(input('Introduceti primul numar: '))
nr2 = int(input('Introduceti al doilea numar: '))

if nr1 > nr2:
    print(f'Primul numar este mai mare decat al doilea numar.')
elif nr1 < nr2:
    print(f'Al doilea numar este mai mare decat primul numar.')
else:
    print(f'Numerele sunt egale.')