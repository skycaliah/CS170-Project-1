import copy
import time


#functions for mov
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

        #able to move up
        if(row > 0):
            newBoard = copy.deepcopy(self.board)
            moveUp(newBoard,row,col)
            if(newBoard not in visited):
                self.child1 = node(newBoard)
                self.child1.depth = self.depth + 1
                visited.append(self.child1.board)
            #print("When moving up:" + '\n') 
            #printPuzzle(newNode.board)

      
        #able to move down
        if(row < 2):
            newBoard = copy.deepcopy(self.board)
            moveDown(newBoard,row,col)
            if(newBoard not in visited):
                self.child2 = node(newBoard)
                self.child2.depth = self.depth + 1
                visited.append(self.child2.board)
            #print("When moving down:"+ '\n')
            #printPuzzle(newNode.board)
        
        #able to move right 
        if(col < 2):
            newBoard = copy.deepcopy(self.board)
            moveRight(newBoard,row,col)
            if(newBoard not in visited):
                self.child3 = node(newBoard)
                self.child3.depth = self.depth + 1
                visited.append(self.child3.board)
            #print("When moving right:"+ '\n') 
            #printPuzzle(newNode.board)
            

        #able to move left
        if(col != 0):
            newBoard = copy.deepcopy(self.board)
            moveLeft(newBoard,row,col)
            if(newBoard not in visited):
                self.child4 = node(newBoard)
                self.child4.depth = self.depth + 1
                visited.append(self.child4.board)
            #print("When moving left:"+ '\n') 
            #printPuzzle(newNode.board)

        return




#prompts user for type of puzzle and generates board
def puzzleGenerator():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own." + '\n')
    if puzzle_mode == "1":
        user_puzzle = [[0, 1, 2],
                       [4, 5, 3],
                       [7, 8, 6]]

        superEasy =  [[1, 2, 0],
                      [4, 5, 3],
                      [7, 8, 6]]

        doable = [[0, 1, 2],
                  [4, 5, 3],
                  [7, 8, 6]]                    
                               
        oh_boy = [[8, 7, 1],
                  [6, 0, 2],
                  [5, 4, 3]]

        depth8 = [[1, 3, 6],
                  [5, 0, 2],
                  [4, 7, 8]]

        depth12 = [[1, 3, 6],
                  [5, 0, 7],
                  [4, 8, 2]]

        depth16 = [[1, 6, 7],
                  [5, 0, 3],
                  [4, 8, 2]]

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
    return depth12

#Framework for menu prompts and printing puzzle from sample report given
def main():
    
    #start time 
    st = time.time()

    #create a node based off the user chosen board   
    testBoard = puzzleGenerator()
    #printPuzzle(testNode.board)

    qFunc = int(input("Enter what type of search you'd like to do: (1) Uniform Cost Search (2) A* with Misplaced Tile (3) A* with Manhattan Distance" + '\n'))

    generalSearch(testBoard,qFunc)

    #end time 
    et = time.time()
    elapsedTime = et-st

    print("RunTime was:", elapsedTime, "seconds")            
                                                        
    
    return

def printPuzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
    print('\n')

def generalSearch(problem,qFunc):

    #queue of nodes to search through
    nodes = []

    #list of nodes already visited 
    visited = []

    currNode = node(problem)

    #add inital state (problem) to the queue 
    nodes.append(currNode)

    #variable to hold currBoard for initial while Check
    visited.append(currNode.board)

    #initial check incase user enters solved board at start 
    if(goalAchieved(currNode)):
        print("You entered a solved board, try again!")
        printPuzzle(currNode.board)
        return 


    #loop that solves problem
    while(not goalAchieved(currNode)):
        
        #if queue is empty, no solution found. Terminate
        if(len(nodes) == 0):
            print ("Failure: No valid solution :/")
            return
    

        if(qFunc == 2):
            currNode.h = misplacedTile(currNode)

        #have queue sorted based of heuristc value 
        #minHeap.heappush(nodes,currNode)
        #minHeap.heapify(nodes)

        if(qFunc == 2 or qFunc ==3):
            nodes = sorted(nodes, key=lambda cost: cost.fn)

        #obtain new node from queue 
        currNode = nodes.pop(0)
        
        #add currNode as visited node before expanding
        visited.append(currNode.board)

        #print current board and it's depth 
        print("Current Node has depth of: ", currNode.depth)
        printPuzzle(currNode.board)
   
        
    
        

        #GOAL_TEST for current node 
        if(goalAchieved(currNode)):
            print("Success: We found the solution!")
            printPuzzle(currNode.board)
            return 

        #implement queuing function 
        #nodes = qFunc(nodes,expand(node,OPERATORS))

        #Call available operators to expand currNode and create all its children
        currNode.operators(visited)

        #Series of checks to update child values of currNode and append to list of queues
        if(currNode.child1 != None):

            if(qFunc == 2):
                currNode.child1.h = misplacedTile(currNode.child1)
                currNode.child1.fn = currNode.child1.h + currNode.child1.depth

            #printPuzzle(currNode.child1.board)
            nodes.append(currNode.child1)
            visited.append(currNode.child1.board)


        if(currNode.child2 != None):

            if(qFunc == 2):
                currNode.child2.h = misplacedTile(currNode.child2)
                currNode.child2.fn = currNode.child2.h + currNode.child2.depth

            #printPuzzle(currNode.child2.board)
            nodes.append(currNode.child2)
            visited.append(currNode.child2.board)


        if(currNode.child3 != None):

             if(qFunc == 2):
                currNode.child3.h = misplacedTile(currNode.child3)
                currNode.child3.fn = currNode.child3.h + currNode.child3.depth

           # printPuzzle(currNode.child3.board)
             nodes.append(currNode.child3)
             visited.append(currNode.child3.board)


        if(currNode.child4 != None):

            if(qFunc == 2):
                currNode.child4.h = misplacedTile(currNode.child4)
                currNode.child4.fn = currNode.child4.h + currNode.child4.depth

            #printPuzzle(currNode.child4.board)
            nodes.append(currNode.child4)
            visited.append(currNode.child4.board)


    return

#misplacedTile Heuristic. Count number of misplaced tiles (not including the blank)
def misplacedTile(node):
    numMisplaced = 0
    solvedPuzzle = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]

    for i in range( len(node.board) ) :
            for j in range( len(node.board) ):
                if (node.board[i][j] != solvedPuzzle[i][j] and node.board[i][j] != 0 ):
                    numMisplaced += 1

    return numMisplaced
    


#evaulates whether a particular state/node is the goal state 
def goalAchieved(problem):
    
    solvedPuzzle = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]

    solvedNode = node(solvedPuzzle)

    if(problem.board == solvedNode.board):
        return True
    else:
        return False


main()





