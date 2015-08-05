import xml.etree.ElementTree as ElementTree #https://docs.python.org/3.4/library/xml.etree.elementtree.html
import os

SBML_DIR = 'subset'
FILE_PATHS = [SBML_DIR + '/' + x for x in os.listdir(SBML_DIR)] #will crash in windows 




'''
tree = ElementTree.parse(FILE_PATHS[0])
root = tree.getroot()


print(root.tag)
print(root.attrib)


for x in root:
    print(x.tag)
    for y in x:
        print(type(y.tag))
'''
