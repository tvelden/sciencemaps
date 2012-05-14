
import pprint, pickle
from operator import itemgetter
import operator
import math
from xml.dom.minidom import parse
import os
from priodict import priorityDictionary
import csv
import sys
def Dijkstra(G,start,end=None):
	D = {}	# dictionary of final distances
	P = {}	# dictionary of predecessors
	Q = priorityDictionary()   # est.dist. of non-final vert.
	Q[start] = 0
	
	for v in Q:
		D[v] = Q[v]
		if v == end: break
		
		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					raise ValueError, \
  "Dijkstra: found better path to already-final vertex"
			elif w not in Q or vwLength < Q[w]:
				Q[w] = vwLength
				P[w] = v
	
	return (D,P)
			


def shortestPath(G,start,end):
	"""
	Find a single shortest path from the given start vertex
	to the given end vertex.
	The input has the same conventions as Dijkstra().
	The output is a list of the vertices in order along
	the shortest path.
	"""
	D,P = Dijkstra(G,start,end)
	Path = []
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	return Path


def getDistance(G, Path):
        i = 0
        a = Path
        distance = 0

        while (i < (len(a)-1)):
                firstP = a[i]
                #print 'firstP::',firstP
                secondP = a[i+1]
                #print 'second::', secondP
                distance = distance + G[firstP][secondP]
                #print '::::', distance
                i += 1

        return distance


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
	

def MakeEachAuthorCSVFile(rank, authorName, listItem, G):
        doc = parse(basemappath)
        sequenceCA = {}
        sequence = 1
        listCA = {}
 #       totalCount = 0

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

        Year_RaoStirling = {}
        year_nodesize = {}
        for yearSequence, year in yearsequence_dict.items():
            IDlist = []
            IDlist = Year_ArticleIDlist_dict[str(year)]
            TemplistCA = {}
            TemplistCA = listCA.copy()
            for item in IDlist:
                if item in listItem:
                        TemplistCA[articleIDandCA[item]] = TemplistCA[articleIDandCA[item]] + 1
#                        totalCount += 1

            currentNode = 1
            endNode = 224
 #           totalFreq = float(len(IDlist))
            totalDiversity = 0

            totalFreq = 0
            for key, value in TemplistCA.items():
                    totalFreq = totalFreq + value
                    
            while(currentNode < endNode):
                    if TemplistCA[sequenceCA[currentNode]] != 0:
                            nextNode = currentNode + 1
                            while(nextNode < endNode):
                                    if TemplistCA[sequenceCA[nextNode]] != 0:
                                            totalDiversity = totalDiversity + ((float(TemplistCA[sequenceCA[currentNode]])/totalFreq) * (float(TemplistCA[sequenceCA[nextNode]])/totalFreq) * getDistance(G, shortestPath(G,currentNode, nextNode)))
                                    nextNode = nextNode + 1            
                    currentNode = currentNode + 1

            #print totalDiversity
            Year_RaoStirling[year] = totalDiversity
            year_nodesize[year] = totalFreq/1000.0

        filename = str('author' + str(rank) + '.csv')
        authorName = str('author' + str(rank))
        nodesizefilename = str('authornode' + str(rank)+'.csv')
        nodesizename = str('authornode' + str(rank))
        with open(filename, 'wb') as f:
                csvWriter = csv.writer(f)
                csvWriter.writerow([authorName])
                for key, value in yearsequence_dict.items():
                        temp = list()
                        #temp.append(value)
                        temp.append(Year_RaoStirling[value])
                        csvWriter.writerow(temp)
                        print value, ':', Year_RaoStirling[value]
        print filename, 'is done for', rank

        with open(nodesizefilename, 'wb') as nodeF:
                csvWriter2 = csv.writer(nodeF)
                csvWriter2.writerow([nodesizename])
                for key, value in yearsequence_dict.items():
                        temp2 = list()
                        temp2.append(year_nodesize[value])
                        csvWriter2.writerow(temp2)
        print nodesizefilename, 'is done for', rank

############################
basemappath = str(sys.argv[1])
edgepath = str(sys.argv[2])
orginaldatapath = str(sys.argv[3])

noderolepath = str(sys.argv[4])
authorarticlepath = str(sys.argv[5])

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

###### building edge Graph#######
f = open(edgepath, 'r')
G = {}


while True:
    line = f.readline()
    if len(line)==0:
        break
    else:
        FirstV =int(str(line[0:4]).strip())
        SecondV = int(str(line[5:9]).strip())
        Value = float(str(line[10:]).strip())
        Value = 1 - Value
        if not G.has_key(FirstV):
            G[FirstV]={}
        if not G.has_key(SecondV):
            G[SecondV]={}
        G[FirstV][SecondV]=Value;
        G[SecondV][FirstV]=Value;
              
f.close()


for key, value in authorRank.items():
    authorName = authorRank[key]
    MakeEachAuthorCSVFile(key, authorRank[key], authorCandidates_articles[authorName],G)

############################
csvlist = []
 
csvCount = 1
while(csvCount< 11):
        csvFile = 'author' + str(csvCount) + '.csv'
        rowName = 'author' + str(csvCount)
        with open(csvFile, 'rb') as f:
                reader = csv.reader(f)
                templist = []
                for row in reader:
                        templist.extend(row)
        #print templist
        csvlist.append(templist)
        csvCount = csvCount + 1



addedList = zip(*csvlist)
#print csvlist
print addedList

with open('MajorResearchersField.csv', 'wb') as f:
        csvWriter = csv.writer(f)
        for item in addedList:
                csvWriter.writerow(item)
print 'MajorResearchersField.csv is done'

csvlist2 = []
 
csvCount2 = 1
while(csvCount2<11):
        csvFile2 = 'authornode' + str(csvCount2) + '.csv'
        #rowName = 'top' + str(csvCount)
        with open(csvFile2, 'rb') as f:
                reader = csv.reader(f)
                templist2 = []
                for row in reader:
                        templist2.extend(row)
        #print templist
        csvlist2.append(templist2)
        csvCount2 = csvCount2 + 1



addedList2 = zip(*csvlist2)
#print csvlist
print addedList2

with open('MajorResearchersNodeSize.csv', 'wb') as f:
        csvWriter = csv.writer(f)
        for item in addedList2:
                csvWriter.writerow(item)
