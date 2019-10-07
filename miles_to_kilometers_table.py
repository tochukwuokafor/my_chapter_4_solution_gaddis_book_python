print('Miles\tKilometers')
print('-----------------')
for miles in range(10, 90, 10):
    kilometers = miles * 1.60934
    print(miles, '\t', '{:>6.2f}'.format(kilometers), sep = '')
