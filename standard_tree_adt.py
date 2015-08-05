# We wrote the height function in class.  Next class, we'll write contains.

# Suggested exercises:
# - revise __str__ so that it prints children with the last child at the top
#   the previous child next, and so on.  If you look at the printed string 
#   sideways, the first child will be on the left, as we expect.
# - revise the height function that we wrote in class so that it is a single
#   return statement.  Hint: use a ternary if.

from csc148_queue import Queue

class Tree:
    ''' Represent a Bare-bones Tree ADT'''

    def __init__(self, value=None, children=None):
        ''' (Tree, object, list) -> NoneType

        Create Tree(self) with content value and 0 or more children.
        '''
        self.value = value
        # Copy children if they are not None.
        self.children = children.copy() if children else []
        # This "functional" form of if is equivalent to:
        #if not children:a
           #self.children = []
        #else:
           #self.children = children.copy()

    def __repr__(self):
        ''' (Tree) -> str

        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        '''
        # Our __repr__ doesn't look recursive, but it is because
 	# the repr function calls __repr__!
        return ('Tree({}, {})'.format(repr(self.value), repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))
       
    def __str__(self, indent=0):
        ''' (Tree, int) -> str

        Produce a user-friendly string representation of Tree (self).

        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
        19
           17
           23
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
        29
           31
           19
              17
              23
        '''
        root_str = indent * ' ' + str(self.value)
        return '\n'.join([root_str] +
                         [c.__str__(indent + 3) for c in self.children])   

    def __eq__(self, other):
        ''' (Tree, object) -> bool

        Return whether this Tree is equivalent to other.


        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        '''
        return (isinstance(other, Tree) and
                self.value == other.value and
                self.children == other.children)

# Module-level functions.  (We are outside the class now.)
# These could be written as methods instead.

#def contains(t, v):
    #''' (Tree, v) -> bool

    #Return whether Tree t contains v.

    #>>> t = Tree(17)
    #>>> contains(t, 17)
    #True
    #>>> t = descendents_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
    #>>> contains(t, 5)
    #True
    #>>> contains(t, 18)
    #False
    #'''
    #pass
    
def height(t):
    ''' (Tree) -> int
    
    Return height of Tree t,

    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> height(tn1)
    3
    '''
    if t.children:
        return max([height(c) for c in t.children]) + 1
    else:
        return 1

def descendents_from_list(t, L, arity):
    ''' (Tree, list, int) -> Tree

    Populate t's descendents from L, filling them
    in in level order, with up to arity children per node.
    Then return t.

    >>> descendents_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    '''
    q = Queue()
    q.enqueue(t)
    L = L.copy()
    while not q.is_empty(): # unlikely to happen
        new_t = q.dequeue()
        for i in range(0,arity):
            if len(L) == 0:
                return t # our work here is done
            else:
                new_t_child = Tree(L.pop(0))
                new_t.children.append(new_t_child)
                q.enqueue(new_t_child)
    return t

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    # Make a tree using this handy function.
    t = descendents_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
    print(str(t))    
    
    # Here's how to make a tree "by hand".  The lines are broken here to show
    # what brackets match with what.
    t = Tree('root', [Tree('left', [Tree(1, [Tree(2), 
                                              Tree(3)]
                                          )
                                     ]
                           ),
                      Tree('right', [Tree(1, [Tree(2), 
                                              Tree(3)]
                                          )
                                     ]
                           )
                      ]
             )
    print(str(t))