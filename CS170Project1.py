import copy
import time

#functions for moving tile in respective location (up,down,right,left)
def moveUp(board,row,col):
    temp = board[row - 1][col]
    board[row-1][col] = 0
    board[row][col] = temp
    return

def moveDown(board,row,col):
    temp = board[row+1][col]
    board[row+1][col] = 0
    board[row][col] = temp
    return

def moveRight(board,row,col):
    temp = board[row][col+1]
    board[row][col+1] = 0
    board[row][col] = temp
    return

def moveLeft(board,row,col):
    temp = board[row][col-1]
    board[row][col-1] = 0
    board[row][col] = temp
    return


#class to store node of current puzzle and potential chlidren
# potential max of 4 children (move '0' up,down,right,left)  
# depth: how far node is in tree
# h: heuristic value 
# fn: depth + heuristic     
class node:
    def __init__(self,board):
        self.board = board
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.depth = 0
        self.h = 0
        self.fn = 0



    #evaluates possible operators (visited holds list of visited nodes to avoid repeated states )
    def operators(self,visited):

        #find current location of '0' tile to move
        for i in range( len(self.board) ) :
            for j in range( len(self.board) ):
                if self.board[i][j]  == 0:
                    row = i
                    col = j


        #Calling operators for each possible case
        #Can change if conditions to n variable values 
        #for n x n puzzles 
        #Updated children nodes for currNode and increases depth if able to move for each node

        #able to move up
        if(row > 0):
            newBoard = copy.deepcopy(self.board)
            moveUp(newBoard,row,col)
            if(newBoard not in visited):
                self.child1 = node(newBoard)
                self.child1.depth = self.depth + 1

      
        #able to move down
        if(row < 2):
            newBoard = copy.deepcopy(self.board)
            moveDown(newBoard,row,col)
            if(newBoard not in visited):
                self.child2 = node(newBoard)
                self.child2.depth = self.depth + 1

        
        #able to move right 
        if(col < 2):
            newBoard = copy.deepcopy(self.board)
            moveRight(newBoard,row,col)
            if(newBoard not in visited):
                self.child3 = node(newBoard)
                self.child3.depth = self.depth + 1

        #able to move left
        if(col != 0):
            newBoard = copy.deepcopy(self.board)
            moveLeft(newBoard,row,col)
            if(newBoard not in visited):
                self.child4 = node(newBoard)
                self.child4.depth = self.depth + 1

        return

#prompts user for type of puzzle and generates board
#creation of custom puzzle gathered from Project Assignment 
def puzzleGenerator():

    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own." + '\n')

    #Allow user to pick default puzzle of particular depth
    #Puzzles below gathered from Project Assignment
    if puzzle_mode == "1":

        depthProblem = int(input("Choose your problem's depth by entering a '0' '2' '4' '8' '12' '16' '20' or '24'" + '\n'))

        if(depthProblem == 0):
            user_puzzle = [[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 0]]

        elif(depthProblem == 2):
            user_puzzle = [[1, 2, 3],
                           [4, 5, 6],
                           [0, 7, 8]]

        elif(depthProblem == 4):
            user_puzzle = [[1, 2, 3],
                           [5, 0, 6],
                           [4, 7, 8]]

        elif(depthProblem == 8):
            user_puzzle = [[1, 3, 6],
                           [5, 0, 2],
                           [4, 7, 8]]
        elif(depthProblem == 12):
            user_puzzle = [[1, 3, 6],
                           [5, 0, 7],
                           [4, 8, 2]]

        elif(depthProblem == 16):
            user_puzzle = [[1, 6, 7],
                           [5, 0, 3],
                           [4, 8, 2]]

        elif(depthProblem == 20):
            user_puzzle = [[7, 1, 2],
                           [4, 8, 5],
                           [6, 3, 0]]

        elif(depthProblem == 24):
            user_puzzle = [[0, 7, 2],
                           [4, 6, 1],
                           [3, 5, 8]]


    #Create custom user puzzle
    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " +
              "Please only enter valid 8-puzzles. Enter the puzzle with spaces between the numbers." + '\n')

        #get input from user for each row 
        puzzle_row_one = input("Enter the first row: ")
        puzzle_row_two = input("Enter the second row: ")
        puzzle_row_three = input("Enter the third row: ")

        #seperates the input into distint numbers for 2d-array
        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()

        #combines split inputs into one single user puzzle 
        for i in range(0, 3):
            puzzle_row_one[i] = int(puzzle_row_one[i])
            puzzle_row_two[i] = int(puzzle_row_two[i])
            puzzle_row_three[i] = int(puzzle_row_three[i])

        #storing user puzzle    
        user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]

    #return user_puzzle
    return user_puzzle

#Framework for menu prompts and printing puzzle from sample report given
def main():
    
    

    #create a node based off the user chosen board   
    testBoard = puzzleGenerator()

    #Set what kind of heuristic we will use
    qFunc = int(input("Enter what type of search you'd like to do: (1) Uniform Cost Search (2) A* with Misplaced Tile (3) A* with Manhattan Distance" + '\n'))

    #start time 
    st = time.time()

    #begin search to find solution
    generalSearch(testBoard,qFunc)

    #end time 
    et = time.time()
    elapsedTime = et-st

    print("RunTime was:", elapsedTime, "seconds")            
                                                        
    
    return

#helper function to print puzzle 
def printPuzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
    print('\n')

