# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
import pprint, pickle
from operator import itemgetter
from xml.dom.minidom import parse
import os
import math
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
	
def getSortedKey(dict):
        print "Dict length: ", len(dict)
        DictKeyCount = {}
        for key, value in data1.items():
                DictKeyCount[key] = len(data1[key])

        s = sorted(DictKeyCount.items(), key=itemgetter(1))
        s.reverse()

        sortedListKey = []
        for a, b in s[0:11]:
                sortedListKey.append(a)

        return sortedListKey

def MakeEachCSVFile(rank, keyValue, listItem, G):
        doc = parse(basemappath)
        sequenceCA = {}
        sequence = 1
        listCA = {}
        
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

        Year_RaoStirling = {}
        year_nodesize = {}
        for yearSequence, year in yearsequence_dict.items():
            IDlist = []
            IDlist = Year_ArticleIDlist_dict[str(year)]
            #print len(Year_ArticleIDlist_dict[str(year)])
            #print len(listItem)
            TemplistCA = {}
            TemplistCA = listCA.copy()
            #totalCount = 0
            for item in IDlist:
                if item in listItem:
                        TemplistCA[articleIDandCA[item]] = TemplistCA[articleIDandCA[item]] + 1
                        #totalCount += 1

            currentNode = 1
            endNode = 224
            #totalFreq = float(totalCount)
            totalDiversity = 0

            totalFreq = 0
            for key, value in TemplistCA.items():
                    totalFreq = totalFreq + value
            #print str(float(totalFreq))
                    
            while(currentNode < endNode):
                    if TemplistCA[sequenceCA[currentNode]] != 0:
                            nextNode = currentNode + 1
                            while(nextNode < endNode):
                                    if TemplistCA[sequenceCA[nextNode]] != 0:
                                            totalDiversity = totalDiversity + ((float(TemplistCA[sequenceCA[currentNode]])/float(totalFreq)) * (float(TemplistCA[sequenceCA[nextNode]])/float(totalFreq)) * getDistance(G, shortestPath(G,currentNode, nextNode)))
                                    nextNode = nextNode + 1            
                    currentNode = currentNode + 1

            #print totalDiversity
            Year_RaoStirling[year] = totalDiversity
            year_nodesize[year] = totalFreq

        filename = str('top' + str(rank) + '.csv')
        colname = str('top' + str(rank))
        nodesizefilename = str('node' + str(rank)+ '.csv')
        nodesizename = str('node' + str(rank))
        with open(filename, 'wb') as f:
                csvWriter = csv.writer(f)
                #csvWriter.writerow(['year', 'value'])
                csvWriter.writerow([colname])
                for key, value in yearsequence_dict.items():
                        temp = list()
                        #temp.append(value)
                        temp.append(Year_RaoStirling[value])
 #                       temp.append(year_nodesize[year])
                        csvWriter.writerow(temp)
                        print value, ':', Year_RaoStirling[value], ':', str(year_nodesize[value])
        print filename, 'is done for', rank

        with open(nodesizefilename, 'wb') as nodeF:
                csvWriter2 = csv.writer(nodeF)
                csvWriter2.writerow([nodesizename])
                for key, value in yearsequence_dict.items():
                        temp2 = list()
                        temp2.append(year_nodesize[value])
                        csvWriter2.writerow(temp2)
        print nodesizefilename, 'is done for', rank
                
basemappath = str(sys.argv[1])
edgepath = str(sys.argv[2])
orginaldatapath = str(sys.argv[3])
pckpath = str(sys.argv[4])

pkl_file = open(pckpath, 'rb')

data1 = pickle.load(pkl_file)
pkl_file.close()
#pprint.pprint(data1)

listKey = getSortedKey(data1)



############################
ArticleDict = {}

CurrentIndex = ''
CurrentID = ''
CurrentCategoryList = list()

inputfilename = orginaldatapath 
readfile(inputfilename)

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
############################
#List8topic = []
count = 1
for key in listKey: 
        #List8topic.append(data1[key])
        MakeEachCSVFile(count, key, data1[key], G)
        count += 1

csvlist = []
 
csvCount = 1
while(csvCount<12):
        csvFile = 'top' + str(csvCount) + '.csv'
        rowName = 'top' + str(csvCount)
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

with open('MajorTopicField2.csv', 'wb') as f:
        csvWriter = csv.writer(f)
        for item in addedList:
                csvWriter.writerow(item)
print 'MajorTopicField2.csv is done'

csvlist2 = []
 
csvCount2 = 1
while(csvCount2<12):
        csvFile2 = 'node' + str(csvCount2) + '.csv'
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

with open('MajorTopicFieldNodeSize2.csv', 'wb') as f:
        csvWriter = csv.writer(f)
        for item in addedList2:
                csvWriter.writerow(item)



                






