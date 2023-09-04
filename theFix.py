from lxml import etree
import cv2


#read in file
path = r"C:\Users\theso\CSCI435\CSCI435-Project1\Programming-Assignment-Data\com.dropbox.android"

with open(path + ".xml", "rb") as f:
    file = f.read()

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


print(bounds)


img = cv2.imread(path + ".png")


for item in bounds:
    minX = min(int(item[2]), int(item[3]))
    maxX = max(int(item[2]), int(item[3]))
    minY = min(int(item[0]), int(item[1]))
    maxY = max(int(item[0]), int(item[1]))

    cv2.rectangle(img, (int(item[0]), int(item[1])), (int(item[2]), int(item[3])), (0, 255, 255), 5)

	
cv2.imshow('image', img)

cv2.imwrite(path + "WithBorders.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()





