run_times = int(input('Enter the number of times you have run around a racetrack: '))
record = []
for lap in range(run_times):
    print('Enter the lap time for lap #' + str(lap + 1) + ' : ', sep = '', end = '')
    time = float(input())
    record.append(time)
print('The time of your fastest lap is', min(record))
print('The time of your slowest lap is', max(record))
print('Your average lap time is', sum(record) / run_times)