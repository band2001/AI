'''
Ben Anderson
CSCI 379 Homework 1
Question 2 - Greedy BFS Implementation
'''

'''
File Structure:
    1. Define Goal, Create Tree Data Structure and Graph, and implement Priority Queue structure
    2. Implement Greedy BFS
    3. Written Responses
'''

'''
GENERAL DATA STRUCTURES
'''

# create tree data structure

class TreeNode:
    def __init__(self, data, name):
        self.data = data # the data (in this case number) at the node
        self.name = name # name to be printed for solution path
        self.leftChild = None # the left child (if exists); if there is no left child it is 0
        self.rightChild = None # the right child (if exists); if there is no right child it is 0
        self.parent = None # parent node; if it is the root it is 0
        self.total = 0 # the total sum of the nodes on the path up to and including this node
    
    def setTreeStructure(self, lc, rc, p): # function to assign children and parents to nodes (leftchild, rightchild, parent)
        self.leftChild = lc # assigns the left child
        self.rightChild = rc # assigns the right child
        self.parent = p # assigns the parent
    
    def getData(self): # returns the data associated with a node
        return self.data

    def getName(self): # returns the name of the root (used when printing the solution)
        return self.getName

# create graph - nodes

root = TreeNode(15, "Initial State")

_01 = TreeNode(14, "1 - Down")
_02 = TreeNode(13, "2")
_03 = TreeNode(12, "3")
_04 = TreeNode(11, "4")
_05 = TreeNode(10, "5")
_06 = TreeNode(9, "6")
_07 = TreeNode(8, "7")
_08 = TreeNode(7, "8")
_09 = TreeNode(6, "9")
_10 = TreeNode(5, "10")
_11 = TreeNode(6, "11")
_12 = TreeNode(7, "12")
_13 = TreeNode(8, "13")
_14 = TreeNode(9, "14")
_15 = TreeNode(10, "15")
_16 = TreeNode(11, "16")
_17 = TreeNode(10, "17")
_18 = TreeNode(9, "18")
_19 = TreeNode(8, "19")
_20 = TreeNode(7, "20")
_21 = TreeNode(6, "21")

_22 = TreeNode(14, "22 - Left")
_23 = TreeNode(13, "23")
_24 = TreeNode(12, "24")
_25 = TreeNode(11, "25")
_26 = TreeNode(10, "26")
_27 = TreeNode(9, "27")
_28 = TreeNode(8, "28")
_29 = TreeNode(7, "29")
_30 = TreeNode(6, "30")
_31 = TreeNode(5, "31")
_32 = TreeNode(4, "32")
_33 = TreeNode(3, "33")
_34 = TreeNode(4, "34")

_35 = TreeNode(5, "35 - Paths Unite")
_36 = TreeNode(4, "36")
_37 = TreeNode(3, "37")
_38 = TreeNode(2, "38")
_39 = TreeNode(1, "39")
_40 = TreeNode(0, "GOAL")

# paths

root.setTreeStructure(_01, _22, 0)

_01.setTreeStructure(_02, 0, root)
_02.setTreeStructure(_03,0,_01)
_03.setTreeStructure(_04,0,_02)
_04.setTreeStructure(_05,0,_03)
_05.setTreeStructure(_06,0,_04)
_06.setTreeStructure(_07,0,_05)
_07.setTreeStructure(_08,0,_06)
_08.setTreeStructure(_09,0,_07)
_09.setTreeStructure(_10,0,_08)
_10.setTreeStructure(_11,0,_09)
_11.setTreeStructure(_12,0,_10)
_12.setTreeStructure(_13,0,_11)
_13.setTreeStructure(_14,0,_12)
_14.setTreeStructure(_15,0,_13)
_15.setTreeStructure(_16,0,_14)
_16.setTreeStructure(_17,0,_15)
_17.setTreeStructure(_18,0,_16)
_18.setTreeStructure(_19,0,_17)
_19.setTreeStructure(_20,0,_18)
_20.setTreeStructure(_21,0,_19)
_21.setTreeStructure(_35,0,_20)

