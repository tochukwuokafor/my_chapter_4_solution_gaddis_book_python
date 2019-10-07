NUMBER_OF_DAYS = 5
total = 0
for day in range(NUMBER_OF_DAYS):
    print('Enter the number of bugs collected on day #' + str(day + 1) + ': ', sep = '', end = '')
    bugs_collected = int(input())
    total += bugs_collected

print('The total number of bugs collected is', total)