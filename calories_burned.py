CALORIES_BURN = 4.2
for minutes in range(10, 35, 5):
    total_calories = minutes * CALORIES_BURN
    print('The number of calories burned after', minutes, 'minutes is', total_calories)