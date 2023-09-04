from lxml import etree
import cv2
import os


#Change path to whichever directory the xml and png files are in
path = r"C:\Users\theso\CSCI435\CSCI435-Project1\Programming-Assignment-Data"



xmlfiles = []
for filename in os.listdir(path):
    if filename.endswith(".xml"):
        xmlfiles.append(filename)


for xmlfile in xmlfiles:
    #print(type(item), item)
    curFile =  path + "\\" + xmlfile

    with open(curFile, "rb") as f:
        file = f.read()

    #setting up xml tree
    root = etree.fromstring(file)

    #finding the bounds of every leaf node
    bounds = []

    for item in root.iter("*"):
        if len(item) == 0:
            #converting string to usable list of points
            addition = item.attrib["bounds"]
            addition = addition.replace("[", "")
            addition = addition.replace("]", ",")
            addition = addition.split(",")
            bounds.append(addition[:-1])


    img = cv2.imread(curFile[:-4] + ".png")


    for item in bounds:
        minX = min(int(item[2]), int(item[3]))
        maxX = max(int(item[2]), int(item[3]))
        minY = min(int(item[0]), int(item[1]))
        maxY = max(int(item[0]), int(item[1]))

        cv2.rectangle(img, (int(item[0]), int(item[1])), (int(item[2]), int(item[3])), (0, 255, 255), 5)

        

    cv2.imwrite(r"C:\Users\theso\CSCI435\CSCI435-Project1\annotatedScreenshots\\" + xmlfile[:-4] + ".png", img)





