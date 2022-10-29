import heapq as minHeap #minHeap 

#class to store node of current puzzle and potential chlidren  
class node:
    def __init__(self):
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None




#Framework for menu prompts and printing puzzle from sample report given
def main():
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


    print_puzzle(user_puzzle)
    return

def print_puzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
    print('\n')



def generalSearch(problem, qFunct):

    #queue of nodes to search through
    q = []

    #creting initial state(parent node)
    parentNode = node(problem)

    #add inital state (parent node) to the queue 
    q.append(parentNode)


    while(not goalAchieved):
        
        #if queue is empty, no solution found. Terminate
        if(q.isEmpty()):
            print ("Failure: No valid solution :/")
            return
    
        #obtain new node from queue 
        currNode = q.pop()

        #GOAL_TEST for current node 
        if(goalAchieved(currNode)):
            print("Success: We found the solution!")
            print (currNode)
            return 

        #implement queuing function 
        #q = qFunc(q,expand(currNode,OPERATORS))


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





