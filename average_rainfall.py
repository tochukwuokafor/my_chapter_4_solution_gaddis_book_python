years = int(input('Enter the number of years: '))
count = 0
total = 0
for value in range(1, years + 1):
    for month in range(1, 13):
        print('For year ', value, ', enter the inches of rainfall for month #' + str(month) + ' : ', sep = '', end = '')
        month_value = float(input())
        count += 1
        total += month_value

print('The number of months is', count)
print('The total inches of rainfall is', total)
print('The average rainfall per month for the entire period is', total / count)