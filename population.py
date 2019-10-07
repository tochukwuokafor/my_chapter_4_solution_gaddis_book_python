organism = int(input('Starting number of organisms: '))
percent = float(input('Avergae daily increase: '))
days = int(input('Number of days to multiply: '))
percent /= 100
print('Day Approximate\t\tPopulation')
for day in range(1, days + 1):
    print(day, '\t\t\t', organism)
    organism = (percent * organism) + organism
