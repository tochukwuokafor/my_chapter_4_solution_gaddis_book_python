RATE = 1.6
print('Year\tLevel risen (millimeters)')
for year in range(1, 26):
    level = RATE * year
    print(year, '\t', '{:5.2f}'.format(level), sep = '')