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


    #evaluates possible operators
    def operators(self):

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
            print("When moving up:" + '\n') 
            printPuzzle(newNode.board)
        
        
        #able to move down
        if(row < 2):
            newNode = copy.deepcopy(self)
            moveDown(newNode,row,col)
            print("When moving down:"+ '\n')
            printPuzzle(newNode.board)
        
        #able to move right 
        if(col < 2):
            newNode = copy.deepcopy(self)
            moveRight(newNode,row,col)
            print("When moving right:"+ '\n') 
            printPuzzle(newNode.board)
            

        #able to move left
        if(col != 0):
            newNode = copy.deepcopy(self)
            moveLeft(newNode,row,col)
            print("When moving left:"+ '\n') 
            printPuzzle(newNode.board)

        return


#prompts user for type of puzzle and generates board
def puzzleGenerator():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own." + '\n')
    if puzzle_mode == "1":
        user_puzzle =   [[0, 1, 2],
                        [4, 5, 3],
                        [7, 8, 6]]

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
    return user_puzzle

#Framework for menu prompts and printing puzzle from sample report given
def main():
    
    #create a node based off the user chosen board   
    testNode = node(puzzleGenerator())
    printPuzzle(testNode.board)

    testNode.operators()

    return

def printPuzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
    print('\n')



def generalSearch(problem, qFunct):

    #queue of nodes to search through
    nodes = []

    #creting initial state(parent node)
    parentNode = node(problem)

    #add inital state (parent node) to the queue 
    nodes.append(parentNode)


    while(not goalAchieved):
        
        #if queue is empty, no solution found. Terminate
        if(nodes.isEmpty()):
            print ("Failure: No valid solution :/")
            return
    
        #obtain new node from queue 
        currNode = nodes.pop()

        #GOAL_TEST for current node 
        if(goalAchieved(currNode)):
            print("Success: We found the solution!")
            print (currNode)
            return 

        #implement queuing function 
        #nodes = qFunc(nodes,expand(node,OPERATORS))


    return




#evaulates whether a particular state/node is the goal state 
def goalAchieved(problem):
    
    solvedPuzzle = [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8]]

    if(problem == solvedPuzzle):
        return True
    else:
        return False


main()





