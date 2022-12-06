import pandas as pd

#function to import data
def importData():
    data = pd.read_csv("CS170_Small_Data__110.txt", sep="  ", engine='python', header=None)
    return data


#create basic search to search through data 
def feature_search(data):

    for i in range( len(data)):
        print ("On the ", i, " level of the search tree." + '\n')

        for k in range (len(data)):
            print("--Considering adding the ", k, " feature")




    return 

def main():

    feature_search( importData() )


    return 


main()