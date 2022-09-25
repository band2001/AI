'''
Ben Anderson
CSCI 379 Homework 1
Question 2 - A* Implementation
'''

'''
File Structure:
    1. Define Goal, Create Tree Data Structure and Graph, and implement Priority Queue structure
    2. Implement A*
    3. Written Responses
'''

'''
GENERAL DATA STRUCTURES
'''


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

_0 = TreeNode([15,0], "Initial State") # the data [x,y] is used as the heuristic: x is distance from goal, y is distance from initial state
_1 = TreeNode([14,1], "1")
_2 = TreeNode([13,2], "2")
_3 = TreeNode([12,3], "3")
_4 = TreeNode([11,4], "4")
_5 = TreeNode([10,5], "5")
_6 = TreeNode([11,6], "6 - Branch Left at Fork") # path branching left to goal state
_7 = TreeNode([12,7], "7")
_8 = TreeNode([11,8], "8")
_9 = TreeNode([10,9], "9")
_10 = TreeNode([9,10], "10")
_11 = TreeNode([8,11], "11")
_12 = TreeNode([7,12], "12")
_13 = TreeNode([6,13], "13")
_14 = TreeNode([5,14], "14")
_15 = TreeNode([4,15], "15")
_16 = TreeNode([3,16], "16")
_17 = TreeNode([2,17], "17")
_18 = TreeNode([1,18], "18")
_19 = TreeNode([0,19], "GOAL") # goal state
_20 = TreeNode([9,6], "19 - Branch Up at Fork") # path that goes up from branch
_21 = TreeNode([8,7], "20")
_22 = TreeNode([7,8], "21")
_23 = TreeNode([6,9], "22")
_24 = TreeNode([5,10], "23")
_25 = TreeNode([4,11], "24")
_26 = TreeNode([5,12], "25")
_27 = TreeNode([6,13], "26")
_28 = TreeNode([7,14], "27")
_29 = TreeNode([8,15], "28")
_30 = TreeNode([9,16], "29")
_31 = TreeNode([10,17], "30")
_32 = TreeNode([9,18], "31")
_33 = TreeNode([8,19], "32")
_34 = TreeNode([7,20], "33")
_35 = TreeNode([6,21], "34")
_36 = TreeNode([5,22], "35")
_37 = TreeNode([4,23], "36")
_38 = TreeNode([3,24], "37")
_39 = TreeNode([2,25], "38")
_40 = TreeNode([1,26], "39")

# - paths

_0.setTreeStructure(_1,0,0) # (leftChild, rightChild, parent) where leftChild is generally the next spot,
_1.setTreeStructure(_2,0,0)     # parent is previous spot, and rightChild is used if there is a fork.
_2.setTreeStructure(_3,0,_1)
_3.setTreeStructure(_4,0,_2)
_4.setTreeStructure(_5,0,_3)
_5.setTreeStructure(_6,_20,_4)
_6.setTreeStructure(_7,0,_5)
_7.setTreeStructure(_8,0,_6)
_8.setTreeStructure(_9,0,_7)
_9.setTreeStructure(_10,0,_8)
_10.setTreeStructure(_11,0,_9)
_11.setTreeStructure(_12,0,_10)
_12.setTreeStructure(_13,0,_11)
_13.setTreeStructure(_14,0,_12)
_14.setTreeStructure(_15,0,_13)
_15.setTreeStructure(_16,0,_14)
_16.setTreeStructure(_17,0,_15)
_17.setTreeStructure(_18,0,_16)
_18.setTreeStructure(_19, 0, _17)
_19.setTreeStructure(0, 0, _18)
_20.setTreeStructure(_21,0,_5)
_21.setTreeStructure(_22,0,_20)
_22.setTreeStructure(_23,0,_21)
_23.setTreeStructure(_24,0,_22)
_24.setTreeStructure(_25, 0, _23)
_25.setTreeStructure(_26, 0, _24)
_26.setTreeStructure(_27, 0, _25)
_27.setTreeStructure(_28, 0, _26)
_28.setTreeStructure(_29, 0, _27)
_29.setTreeStructure(_30, 0, _28)
_30.setTreeStructure(_31, 0, _29)
_31.setTreeStructure(_32, 0, _30)
_32.setTreeStructure(_33, 0, _31)
_33.setTreeStructure(_34, 0, _32)
_34.setTreeStructure(_35, 0, _33)
_35.setTreeStructure(_36, 0, _34)
_36.setTreeStructure(_37, 0, _35)
_37.setTreeStructure(_38, 0, _36)
_38.setTreeStructure(_39, 0, _37)
_39.setTreeStructure(_40, 0, _38)
_40.setTreeStructure(_19, 0, _39)

# priority queue

class PriorityQueue:
    def __init__(self):
        self.array = [] # list where elements in priority queue are stored
    
    def inject(self, node):
        self.array.append([node, node.data[0]+node.data[1]]) # each element of the priorty queue is [x, y], where x is the node TreeNode structure, and y is its Manhattan Distance
    
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


'''A* IMPLEMENTATION'''

explored = [] # array storing all explored locations so nodes are not doubly added to the priority queue

def a_star(root): # A* Algorithm Function, takes the root (initial state) as an argument
    print("A* SOLUTION")
    if root.data[0] == 0: # Checks if initial state is goal state
        return 1 # return 1 on success
    
    frontier = PriorityQueue() # creates the frontier as a priority queue
    frontier.inject(root) # injects the root into the priority queue

    while frontier: # the loop to find the goal state
        current = frontier.eject() # eject from the priority queue (details on what is ejected in comments in priority queue code)
        explored.append(current) # add ejected node to explored array

        print(current.name) # prints the name of the node so the user can see the explored squares/paths

        if current.data[0] == 0: # reached goal state?
            return 1 # return 1 on success

        inExplored = 0 # bool to check if left child is in the explore array or not
        for i in explored: # checks to see if leftChild has been explored
            if i == current.leftChild:
                inExplored = 1
                break
        if not inExplored and current.leftChild != 0: # if not explored AND exists, inject to queue
            frontier.inject(current.leftChild)

        inExplored = 0 # bool to check if right child is in the explore array or not
        for i in explored: # checks to see if rightChild has been explored
            if i == current.rightChild:
                inExplored = 1
                break
        if not inExplored and current.rightChild != 0: # if not explored AND exists, inject to queue
            frontier.inject(current.rightChild)

    print("No solution") # print statement for no solution
    return -1 # return case for no solution

a_star(_0) # calls the A* algorithm with _0 as the initial state

'''
WRITTEN RESPONSES
'''

'''
My A* implementation takes the same path as I took manually when I simulated the problem. At the first fork, it intially
moves up (uses rightChild) until it reaches area where the right path goes down and curves away from the goal state, 
in which case it begins following the left path all the way to the goal.
'''