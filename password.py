import crypt
import itertools
import datetime
import copy
from multiprocessing import Process
def setUpDict():
	hashes = open('shadow.txt')
	global d
	d = {}
	for line in hashes:
		data = line.split(':',2)
		d[data[0]] = [data[1],data[1][:12]]
	hashes.close()

def main():
	setUpDict()	
	#variationCreator()
	#print [list(x) for x in itertools.combinations([], 2)]
	p = Process(target = passwordGuesser, args = ('hits1.txt',))
	q = Process(target = passwordGuesser, args = ('hits2.txt',))
	p.start()
	q.start()
	p.join()
	q.join()
	print "done"

def variationCreator():
	combinedDictList = []
	for i in range(4):
		separateDictList = [list(x) for x in itertools.combinations([{'e':3},{'s':5}, {'l':1},{'t':7}], (i+1))]
		for subList in separateDictList:
			print subList[0]
			tempList = []
			for i in range(1,len(subList)):
				tempList = copy.copy(subList[0])
				tempList.update(subList[i])
			combinedDictList.append(tempList)
	print combinedDictList


def leetSpeakMaker(word, letterDictList):
	s = list(word)
	for i in range(len(s)):
		for letter in letterDictList:
			if s[i] == letter:
				s[i] = str(letterDictList[letter])
	return "".join(s)

# def variationMaker(word, translations):
# 	for 
def passwordGuesser(name):
	hits = open(name, 'w')
	wordList = open('words%i.txt' %(int(name[4])), 'r')
	wordList = wordList.readlines()
	# word = "schiller"
	#variations = []
	#variations.extend([word, leetSpeakMaker(word, {'e':3}), leetSpeakMaker(word, {'s':5}), leetSpeakMaker(word, {'l':1}), leetSpeakMaker(word, {'t':7}), leetSpeakMaker(word, {'e':3, 's':5}), leetSpeakMaker(word, {'e':3, 'l':1}), leetSpeakMaker(word, {'s':5, 'l':1}), leetSpeakMaker(word, {'s':5, 'e':3, 'l':1}), leetSpeakMaker(word, {'t':7, 'e':3, 'l':1}), leetSpeakMaker(word, {'s':5, 't':7, 'l':1}), leetSpeakMaker(word, {'s':5, 'e':3, 't':7}), leetSpeakMaker(word, {'s':5, 'e':3, 'l':1, 't':7})])
	#print variations
	userNumber = 1
	sucess = False
	for user in d:
		n = 0
		print "current user number is:", userNumber
		for word in wordList:
			if d[user][0] == crypt.crypt(word, d[user][1]):
				success = True
				hits.write(word+' '+user+'\n')
			n+=1
			if n%1000 == 0:
				print "Process %i is %f%% done for user"%(int(name[4]),n/float(670)), userNumber, '\n'
		
		userNumber+=1
	print "process %i success:" %(int(name[4])), success
main()