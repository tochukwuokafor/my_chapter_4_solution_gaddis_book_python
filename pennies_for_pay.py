days = int(input('Enter the number of days: '))
counter = 0
penny = 1
print('Day\tSalary')
print('-----------')
for day in range(1, days + 1):
    print(day, '\t', penny, sep = '')
    counter += penny
    penny *= 2
print('The total pay at the end of the period is', counter / 100, 'dollar')