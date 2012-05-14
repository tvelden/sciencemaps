import pprint, pickle
from xml.dom.minidom import parse
import os
import math
import sys

basemappath = str(sys.argv[1])
orginaldatapath = str(sys.argv[2])

#########################################, 
#### readfile to get the list of CA
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
            
                    #listCA[field.lower()] = listCA[field.lower()] + 1
                    
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

#for key, value in yearsequence_dict.items():
#    print key, ":", value

##########################
yearbyyearSequence_dict = {}
yearbyyear = 1992
#yearbyyear = 1995
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
    #if key == 17:
    if key == 20:
        break;
    while(i < 2):
        fiveyear = value + i
        for eachItem in Year_ArticleIDlist_dict[str(fiveyear)]:
            tempList.append(eachItem)
        i += 1
    #print str(fiveyear)
    yearbyyear[str(fiveyear)] = tempList

########################
totalCount = 0
for yearSequence, year in yearbyyearSequence_dict.items():
    TemplistCA = {}
    ################################## need to fix it
    TemplistCA = listCA.copy()
    IDlist = []
    IDlist = yearbyyear[str(year)]
    for item in IDlist:
        TemplistCA[articleIDandCA[item]] = TemplistCA[articleIDandCA[item]] + 1
        totalCount += 1
        # create a backup of original file

    doc = parse(basemappath)
    nodes = doc.getElementsByTagName('node')

    for key, value in sequenceCA.items():
        index = int(key) -1
        a= nodes[index].getElementsByTagName('attvalues')
        maincard = doc.createElement("attvalue")
        maincard.setAttribute("for", "freq")
#        maincard.setAttribute("value", str(TemplistCA[value]))
        if TemplistCA[value] == 0:
            maincard.setAttribute("value", "0")
        else:
#            logValue = math.log10(TemplistCA[value])
            logValue = math.log(TemplistCA[value], 2)
            maincard.setAttribute("value", str(logValue))
            
        a[0].appendChild(maincard)
            
        # persist changes to new file
    filename = str(str(year) + '.gexf')
    xml_file = open(filename, "w")
    doc.writexml(xml_file, encoding="utf-8")
    xml_file.close()
    print filename + " is done"
print totalCount
