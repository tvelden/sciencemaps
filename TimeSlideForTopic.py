import pprint, pickle
from operator import itemgetter
from xml.dom.minidom import parse
import os
import math
import sys

def printDict():
        global ArticleDict
	
        for key,value in ArticleDict.items():
                print(key + '::::::::::::')
                print(len(value))
                print(value.pop())

def readline(line):
	
	global writer
	global ArticleDict
	global CurrentIndex
	global CurrentID
	global CurrentCategoryList
	
	line = line.replace("\n","")
	
	if len(line.partition(" ")[0]) == 2:
		CurrentIndex = line.partition(" ")[0]

		
		
	if(CurrentIndex=='ID'):
		if CurrentCategoryList:
			CurrentCategoryList.remove('')
			ArticleDict[CurrentID]=CurrentCategoryList
			
		CurrentID =line[3:]
		CurrentCategoryList = list()
	
	if(CurrentIndex=='CA'):
		CurrentCategoryList.append(line[3:].lower().strip())



def readfile(filename):
	'''comfirm the file name '''
	inputfile=file(filename)
			
	while True:
		line = inputfile.readline()
		if len(line)==0:
			break
		else:
			readline(line)
			
	inputfile.close()
	
def getSortedKey(dict, field):
        print "Dict length: ", len(dict)
        DictKeyCount = {}
        for key, value in data1.items():
                DictKeyCount[key] = len(data1[key])

        #for key, value in DictKeyCount.items():
        #        print key, ":", value

        #print sorted(DictKeyCount.values())

        s = sorted(DictKeyCount.items(), key=itemgetter(1))
        s.reverse()

        sortedListKey = []
        for a, b in s[0:int(field)]:
                sortedListKey.append(a)

        return sortedListKey

def MakeEachGexfFile(rank, keyValue, listItem):
        doc = parse(basemappath)
        sequenceCA = {}
        sequence = 1
        listCA = {}
        totalCount = 0
        
        articleIDandCA = {}
        ID_Year_dict = {}

        nodes = doc.getElementsByTagName('node')
        for item in nodes:
                listName = item.getAttribute('label')
                listName = listName.replace('and', '&')
                sequenceCA[sequence] = str(listName).lower()
                listCA[str(listName).lower()] = 0
                sequence += 1
                
        ###################
        ####### read in.txt to save the # of article to each CA
        f = open(orginaldatapath, 'r')
        #totalarticle = 0
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            else:
                if len(line.partition(" ")[0]) == 2:
                    CurrentIndex = line.partition(" ")[0]
                    if CurrentIndex == 'ID':
                        #totalarticle += 1
                        CurrentID = line.partition(" ")[2].strip()
                    #print CurrentIndex
                    if CurrentIndex == 'BI':
                        line = line.strip()
                        year = line[-4:]
                        ID_Year_dict[CurrentID] = year
                        
                    if CurrentIndex == 'CA':
                        field = str(line.partition(" ")[2]).strip()
                        if field.lower() in listCA:
                            articleIDandCA[CurrentID] = field.lower()
                            
        f.close()

        ArticleIDList = list()
        Year_ArticleIDlist_dict = {}

        ### key = ID value = year
        for keyID, valueYear in ID_Year_dict.items():
            if not Year_ArticleIDlist_dict.get(valueYear):
                ArticleIDList = list()
                ArticleIDList.append(keyID)
                Year_ArticleIDlist_dict[valueYear] = ArticleIDList
            else:
                ArticleIDList = Year_ArticleIDlist_dict[valueYear]
                ArticleIDList.append(keyID)
                Year_ArticleIDlist_dict[valueYear] = ArticleIDList

        yearsequence_dict={}
        yearStart=1991
        index=1
        while True:
            yearsequence_dict[index]=yearStart
            yearStart +=1
            index+=1
            if yearStart>2010:
                break;
        ############
        ##########################
        yearbyyearSequence_dict = {}
        #yearbyyear = 1995
        yearbyyear = 1992
        index2 = 1
        while True:
            yearbyyearSequence_dict[index2] = yearbyyear
            yearbyyear += 1
            index2 += 1
            if yearbyyear > 2010:
                break;

        yearbyyear = {}
        for key, value in yearsequence_dict.items():
            i = 0
            tempList = []
            if key == 20:
            #if key == 17:
                break;
            while(i < 2):
                fiveyear = value + i
                for eachItem in Year_ArticleIDlist_dict[str(fiveyear)]:
                    tempList.append(eachItem)
                i += 1
            #print str(fiveyear)
            yearbyyear[str(fiveyear)] = tempList



        
        ############
        for yearSequence, year in yearbyyearSequence_dict.items():
            TemplistCA = {}
            TemplistCA = listCA.copy()
            IDlist = []
            IDlist = yearbyyear[str(year)]
            for item in IDlist:
                if item in listItem:
                        TemplistCA[articleIDandCA[item]] = TemplistCA[articleIDandCA[item]] + 1
                        totalCount += 1


        ####make gexf file for each key
            doc = parse(basemappath)
            nodes = doc.getElementsByTagName('node')

            for key, value in sequenceCA.items():
                    index = int(key) -1
                    a= nodes[index].getElementsByTagName('attvalues')
                    maincard = doc.createElement("attvalue")
                    maincard.setAttribute("for", "freq")
                    #maincard.setAttribute("value", str(listCA[value]))
                    if TemplistCA[value] == 0:
                            maincard.setAttribute("value", "0")
                    else:
                            logValue = math.log(TemplistCA[value], 2)
                            maincard.setAttribute("value", str(logValue))

                    a[0].appendChild(maincard)       
            filename = str(str(year)+ 'top' + str(rank) +'.gexf')
            xml_file = open(filename, "w")
            doc.writexml(xml_file, encoding="utf-8")
            xml_file.close()

            #print len(listItem)
            #print 'total: ' + str(totalCount)
            print filename, 'is done for', rank

basemappath = str(sys.argv[1])
orginaldatapath = str(sys.argv[2])
pckpath = str(sys.argv[3])
field = str(sys.argv[4])        
if field != '1' and field != '2':
        print "put 1 for field 1or 2 for field 2"
        sys.exit()


pkl_file = open(pckpath, 'rb')

data1 = pickle.load(pkl_file)
pkl_file.close()
#pprint.pprint(data1)
if field == '1':
        field = 8
elif field == '2':
        field = 11
        
listKey = getSortedKey(data1, field)



############################
ArticleDict = {}

CurrentIndex = ''
CurrentID = ''
CurrentCategoryList = list()

inputfilename = orginaldatapath
readfile(inputfilename)


#for key, value in ArticleDict.items()[0:2]:
#        print ArticleDict[key]        




############################
#List8topic = []
count = 1
for key in listKey: 
        #List8topic.append(data1[key])
        MakeEachGexfFile(count, key, data1[key])
        count += 1


                






