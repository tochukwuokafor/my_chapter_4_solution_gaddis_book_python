again = input('Enter a sentence or a word: ')
total = 0
words_list = []
while again != '':
    words = again.split()
    for word in words:
        words_list.append(word)
        total += len(word)
    again = input('Enter another sentence or another word: ')
average = total / len(words_list)
print('The average length of the words entered is', round(average))