# extract instances of target words (arm, difficulty, interest) to training file

# flags to indicate start to write
# arm = False
# difficulty = False
# interest = False

def writeToTrain(words):
	flag = False
	f = None
	for line in open("EnglishLS.train"):
		for wd in words:
			if line.startswith("<lexelt item=\"" + wd + "\">"):
				flag = True
				assert f == None
				f = open("trainInstances/" + wd.split('.')[0] + "_train.instance", "w")

		if flag == True:
			f.write(line)
			#print( line)
				
		if line.startswith("</lexelt>") and flag == True:
			flag = False
			assert f != None 
			f.close()
			f = None
	return

def getAllWords():
        list1 = []
        for line in open("EnglishLS.words"):
                currline = line
                list1.append(currline.split()[0])
        writeToTrain(list1)
	
getAllWords()

