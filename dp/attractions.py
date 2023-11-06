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
    #we'll use dictionaries because they're easier to read
    attractions = []
    fi = open(argv[1], "r")
    for line in fi:
        line = line.replace("\n", "").split(" ")[:2] #strings are immutable in Python
        entry = {"name": line[0], "cost":int(line[1])}
        attractions.append(entry)
      
    #algorithm
    
    highest_costs = [0]*len(attractions)
    #notice that the minimalis cost of visiting every attraction 
    #is the difference between the maximal cost of missing
    #every possible attraction and the total cost
    highest_costs[0] = (attractions[0]["cost"], -1)
    highest_costs[1] = (attractions[1]["cost"], -1)
    total_cost = attractions[0]["cost"] + attractions[1]["cost"]
    for i in range(2, len(attractions)):
        (prevCost, prev) = highest_costs[i-1]
        (prevPrevCost, prevPrev) = highest_costs[i-2]
        if attractions[i]["cost"] + prevPrevCost > prevCost:
            highest_costs[i] = (attractions[i]["cost"]+prevPrevCost, i-2)
        else:
            highest_costs[i] = (prevCost, i-1)
        total_cost += attractions[i]["cost"]

    
    
    #This is the list of the most expensive, skippable attractions
    #We'll just need to trim it so that it is less than or equal to k
    
    # expensive_attractions
    expensive_attractions = [attractions[-1]]
    (prevCost, prev) = highest_costs[-1]
    while prev > -1:
        expensive_attractions.append(attractions[prev])
        (prevCost, prev) = highest_costs[prev]
    print(attractions)
    print(highest_costs)
    print(total_cost - highest_costs[-1][0])
    print(expensive_attractions)
    

if __name__ == "__main__":
    main()