bilet = int(input('Введите количество билетов:'))
sum = 0

for ticket in range(bilet):
    age = int(input('Введите Ваш возраст:'))
    if age < 18:
        sum += 0
        print('Бесплатно')
    if 18 <= age <= 25:
        sum += 990
        print('Cумма за билет:990')
    if age > 25:
        sum += 1390
        print('Cумма за билет:1390')

if bilet >= 3:
    sum = sum * 0.9
print('Стоимость билетов:', int(sum))