#Written by Thien K. M. Bui <kevinbui904@gmail.com>
#Last modified Nov 06, 2023

#This is a different perspective of the House Robber Problem (medium)
#on Leetcode

#Description
#Given a list of attractions c1,c2,...,cn with associated cost,
#Return the list of attractions to skip such that the total cost of 
#skipped attractions are minimized. Note that we are unable to skip
#more than 1 attractions in a row

#The following commands will run the program
# > python3 attractions.py [filename]
# > output, a solution.txt file that list the attractions we should skip

from sys import argv

def main():
    arg_count = len(argv)
    print("Params passed", arg_count - 1, ":", argv[1:])
    if(arg_count > 2):
        print("Only one argument is allowed")
        quit()

    #we first need to load the txt file into memory
    attractions = []
    fi = open(argv[1], "r")
    for line in fi:
        line = line.replace("\n", "") #strings are immutable in Python
        entry = line.split(" ")[:2]
        entry[1] = int(entry[1])
        attractions.append(entry)
    
    #algorithm
    cost = [0]*len(attractions)
    cost[0] = (attractions[0][1], 0)
    cost[1] = (attractions[1][1], 0)
    for i in range(2, len(attractions)):
        if attractions[i][1] + cost[i-2][0] < cost[i-1][0]:
            cost[i] = (attractions[i][1]+cost[i-2][0], i-2)
        else:
            cost[i] = (cost[i-1][0], i-1)
            
    print(attractions)
    print(cost)
    
    

if __name__ == "__main__":
    main()