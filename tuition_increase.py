TUITION = 8000
print('Year\tTuition')
for year in range(1, 6):
    increase = 0.03 * TUITION
    TUITION = increase + TUITION
    print(year, '\t', '${:7.2f}'.format(TUITION), sep = '')