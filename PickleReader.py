import pickle

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

readPickleOutput()
