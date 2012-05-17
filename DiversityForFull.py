# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002

# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228

import pprint, pickle
from priodict import priorityDictionary
import csv
from xml.dom.minidom import parse
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
basemappath = str(sys.argv[1])
edgepath = str(sys.argv[3])
orginaldatapath = str(sys.argv[2])
whichfield = str(sys.argv[4])
if whichfield != '1' and whichfield != '2':
        print "put 1 for field 1or 2 for field 2"
        sys.exit()
        
#### readfile to get the list of CA
doc = parse(basemappath)
sequenceCA = {}
CAsequence = {}
sequence = 1
listCA = {}

articleIDandCA = {}
ID_Year_dict = {}

nodes = doc.getElementsByTagName('node')
for item in nodes:
        listName = item.getAttribute('label')
        listName = listName.replace('and', '&')
        sequenceCA[sequence] = str(listName).lower()
        CAsequence[str(listName).lower()] = sequence
        listCA[str(listName).lower()] = 0
        sequence += 1

####### read in.txt to save ID-year pair and ID-CA pair dictionaries 
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
for key, value in ID_Year_dict.items():
    if not Year_ArticleIDlist_dict.get(value):
        ArticleIDList = list()
        ArticleIDList.append(key)
        Year_ArticleIDlist_dict[value] = ArticleIDList
    else:
        ArticleIDList = Year_ArticleIDlist_dict[value]
        ArticleIDList.append(key)
        Year_ArticleIDlist_dict[value] = ArticleIDList

yearsequence_dict={}
yearStart=1991
index=1
while True:
    yearsequence_dict[index]=yearStart
    yearStart +=1
    index+=1
    if yearStart>2010:
        break;

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


#for key, value in CAsequence.items():
#   print key, ':', value
############# for each year, calculate Rao-Stirling Diversity
Year_RaoStirling = {}

for yearSequence, year in yearsequence_dict.items():
    IDlist = []
    IDlist = Year_ArticleIDlist_dict[str(year)]
    TemplistCA = {}
    TemplistCA = listCA.copy()

    for item in IDlist:
        TemplistCA[articleIDandCA[item]] = TemplistCA[articleIDandCA[item]] + 1

    print year, 'total::', len(IDlist)
    
    currentNode = 1
    endNode = 224
    totalFreq = float(len(IDlist))
    totalDiversity = 0
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

#csvfile = open('field1diversity.csv', 'wb')
CSVFile = 'field' + whichfield + 'diversity.csv'
with open(CSVFile, 'wb') as f: 
        csvWriter = csv.writer(f)
        csvWriter.writerow(['year', 'value', 'total'])
        for key, value in yearsequence_dict.items():
                temp = list()
                temp.append(value)
                temp.append(Year_RaoStirling[value])
                temp.append(float(len(Year_ArticleIDlist_dict[str(value)])))
                csvWriter.writerow(temp)
                print value, ':', Year_RaoStirling[value], ':', str(float(len(Year_ArticleIDlist_dict[str(value)])/1000.0))

    #for key, value in sequenceCA.items():
#        if TemplistCA[value] != 0:
            
############# with R.py

