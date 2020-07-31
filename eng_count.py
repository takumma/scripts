sentences = input()
words = sentences.split(' ')
exclude = 0
for word in words:
    if(word[0] == '{'):
        exclude += 1
print('(' + str(len(words) - exclude) + ' words)')