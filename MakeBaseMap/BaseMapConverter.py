from xml.dom.minidom import parse

#Read 19 cluster info
seq19 = 1
f = open('19clu.txt')
clu19 = {}
while True:
    line = f.readline()
    if len(line)==0:
        break
    else:
        clu19[seq19] = line.strip()
        seq19 += 1   

f.close()

#Read 6 cluster info

seq6 = 1
f = open('6clu.txt')
clu6 = {}
while True:
    line = f.readline()
    if len(line)==0:
        break
    else:
        clu6[seq6] = line.strip()
        seq6 += 1   

f.close()

#Read 4 cluster info
seq4 = 1
f = open('4clu.txt')
clu4 = {}
while True:
    line = f.readline()
    if len(line)==0:
        break
    else:
        clu4[seq4] = line.strip()
        seq4 += 1   

f.close()


#Read color info from the txt file
colorSeq = 1
f = open('color.txt')
color = {}
while True:
    line = f.readline()
    if len(line)==0:
        break
    else:
        color[colorSeq] = line.strip()
        colorSeq += 1   

f.close()
f = open('list.txt', 'r')
sequenceCA = {}
sequence = 1
listCA = {}
Xposition = {}
Yposition = {}

articleIDandCA = {}
ID_Year_dict = {}

while True:
    line = f.readline()
    if len(line)==0:
        break
    else:
        keys = line.split("\"")
        listName = str(keys[1]).strip()
        positionInfo = str(keys[2]).strip().split(" ")
        x = positionInfo[0].strip()
        y = positionInfo[4].strip()
        #print listName
        ###### make a dictionary key: value = (CA name : # of article)
        sequenceCA[sequence] = str(listName).lower()
        listCA[str(listName).lower()] = 0
        Xposition[str(listName).lower()] = x
        Yposition[str(listName).lower()] = y
        sequence += 1
f.close()

#read position info
f = open('list.txt', 'r')
sequenceCA = {}
sequence = 1
listCA = {}
Xposition = {}
Yposition = {}

articleIDandCA = {}
ID_Year_dict = {}

while True:
    line = f.readline()
    if len(line)==0:
        break
    else:
        keys = line.split("\"")
        listName = str(keys[1]).strip()
        positionInfo = str(keys[2]).strip().split(" ")
        x = positionInfo[0].strip()
        y = positionInfo[4].strip()
        #print listName
        ###### make a dictionary key: value = (CA name : # of article)
        sequenceCA[sequence] = str(listName).lower()
        listCA[str(listName).lower()] = 0
        Xposition[str(listName).lower()] = x
        Yposition[str(listName).lower()] = y
        sequence += 1
f.close()

doc = parse('BaseMap.gexf')
nodes = doc.getElementsByTagName('node')

for key, value in sequenceCA.items():
    index = int(key) -1
    a= nodes[index].getElementsByTagName('attvalues')
    maincard = doc.createElement("attvalue")
    maincard.setAttribute("for", "clusters19")
    newindex = index + 1
    maincard.setAttribute("value", str(clu19[newindex]))
    a[0].appendChild(maincard)

    c= nodes[index].getElementsByTagName('attvalues')
    maincard1 = doc.createElement("attvalue")
    maincard1.setAttribute("for", "clusters6")
    maincard1.setAttribute("value", str(clu6[newindex]))
    c[0].appendChild(maincard1)

    d= nodes[index].getElementsByTagName('attvalues')
    maincard2 = doc.createElement("attvalue")
    maincard2.setAttribute("for", "clusters4")
    maincard2.setAttribute("value", str(clu4[newindex]))
    d[0].appendChild(maincard2)

    e = nodes[index].getElementsByTagName('viz:size')
    e[0].setAttribute("value", str('4.0'))

    f = nodes[index].getElementsByTagName('viz:color')
    colorArray = color[int(clu19[newindex])].split(" ")
    
    f[0].setAttribute("b", str(colorArray[0]))
    f[0].setAttribute("g", str(colorArray[1]))
    f[0].setAttribute("r", str(colorArray[2]))
    
    b = nodes[index].getElementsByTagName('viz:position')
    x = float(Xposition[value]) * 1000
    y = float(Yposition[value]) * 1000 * (-1)
    b[0].setAttribute("x", str(x))
    b[0].setAttribute("y", str(y))

        # persist changes to new file
    filename = str(str('newBase.gexf'))
    xml_file = open(filename, "w")
    doc.writexml(xml_file, encoding="utf-8")
    xml_file.close()

print "DONE"

