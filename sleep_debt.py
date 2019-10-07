hours = []
for day in range(1, 8):
    print('Enter the number of hours slept on day #' + str(day) + ' : ', end = '')
    number_hours = float(input())
    hours.append(number_hours)
sleep_debt = 56 - sum(hours)
if sleep_debt == 0:
    print("Wow! You owe no sleep debt; I'm jealous")
elif sleep_debt > 0:
    print('You owe', sleep_debt, 'hours of sleep')