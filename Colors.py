
a = input(' Введи первый цвет')
b = input(' веди второй цвет')

if a.lower() == 'red' and b.lower() == 'blue':
    print('purple')
elif a.lower() == 'blue' and b.lower() == 'red':
    print('purple')
elif a.lower() == 'yelow' and b.lower() == 'red':
    print('orange')
elif a.lower() == 'red' and b.lower() == 'yelow':
    print('orange')
elif a.lower() == ('blue') and b.lower() == ('yelow'):
    print('gren')
elif a.lower() == ('yelow') and b.lower() == ('blue'):
    print('gren')
else:
    print('Такие цвета смешивать нельзя, получится грязь')
