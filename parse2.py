import xml.etree.ElementTree as ElementTree
import sys
import os

SBML_DIR = 'subset' if len(sys.argv) < 2 else sys.argv[1]
FILE_PATHS = [SBML_DIR + '/' + x for x in os.listdir(SBML_DIR)]


class Tree:

    def __init__(self, ElementTreeObj):
        self.root = ElementTreeObj
        self.children = []
        self.make_children()


    def __str__(self, indent=2):

       root_txt = self.root.text
       root_str = indent * ' ' + str(self.root.tag) + " : " + str(root_txt)

       return '\n'.join([root_str] + [c.__str__(indent + 3) for c in self.children]) 

    def make_children(self):
        self.children = [Tree(x) for x in self.root]
        for x in self.children:
            x.make_children()

if __name__ == '__main__':
    path = FILE_PATHS[0]
    tree = (ElementTree.parse(path).getroot())

    A = Tree(tree)
    print(A)