def generalSearch(problem,qFunc):

    #global variable for keeping track of runtime statistics
    #expandedNodes: number of nodes be expanded through operators 
    #maxQ: the max value see so far in the queue 
    #tempQ: temp variable for holding current queue count for updating maxQ
    expandedNodes = 0
    maxQ = 0
    tempQ = 0


    #queue of nodes to search through
    nodes = []

    #list of nodes already visited 
    visited = []

    #initialize 1st node (initial state)
    currNode = node(problem)

    #add inital state (problem) to the queue 
    nodes.append(currNode)
    tempQ +=1
    maxQ +=1
    
    #variable to hold currBoard for initial while Check
    visited.append(currNode.board)

    #initial check incase user enters solved board at start 
    if(goalAchieved(currNode)):
        print("Goal state!")
        printPuzzle(currNode.board)
        print("Solution depth was:", currNode.depth)
        print("Number of nodes expanded:", expandedNodes)
        print("Max queue size:",maxQ )
        print("Temp queue size:", tempQ)
        return 




    #main loop that solves problem
    while(not goalAchieved(currNode)):
        
        #if queue is empty, no solution found. Terminate
        if(len(nodes) == 0):
            print ("Failure: No valid solution :/")
            return


        #set herusictic value depending on user input
        if(qFunc == 2):
            currNode.h = misplacedTile(currNode)

        elif(qFunc == 3):
            currNode.h = manhattanDist(currNode)

        #have queue sorted based off heuristc value 
        if(qFunc == 2 or qFunc ==3):
            nodes = sorted(nodes, key=lambda cost: (cost.fn, cost.depth))

        #obtain new node from queue 
        currNode = nodes.pop(0)
        tempQ -=1
        expandedNodes +=1

        
        #add currNode as visited node before expanding
        visited.append(currNode.board)

        #print current board and it's depth 
        print("The best state to expand with a g(n)=", currNode.depth, "and h(n)= ", currNode.h)
        printPuzzle(currNode.board)
   

        #GOAL_TEST for current node 
        if(goalAchieved(currNode)):
            print("Goal state!")
            printPuzzle(currNode.board)
            print("Solution depth was:", currNode.depth)
            print("Number of nodes expanded:", expandedNodes)
            print("Max queue size:",maxQ )
            print("Temp queue size:", tempQ)

            return 


        #Call available operators to expand currNode and create all its children
        currNode.operators(visited)

        #Series of checks to update heuristic cost for each child and append to queue of nodes 
        #and visited nodes 
        if(currNode.child1 != None):

            if(qFunc == 2):
                currNode.child1.h = misplacedTile(currNode.child1)
            elif(qFunc == 3):
                currNode.child1.h = manhattanDist(currNode.child1)

            currNode.child1.fn = currNode.child1.h + currNode.child1.depth
            
            nodes.append(currNode.child1)
            visited.append(currNode.child1.board)

            tempQ +=1


        if(currNode.child2 != None):

            if(qFunc == 2):
                currNode.child2.h = misplacedTile(currNode.child2)
            elif(qFunc == 3):
                currNode.child2.h = manhattanDist(currNode.child2)

            currNode.child2.fn = currNode.child2.h + currNode.child2.depth

            #printPuzzle(currNode.child2.board)
            nodes.append(currNode.child2)
            visited.append(currNode.child2.board)

            tempQ +=1


        if(currNode.child3 != None):

            if(qFunc == 2):
                currNode.child3.h = misplacedTile(currNode.child3)
            elif(qFunc == 3):
                currNode.child3.h = manhattanDist(currNode.child3)

            currNode.child3.fn = currNode.child3.h + currNode.child3.depth
            nodes.append(currNode.child3)
            visited.append(currNode.child3.board)

            tempQ +=1


        if(currNode.child4 != None):

            if(qFunc == 2):
                currNode.child4.h = misplacedTile(currNode.child4)
            elif(qFunc == 3):
                currNode.child4.h = manhattanDist(currNode.child4)

            currNode.child4.fn = currNode.child4.h + currNode.child4.depth
            nodes.append(currNode.child4)
            visited.append(currNode.child4.board)

            tempQ +=1


        #check for updating maxQ
        if(tempQ > maxQ):
            maxQ = tempQ

    return

#misplacedTile Heuristic. Count number of misplaced tiles (not including the blank)
def misplacedTile(node):

    #heuristic return value
    #number of nodes not in goal location
    numMisplaced = 0
    solvedPuzzle = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]

    #for loop iterates through and checks each tile to see if it is 
    #in the right position on the board (excluding 0)
    for i in range( len(node.board) ) :
            for j in range( len(node.board) ):
                if (node.board[i][j] != solvedPuzzle[i][j] and node.board[i][j] != 0 ):
                    numMisplaced += 1

    return numMisplaced
 
#manhattanDistance Heuristic. Count number of moves needed to move each individual piece and return the sum   
def manhattanDist(node):
        
    solvedPuzzle = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]


    #array to hold index values of 2 array mapping to solvedPuzzle
    goalIndex = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]


    #variable to hold current row and current column of loop for ease of reading
    currRow = 0
    currCol = 0

    #number of moves needed to get particular number in proper position
    moveDistance = 0

    #for loop iterates through board and for each misplaced tile will calculate 
    #the number of moves needed to get to goal location using index of array and goalIndex(array of tuple index locations)
    for i in range( len(node.board) ) :
        for j in range( len(node.board) ):
            if(node.board[i][j] != solvedPuzzle[i][j]):
                currRow = i
                currCol = j

                #calculates number of moves based on index of current board and goal state for each respective tile using array of tuples
                #goalIndex[ . . .]
                if(node.board[i][j] != 0):
                    moveDistance += abs(goalIndex[ node.board[i][j] -1 ][0] - currRow) + abs( goalIndex[ node.board[i][j] -1 ][1] - currCol )

    return moveDistance

#Function for evaluation whether or not a current board is the goal state
def goalAchieved(problem):
    
    solvedPuzzle = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]

    solvedNode = node(solvedPuzzle)

    if(problem.board == solvedNode.board):
        return True
    else:
        return False


#call main
main()





