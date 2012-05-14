
import pprint, pickle
from operator import itemgetter
import operator
import math
from xml.dom.minidom import parse
import os
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
	

def MakeEachAuthorGexfFile(rank, authorName, listItem):
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
######################
        f = open(orginaldatapath, 'r')
        
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

        for yearSequence, year in yearsequence_dict.items():
            IDlist = []
            IDlist = Year_ArticleIDlist_dict[str(year)]
            for item in IDlist:
                if item in listItem:
                        listCA[articleIDandCA[item]] = listCA[articleIDandCA[item]] + 1
                        totalCount += 1
            
######################
        
#        for item in listItem:
#                if item in ArticleDict:                        
#                        for ca in ArticleDict[item]:
#                                if ca in listCA:
#                                        listCA[ca] = listCA[ca] + 1

        ####make vec file for each key
            authorNameSep = authorName.split(",")
        #author = authorNameSep[0],"_",authorNameSep[1]
            filename = str('author' +str(rank) +'.gexf')

            doc = parse(basemappath)
            nodes = doc.getElementsByTagName('node')

            for key, value in sequenceCA.items():
                    index = int(key) -1
                    a= nodes[index].getElementsByTagName('attvalues')
                    maincard = doc.createElement("attvalue")
                    maincard.setAttribute("for", "freq")
                    #maincard.setAttribute("value", str(listCA[value]))
                    if listCA[value] == 0:
                            maincard.setAttribute("value", "0")
                    else:
 #                           logValue = math.log10(listCA[value])
                            logValue = math.log(listCA[value], 2)
                            maincard.setAttribute("value", str(logValue))

                    a[0].appendChild(maincard)
            if(year == 2010):
                    xml_file = open(filename, "w")
                    doc.writexml(xml_file, encoding="utf-8")
                    xml_file.close()

#            print len(listItem)
#            print 'total: ' + str(totalCount)
                    print filename, 'is done for', authorName       


############################

basemappath = str(sys.argv[1])
orginaldatapath = str(sys.argv[2])
noderolepath = str(sys.argv[3])
authorarticlepath = str(sys.argv[4])

ArticleDict = {}

CurrentIndex = ''
CurrentID = ''
CurrentCategoryList = list()

inputfilename = orginaldatapath
readfile(inputfilename)


#for key, value in ArticleDict.items()[0:2]:
#        print key,':', value       


#########################
data1 = pickle.load(open(noderolepath,'rb'));
data2 = pickle.load(open(authorarticlepath,'rb'));


# get all authors from authorname-noderrole pck
AuthorsOnBoardDict={}

# for every author find out the dict items in authorname-articleids.pck
for key,value in data1.items():
        AuthorsOnBoardDict[key]= len(data2[key])


# sort author dictionary        
items = AuthorsOnBoardDict.items()
items.sort(key=operator.itemgetter(1),reverse=True)

# get the author candidates(top 10!)
authorCandidates_articles = {}
authorRank={}
i=1;

for key,value in items:
        if i>10:
                break
        authorRank[i]=key;
        authorCandidates_articles[key]=data2[key]
        i=i+1


for key, value in authorRank.items():
    authorName = authorRank[key]
    MakeEachAuthorGexfFile(key, authorRank[key], authorCandidates_articles[authorName])

############################

