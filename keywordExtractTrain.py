import hashmap
import pickle

def writeToTrain(wd):
    fname = wd.split('.')[0]
    f1 = open("trainInstances/"+fname+"_train.instance","r")
    context = False
    dict1=hashmap.new()
    sensids = []
    for line in f1:
        if line.startswith("<answer instance"):
            split_for_sensid = line.split()[2]
            #print(split_for_sensid)
            sid = split_for_sensid[9:-3]
            if sid not in sensids:
                sensids.append(sid)
            continue
        if line.startswith("<context"):
            context = True
            continue
        if line.startswith("</context"):
            context = False
            continue
        if context and (not line.startswith("<instance")) and (not line.startswith("</instance")) and (not line.startswith("<answer")):
            newList = []
            list1 = hashmap.get(dict1,sid)
            splitLine = line.split()
            if list1:
                hashmap.delete(dict1,sid)
                for word in splitLine:
                    #print(word)
                    if word not in list1:
                        list1.append(word.lower())
                hashmap.set(dict1,sid,list1)
            else:
                for word in splitLine:
                    if word not in newList:
                        #print(word)
                        newList.append(word.lower())
                hashmap.set(dict1,sid,newList)
    cleanAndWrite(fname,dict1,sensids)
    #dictFromPickle()
   
def cleanAndWrite(wd,hmap,sensids):
    file = open("pickleOutput/" + wd + "_output.p","wb")
    mainDict = {}
    tempList = []
    for sid in sensids: #outer loop for going through all sense-ids
        dict1={}
        list1 = hashmap.get(hmap,sid)
        for othersid in sensids: #inner for loop 
            if sid==othersid:   #if both sense-ids are same, move forward
                continue
            else:
                l1 = hashmap.get(hmap,othersid)
                hashmap.delete(hmap,othersid)
                if list1:
                    for word in list1:  #check if word from outer loop is in inner
                        dict1[word]=1
                        #print(word)
                        if l1:
                            if word in l1:
                                dict1[word]=dict1[word]+1
                                l1.remove(word)
                    hashmap.set(hmap,othersid,l1)
        dict2 = dict1.copy()
        for key in dict2:
            if dict2[key]>1:
                del dict1[key]
        mainDict[sid] = dict1.keys()
        tempList.append(sid)
        for item in dict1.keys():
            tempList.append(item)
        tempList.append("-")
    #print(mainDict["bank%1:17:02::"])
    #print(mainDict)
    #print(tempList)
    pickle.dump(tempList,file)
    file.close()


def getAllWords():
    """ This method extracts all words from "EnglishLS.words" file"""
    list1 = []
    for line in open("EnglishLS.words"):
        currline = line
        list1.append(currline.split()[0])
    for item in list1:
        writeToTrain(item)
    print("done")
        
def dictFromPickle(wd):
    """This method is used to read the output pickle file and loads it as a dictionary - dict2"""
    f=open("pickleOutput/" + wd + "_output.p","rb")
    fromPickle = pickle.load(f)
    dict2={}
    l2=[]
    for item in fromPickle:
        #print(key)
        if item=="-":
            dict2[l2[0]] = l2[1:len(l2)]
            l2=[]
        else:
            l2.append(item)
    print(dict2.keys())


def readPickleOutput():
    """ This method extracts all words from "EnglishLS.words" file"""
    list1 = []
    for line in open("EnglishLS.words"):
        currline = line
        list1.append(currline.split()[0].split('.')[0])
    for item in list1:
        dictFromPickle(item)
    
    
#getAllWords()  #default start from here
#writeToTrain("add.v")
#dictFromPickle()
readPickleOutput()

