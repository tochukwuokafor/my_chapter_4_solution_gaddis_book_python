speed = float(input('What is the speed of the vehicle in mph? '))
hours = int(input('How many hours has it traveled? '))
print('Hour\tDistance Traveled')
print('-----------------------')
for hour in range(1, hours + 1):
    distance = speed * hour
    print(hour, '\t', distance, sep = '')