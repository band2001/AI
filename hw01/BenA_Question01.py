'''
Ben Anderson
CSCI 379 Homework 1
Question 1
'''

'''
File Structure:
    1. Define Goal, Create Tree Data Structure, Graph, and PrintSoln Function
    2. BFS Implementation
    3. DFS Implementation
    4. Written responses
'''

'''
GENERAL DATA STRUCTURES AND FUNCTIONS IMPLEMENTATION
'''

# the total sum goal (for easy access to modify)
goal = 27

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

# create graph
    # initialize the data for each tree node; the names they are initialized with should indicate which one they are on the graph
root = TreeNode(6, "Root (Tree Top Node)") # (data, name)
level1_a = TreeNode(5, "1A (Level 1, 1st Node)")
level1_b = TreeNode(9, "1B (Level 1, 2nd Node)")
level2_a = TreeNode(9, "2A (Level 2, 1st Node)")
level2_b = TreeNode(3, "2B (Level 2, 2nd Node)")
level2_c = TreeNode(5, "2C (Level 2, 3rd Node)")
level3_a = TreeNode(9, "3A (Level 3, 1st Node)")
level3_b = TreeNode(7, "3B (Level 3, 2nd Node)")
level3_c = TreeNode(3, "3C (Level 3, 3rd Node)")
    
    # assign children and parents appropriately; using the above definitions for assignment
root.setTreeStructure(level1_a, level1_b, 0) # (leftChild, rightChild, parent)
level1_a.setTreeStructure(level2_a, 0, root)
level1_b.setTreeStructure(level2_b, level2_c, root)
level2_a.setTreeStructure(level3_a, level3_b, level1_a)
level2_b.setTreeStructure(0, 0, level1_b)
level2_c.setTreeStructure(level3_c, 0, level1_b)
level3_a.setTreeStructure(0, 0, level2_a)
level3_b.setTreeStructure(0, 0, level2_a)
level3_c.setTreeStructure(0, 0, level2_c)

# define a function to print out the solution

def printSoln(tree_node): # recursive function that will print the path taken from the root to current node, with running total next to name
    if not tree_node.parent: # checks if root
        print(tree_node.name + " " + str(tree_node.total)) # prints solution line
        return [[tree_node.name, str(tree_node.total)]] # returns the string printed in array form
    prev_text = printSoln(tree_node.parent) # if not root
    prev_text.append([tree_node.name, str(tree_node.total)])
    print(tree_node.name + " " + str(tree_node.total)) # prints solution line
    return prev_text # returns array with all printed strings in array form

'''
BREADTH FIRST SEARCH IMPEMENTATION
'''

# create queue data structure

class Queue:
    def __init__(self): # initializing the queue
        self.array = []
    
    def inject(self, item): # queue inject function, makes use of the list append feature, takes a parameter item to add
        self.array.append(item)
    
    def eject(self): # queue eject function, checks to make sure queue is not empty before returning value
        if not self.array:
            return 0
        item = self.array[0]
        self.array = self.array[1:]
        return item
    
    def getArray(self): # function that returns the array; used to see if array is empty or not
        return self.array


# create explored list and running total dictionary

explored = []

# implement the breadth first search algorithm (as a function)

def bfs(tree_root): # takes the root of the tree as the only parameter
    print('BFS SOLUTION') # helps make solution printings clearer in end
    if tree_root.getData() == goal: # checks if initial state is goal state
        printSoln(tree_root) # prints solution
        return 1 # returns 1 on success

    frontier = Queue() # initializes the frontier as a queue
    frontier.inject(tree_root) # injects tree_root as the initial state

    while frontier.getArray: # the bfs loop, runs as long as there are items in the queue
        current = frontier.eject() # eject from the loop (take out the oldest item in the queue)
        explored.append(current) # add the ejected node to the explored array
        

        if current.parent: # updates total to check for correct solution based on whether there is a parent or not
            current.total = current.parent.total + current.getData() 
        else:
            current.total = current.getData()

        if current.total == goal: # checks to see if goal is met; total stores the running total up to and including the node
            printSoln(current) # prints out the solution
            return 1 # returns 1 on success

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

# run the search algorithm
bfs(root)

'''
DEPTH FIRST SEARCH IMPLEMENTATION
'''

# create queue data structure

class Stack:
    def __init__(self): # initializing the stack
        self.array = []
    
    def push(self, item): # stack push function, makes use of the list append feature, takes a parameter item to add
        self.array.append(item)
    
    def pop(self): # stack eject function, checks to make sure stack is not empty before returning value
        if not self.array:
            return 0
        item = self.array[-1]
        self.array = self.array[:-1]
        return item
    
    def getArray(self): # function that returns the array; used to see if array is empty or not
        return self.array

# create explored list and running total dictionary

explored = []

# implement the depth first search algorithm (as a function)

def dfs(tree_root): # takes the root of the tree as the only parameter
    print('\nDFS SOLUTION') # makes solution clearer
    if tree_root.getData() == goal: # checks if initial state is goal state
        printSoln(tree_root) # prints solution
        return 1 # returns 1 on success

    frontier = Stack() # initializes the frontier as a queue
    frontier.push(tree_root) # injects tree_root as the initial state

    while frontier.getArray: # the dfs loop, runs as long as there are items in the stack
        current = frontier.pop() # pop from the stack (take out the newest item in the stack)
        explored.append(current) # add the popped node to the explored array
        

        if current.parent: # updates total to check for correct solution based on whether there is a parent or not
            current.total = current.parent.total + current.getData() 
        else:
            current.total = current.getData()

        if current.total == goal: # checks to see if goal is met; total stores the running total up to and including the node
            printSoln(current) # prints out the solution
            return 1 # returns 1 on success

        inExplored = 0 # bool to check if left child is in the explore array or not
        for i in explored: # checks to see if leftChild has been explored
            if i == current.leftChild:
                inExplored = 1
                break
        if not inExplored and current.leftChild != 0: # if not explored AND exists, push to stack
            frontier.push(current.leftChild)

        inExplored = 0 # bool to check if right child is in the explore array or not
        for i in explored: # checks to see if rightChild has been explored
            if i == current.rightChild:
                inExplored = 1
                break
        if not inExplored and current.rightChild != 0: # if not explored AND exists, push to stack
            frontier.push(current.rightChild)

    print("No solution") # print statement for no solution
    return -1 # return case for no solution

# run the search algorithm
dfs(root)

'''
WRITTEN RESPONSES
'''

'''
The DFS algorithm finds the correct solution faster when the goal state is 27. This is because the solution to get 27
requires travelling deep in the graph (from root to leaf). So trying to go deep and backtrack makes more sense than
going level by level if you have a general idea that the solution is deep in the tree (far from the initial state). 
On the other hand, say the goal state was 15 (which can be achieved with the root and one of its children), then BFS 
would be faster because the solution is closer to the initial state.
'''