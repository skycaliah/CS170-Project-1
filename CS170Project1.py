import heapq as minHeap #minHeap 
import copy


#functions for mov
def moveUp(node,row,col):
    temp = node.board[row - 1][col]
    node.board[row-1][col] = 0
    node.board[row][col] = temp
    return

def moveDown(node,row,col):
    temp = node.board[row+1][col]
    node.board[row+1][col] = 0
    node.board[row][col] = temp
    return

def moveRight(node,row,col):
    temp = node.board[row][col+1]
    node.board[row][col+1] = 0
    node.board[row][col] = temp
    return

def moveLeft(node,row,col):
    temp = node.board[row][col-1]
    node.board[row][col-1] = 0
    node.board[row][col] = temp
    return


#class to store node of current puzzle and potential chlidren
# potential max of 4 children (move '0' up,down,right,left)      
class node:
    def __init__(self,board):
        self.board = board
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.depth = 0
        self.heuristic = 0


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
            newNode = copy.deepcopy(self)
            moveUp(newNode,row,col)
            if(newNode not in visited):
                self.child1 = newNode
                self.child1.depth +=1
                visited.append(self.child1)
            #print("When moving up:" + '\n') 
            #printPuzzle(newNode.board)

      
        #able to move down
        if(row < 2):
            newNode = copy.deepcopy(self)
            moveDown(newNode,row,col)
            if(newNode not in visited):
                self.child2 = newNode
                self.child2.depth +=1
                visited.append(self.child2)
            #print("When moving down:"+ '\n')
            #printPuzzle(newNode.board)
        
        #able to move right 
        if(col < 2):
            newNode = copy.deepcopy(self)
            moveRight(newNode,row,col)
            if(newNode not in visited):
                self.child3 = newNode
                self.child3.depth +=1
                visited.append(self.child3)
            #print("When moving right:"+ '\n') 
            #printPuzzle(newNode.board)
            

        #able to move left
        if(col != 0):
            newNode = copy.deepcopy(self)
            moveLeft(newNode,row,col)
            if(newNode not in visited):
                self.child4 = newNode
                self.child4.depth +=1
                visited.append(self.child4)
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
    return oh_boy

#Framework for menu prompts and printing puzzle from sample report given
def main():
    
    #create a node based off the user chosen board   
    testNode = node(puzzleGenerator())
    #printPuzzle(testNode.board)

    generalSearch(testNode)
    
    return

def printPuzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
    print('\n')

def generalSearch(problem):

    #queue of nodes to search through
    nodes = []

    #list of nodes already visited 
    visited = []

    #add inital state (problem) to the queue 
    nodes.append(problem)

    #variable to hold currBoard for initial while Check
    currNode = problem

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
    
        #obtain new node from queue 
        currNode = nodes.pop(0)
        printPuzzle(currNode.board)
        print("Current Node has depth of: ", currNode.depth)
        
    
        

        #GOAL_TEST for current node 
        if(goalAchieved(currNode)):
            print("Success: We found the solution!")
            printPuzzle(currNode.board)
            return 

        #implement queuing function 
        #nodes = qFunc(nodes,expand(node,OPERATORS))

        #directly only do uniform cost search 
        currNode.operators(visited)

        if(currNode.child1 != None):

            #printPuzzle(currNode.child1.board)
            nodes.append(currNode.child1)

        if(currNode.child2 != None):

            #printPuzzle(currNode.child2.board)
            nodes.append(currNode.child2)

        if(currNode.child3 != None):

           # printPuzzle(currNode.child3.board)
             nodes.append(currNode.child3)

        if(currNode.child4 != None):

            #printPuzzle(currNode.child4.board)
            nodes.append(currNode.child4)

    return




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





