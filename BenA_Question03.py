'''
Ben Anderson
CSCI 379 Homework 1
Question 3
'''

'''
File Structure:
    1. Create Game Tree
    2. Min-Max Implementation
    3. Written responses
'''

''' CREATING THE GAME TREE '''

# defining tree class
class TreeNode:
    def __init__(self, data, name):
        self.data = data # the data (the potential option) at the node; -1 when unknown
        self.leftChild = None # the left child (if exists); if there is no left child it is 0
        self.rightChild = None # the right child (if exists); if there is no right child it is 0
        self.parent = None # parent node; if it is the root it is 0
        self.name = name # name to be used if solution is printed out
    
    def setTreeStructure(self, lc, rc, p): # function to assign children and parents to nodes (leftchild, rightchild, parent)
        self.leftChild = lc # assigns the left child
        self.rightChild = rc # assigns the right child
        self.parent = p # assigns the parent
    
    def getData(self): # returns the data associated with a node
        return self.data

#creating game tree
root = TreeNode(-1, "Root") # initializes a TreeNode with (data, name)

_01 = TreeNode(5, "01")
_02 = TreeNode(-1, "02")

_03 = TreeNode(-1, "03")
_04 = TreeNode(-1, "04")

_05 = TreeNode(1, "05")
_06 = TreeNode(-1, "06")
_07 = TreeNode(5, "07")
_08 = TreeNode(-1, "08")

_09 = TreeNode(4, "09")
_10 = TreeNode(2, "10")
_11 = TreeNode(4, "11")
_12 = TreeNode(3, "12")

root.setTreeStructure(_01,_02,0) # sets the tree structure with (leftChild, rightChild, parent)

_01.setTreeStructure(0,0,root)
_02.setTreeStructure(_03,_04,root)

_03.setTreeStructure(_05, _06, _02)
_04.setTreeStructure(_07,_08,_02)

_05.setTreeStructure(0,0,_03)
_06.setTreeStructure(_09,_10,_03)
_07.setTreeStructure(0,0,_04)
_08.setTreeStructure(_11,_12,_04)

_09.setTreeStructure(0,0,_06)
_10.setTreeStructure(0,0,_06)
_11.setTreeStructure(0,0,_08)
_12.setTreeStructure(0,0,_08)


''' MIN-MAX IMPLEMENTATION '''

def minVal(state): # minVal function (for min player's turn)
    if not state.leftChild and not state.rightChild: # checks to see if leaf, if it is, begins returning
        return state.data
    
    lcData = 1000 # upper bound for lcData/rcData placeholder
    rcData = 1000

    if state.leftChild: # if this node has a leftChild
        lcData = maxVal(state.leftChild) # checks to see what max would pick to determine which min it would pick
    
    if state.rightChild: # if this node has a rightChild
        rcData = maxVal(state.rightChild) # checks to see what max would pick to determine which min it would pick

    if lcData <= rcData: # checks if lcData is smaller than rcData; if so, returns lcData
        state.data = lcData
        return lcData

    else: # checks if rcData is smaller than lcData; if so, returns rcData
        state.data = rcData
        return rcData

def maxVal(state): # maxVal function (for max player's turn)
    if not state.leftChild and not state.rightChild: # checks if leaf node; if so, begins the recursive return process
        return state.data
    
    lcData = -1 # lower placeholder bound for lc/rcData
    rcData = -1

    if state.leftChild: # checks if there is a left child
        lcData = minVal(state.leftChild) # evaluates what min would do on the next turn
    
    if state.rightChild: # checks if there is a right child
        rcData = minVal(state.rightChild) # evaluates what min would do on the next turn

    if lcData >= rcData: # checks to see if lcData is greater than rcData; if so, returns lcData
        state.data = lcData
        return lcData

    else: # checks to see if rcData is greater than lcData; if so, returns rcData
        state.data = rcData
        return rcData


def minMaxSearch(root): # the minmax function
    player = 1 # max player is 1, min player is -1
    
    if player == 1: # if max's turn first, call maxVal
        value = maxVal(root)
    else: # if min's turn first, call minVal
        value = minVal(root)
        
    return value # return the value from the recursive steps

def printSoln(tree_node): # recursive function that will print the path taken from the root to current node, with running total next to name
    if not tree_node.leftChild and not tree_node.rightChild:
        print(tree_node.name + " " + str(tree_node.data))
        return 0

    print(tree_node.name + " " + str(tree_node.data))
    if tree_node.leftChild:
        printSoln(tree_node.leftChild)
    if tree_node.rightChild:
        printSoln(tree_node.rightChild)

    return 0

def main():
    value = minMaxSearch(root)
    print(str(value))
    # printSoln(root) # can be used to check to make sure the correct values were assigned to each node in the tree

if __name__ == "__main__":
    main()


""" WRITTEN ANSWERS """

'''
Alpha beta-pruning would begin by looking at the leaf node with 5 on the second level of the tree. It would determine
that the root must be at least 5: max will choose 5 if the other node is smaller than 5 and the other node if it 
is greater than 5. Then, going down to the fourth level where there is the leaf node with a 1, it would realize that on
the level above it would be at least 1 (since it would be max's turn). Then it would look at the 4 in the fifth level 
on the left and determine that the min value above will be less than or equal to 4. Using that info, it would mean 
max would pick a value that is at least 4. Then it would look at the 5 on the fourth level, and determine the value
above would be at least 5 (since it is max's turn), but then in comparison with the 4 from the left side, the min turn
above is at most 4, and then we know the root will choose five over four if it's max's turn first. So the 2 leaf, and
bottom right triangle of nodes in the tree get pruned.
'''