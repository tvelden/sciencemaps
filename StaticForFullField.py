from xml.dom.minidom import parse
import math
import sys
# Read base map to et the list of CA

sequenceCA = {}
sequence = 1
listCA = {}
articleIDandCA = {}
ID_Year_dict = {}

##################
#collect file paths
basemappath = str(sys.argv[1])
orginaldatapath = str(sys.argv[2])



##################
#get name of CA from basemap

doc = parse(basemappath)
nodes = doc.getElementsByTagName('node')
for item in nodes:
    listName = item.getAttribute('label')
    listName = listName.replace('and', '&')
    sequenceCA[sequence] = str(listName).lower()
    listCA[str(listName).lower()] = 0
    sequence += 1

#for key, value in sequenceCA.items():
#    print key, ':', value
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
                CurrentID = line.partition(" ")[2].strip()
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

#for key, value in yearsequence_dict.items():
#    print key, ":", value
totalCount = 0

for yearSequence, year in yearsequence_dict.items():
    IDlist = []
    IDlist = Year_ArticleIDlist_dict[str(year)]

    for item in IDlist:
        listCA[articleIDandCA[item]] = listCA[articleIDandCA[item]] + 1
        totalCount += 1

    doc = parse(basemappath)
    nodes = doc.getElementsByTagName('node')

    for key, value in sequenceCA.items():
        index = int(key) -1
        a= nodes[index].getElementsByTagName('attvalues')
        maincard = doc.createElement("attvalue")
        maincard.setAttribute("for", "freq")

        if listCA[value] == 0:
            maincard.setAttribute("value", "0")
        else:

            logValue = math.log(listCA[value], 2)
            maincard.setAttribute("value", str(logValue))
            
        a[0].appendChild(maincard)
        # persist changes to new file

    if(year == 2010):
        filename = str('StaticForFull.gexf')
        xml_file = open(filename, "w")
        doc.writexml(xml_file, encoding="utf-8")
        xml_file.close()
        print filename + " is done"
    
print totalCount
