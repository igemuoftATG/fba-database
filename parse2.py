import xml.etree.ElementTree as ElementTree
import sys
import os


class Tree:
    ''' A standard Tree object used to represent an ElementTree '''

    def __init__(self, ElementTreeObj):
        ''' (Tree, ElementTree) -> None
        Instantiates a new Tree object from ElementTree
        '''
        self.root = ElementTreeObj
        self.children = []
        self.make_children()

    def __str__(self, indent=0):
        ''' (Tree, int) -> str
        Return a string representation of Tree
        '''
        root_str = indent * ' ' + str(self.root.tag) + " : " + str(self.root.text)
        return '\n'.join([root_str] + [c.__str__(indent + 2) for c in self.children]) 

    def make_children(self):
        ''' (Tree) -> None
        Populates the current instance of Tree with children derived from
        ElementTree
        '''
        self.children = [Tree(x) for x in self.root]
        for x in self.children:
            x.make_children()

    def find_text(self, txt):
        ''' (Tree, str) -> list of list of int
        Return all paths that leads to where txt can be found in self
        '''
        pass

    def find_attr(self, att):
        ''' (Tree, str) -> list of list of int
        Return all paths that leads to where txt can be found in self
        '''
        pass


    def find_tag(self, tag):
        ''' (Tree, str) -> list of list of int
        Return all paths that leads to where txt can be found in self
        '''
        pass


if __name__ == '__main__':

    SBML_DIR = 'subset' if len(sys.argv) < 2 else sys.argv[1]
    FILE_PATHS = [SBML_DIR + '/' + x for x in os.listdir(SBML_DIR)]

    path = FILE_PATHS[0]
    ET = (ElementTree.parse(path).getroot())

    SampleTree = Tree(ET)
    print(SampleTree)

