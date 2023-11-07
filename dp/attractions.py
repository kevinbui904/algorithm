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
    if(arg_count > 3):
        print("Only two arguments are allowed")
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
    
    highest_costs = [(0,0)]*len(attractions)
    #notice that the minimalis cost of visiting every attraction 
    #is the difference between the maximal cost of missing
    #every possible attraction and the total cost

    #for keeping track of the sequence that results in the maximum sum
    global_prev = None 
    global_max = attractions[0]["cost"]    
    highest_costs[0] = (attractions[0]["cost"], 0)
    if attractions[1]["cost"] > attractions[0]["cost"]:
        highest_costs[1] = (attractions[1]["cost"], 1)
        global_max = attractions[1]["cost"]
        global_prev = 1
    else:
        highest_costs[1] = (attractions[0]["cost"],0)
        global_prev = 0
    print(global_max)
    total_cost = attractions[0]["cost"] + attractions[1]["cost"]
    for i in range(2, len(attractions)):
        (prev_cost, prev) = highest_costs[i-1]
        (prev_prev_cost, prev_prev) = highest_costs[i-2]
        if attractions[i]["cost"] + prev_prev_cost > prev_cost:
            highest_costs[i] = (attractions[i]["cost"] + prev_prev_cost, prev_prev)
            if attractions[i]["cost"] + prev_prev_cost > global_max:
                global_max = attractions[i]["cost"] + prev_prev_cost
                global_prev = i
                print("here", global_prev)
                
    #     (prev_cost, prev) = highest_costs[i-1]
    #     (prev_prev_cost, prev_prev) = highest_costs[i-2]
    #     if attractions[i]["cost"] + prev_prev_cost > prev_cost:
    #         if attractions[i]["cost"]+prev_prev_cost > global_max:
    #             global_prev = i
    #         highest_costs[i] = (attractions[i]["cost"]+prev_prev_cost, i-2)
    #     else:
    #         print("HERE", prev, i, highest_costs[4])
    #         highest_costs[i] = (prev_cost, global_prev)
        total_cost += attractions[i]["cost"]
    print(global_prev)
    print(highest_costs)

    quit()
    
    #This is the list of the most expensive, skippable attractions
    #We'll just need to trim it so that it is less than or equal to k
    
    # expensive_attractions
    (cost, prev) = highest_costs[-1]
    expensive_attractions = [attractions[prev]]
    while prev > 1:
        expensive_attractions.append(attractions[prev])
        (cost, prev) = highest_costs[prev]
    expensive_attractions = sorted(expensive_attractions, key=lambda d: d["cost"], reverse=True)

    print(expensive_attractions[:int(argv[2])])
    print(total_cost - highest_costs[-1][0])
    print(highest_costs)    
    print(highest_costs[-1])

if __name__ == "__main__":
    main()