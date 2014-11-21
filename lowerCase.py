wordList = open('words.txt', 'r')
words = open('wordsLower.txt', 'w')
for word in wordList:
	words.write(word.lower())
