import xml.etree.ElementTree as ElementTree
import sys
import os


def str_tree(element_tree, indent=0):
    root_str = indent * ' ' + str(element_tree.tag) + ' : ' + str(element_tree.text)
    return '\n'.join([root_str] + [str_tree(c, indent + 2) for c in element_tree])


'''
def find_text(element_tree, text, path=[]):


    if isinstance(element_tree, int):
        return path

    else:
        for x in range(len(element_tree)):
            path.append(x)
            find_text(x, text, path)
'''

if __name__ == '__main__':

    SBML_DIR = 'subset' if len(sys.argv) < 2 else sys.argv[1]
    FILE_PATHS = [SBML_DIR + '/' + x for x in os.listdir(SBML_DIR)]

    path = FILE_PATHS[1]
    ET = ElementTree.parse(path).getroot()



    model = ET[0]

    list_of_species = model[-2]

    for s in list_of_species:
        print(s.tag)
