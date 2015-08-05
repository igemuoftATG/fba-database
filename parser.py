import xml.etree.ElementTree as ElementTree 
import sys
import os


SBML_DIR = 'subset' if len(sys.argv) < 2 else sys.argv[1]
FILE_PATHS = [SBML_DIR + '/' + x for x in os.listdir(SBML_DIR)]


class Tree:
    '''
    Standard ADT
    '''

    def __init__(self, data=None):
        ''' (Tree, data) -> None
        Instantiates a standard tree ADT
        '''
        self.data = data
        self.children = []

    def __str__(self, indent=None):
        pass

class ParsedXML:
    '''
    A class representing a XML file as a more traditional tree
    abstracting the more confusing features of xml.etree.ElementTree
    '''

    def __init__(self, path):
        ''' (ParsedXML, str) -> None
        Instantiates a new class of ParsedXML from path
        '''
        self.root = ElementTree.parse(path).getroot()

    def find_attr(self, node, attribute):
        ''' (ParsedXML, str) -> list of list of int
        Return a list of list of int representing all the possible paths that 
        leads to attribute
        '''
        if attribute in node.attrib:
            return [0]

    def find_tag(self,node, tag):
        ''' (ParsedXML, str) -> list of list of int
        Return a list of list of int representing all the possible paths that 
        leads to tag
        '''
        pass

if __name__ == '__main__':
    test = ParsedXML(FILE_PATHS[0])
    print(test.root[0].attrib)