_22.setTreeStructure(_23, 0, root)
_23.setTreeStructure(_24,0,_22)
_24.setTreeStructure(_25,0,_23)
_25.setTreeStructure(_26,0,_24)
_26.setTreeStructure(_27,0,_25)
_27.setTreeStructure(_28,0,_26)
_28.setTreeStructure(_29,0,_27)
_29.setTreeStructure(_30,0,_28)
_30.setTreeStructure(_31,0,_29)
_31.setTreeStructure(_32,0,_30)
_32.setTreeStructure(_33,0,_31)
_33.setTreeStructure(_34,0,_32)
_34.setTreeStructure(_35,0,_33)

_35.setTreeStructure(_36,0,_21)
_36.setTreeStructure(_37,0,_35)
_37.setTreeStructure(_38,0,_36)
_38.setTreeStructure(_39,0,_37)
_39.setTreeStructure(_40,0,_38)
_40.setTreeStructure(0,0,_39)


# priority queue

class PriorityQueue:
    def __init__(self):
        self.array = [] # list where elements in priority queue are stored
    
    def inject(self, node):
        self.array.append([node, node.total]) # each element of the priorty queue is [x, y], where x is the node TreeNode structure, and y is its Manhattan Distance
    
    def eject(self): # returns the TreeNode in the priority queue with the smallest Manhattan distance
        if not self.array: # checks if priority queue is empty
            return 0
        
        num = 10000000000000000 # a number that is guarenteed to be larger than any Manhattan distance for this problem
        index = None # index of element to eject (set in the loop below)
        
        for i in range(len(self.array)): # from 0...n
            if int(self.array[i][1]) < num: # if the Manhattan distance is less than num
                num = self.array[i][1] # update num to be the smallest Manhattan distance
                index = i # update the index to match the smallest Manhattan distance
        
        toReturn = self.array[index][0] # TreeNode to return - the one with the smallest Manhattan distance in the priority queue

        self.array.pop(index) # removes the element from the list

        return toReturn # returns the TreeNode

    def get_array(self): # used to access the PriorityQueue list for debugging
        return self.array


'''GREEDY BFS IMPLEMENTATION'''

explored = [] # array storing all explored locations so nodes are not doubly added to the priority queue

def gbfs(root):
    print("GBFS SOLUTION")
    if root.data == 0:
        return 1 # return 1 on success

    root.total = root.data
    
    frontier = PriorityQueue() # creates the frontier as a priority queue
    frontier.inject(root) # injects root into priority queue

    while frontier: # the loop to find the goal state
        current = frontier.eject() # eject from the priority queue (details on what is ejected in comments in priority queue code)
        explored.append(current) # add ejected node to explored array

        print(current.name) # prints the name of the node so the user can see the explored squares/paths

        if current.data == 0: # reached goal state?
            return 1 # return 1 on success
        
        if current.leftChild and current.rightChild: # if node has two children, pick one with smaller Manhattan distance at that moment
            current.leftChild.total = current.leftChild.data + 1
            current.rightChild.total = current.rightChild.data + 1
            if current.leftChild.total <= current.rightChild.total:
                frontier.inject(current.leftChild)
            else:
                frontier.inject(current.rightChild) 
        elif current.leftChild and not current.rightChild: # if only a left child exists, inject it
            current.leftChild.total = current.leftChild.data + 1
            frontier.inject(current.leftChild)
        elif current.rightChild and not current.leftChild: # if only a right child exists, inject it
            current.rightChild.total = current.rightChild.data + 1
            frontier.inject(current.rightChild)
        else:
            print("No solution") # print statement for no solution
            return -1 # return case for no solution
    
    print("No solution") # print statement for no solution
    return -1 # return case for no solution


gbfs(root) # calls the GBFS algorithm with _0 as the initial state

''' WRITTEN RESPONSES '''

'''
My GBFS implementation takes the same path as I took manually when I simulated the problem. The key in this situation
is that since it is a greedy algorithm, at the fork, it takes the path down (uses leftChild) because my algorithm
chooses the leftChild first (in an attempt to be random). It follows this path all the way to the goal despite it taking 
longer than if it had taken the path to the left at the fork.
'''