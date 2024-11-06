## Reyjay Collazo
## Pa01
## Notes: can be greatly reduced in size if implemented more modular functions

import math

# Define the modulus
MOD = 1000000007


# Returns n choose k.
def choose(n,k):
    return math.factorial(n)//math.factorial(k)//math.factorial(n-k)

def if_valid_locations(points,schoolLoc):
    prevPoint = 0
    # ensures the points are going in increasing order not decreasing
    for point in points:
       if point >= prevPoint:
           prevPoint = point
       else:
           return False
    
    #makes sure point doesnt pass school
    if points[-1] > schoolLoc:
        return False
    
    return True
    

def calculate_result_type_1(school):
    result = 1
    x_points = []
    y_points = []
    amntOfLoc = int(input())
    
    ## Loop x amount of time from input
    for i in range(0,amntOfLoc):
        inputs = input().split()
        x_points.append(int(inputs[0]))  # Convert and append x coordinate
        y_points.append(int(inputs[1]))
    
    #checks if its valid by making sure neither x or y decreases
    if (not if_valid_locations(x_points,school[0]) or not if_valid_locations(y_points,school[1])):
        return 0
    
    ##starting point is 0
    prev_x, prev_y = 0, 0
    for i in range(0,amntOfLoc):
        curr_x = x_points[i]
        curr_y = y_points[i]
        # Calculate the number of ways to get from (prev_x, prev_y) to (curr_x, curr_y)
        result *= choose(curr_x - prev_x + curr_y - prev_y, curr_x - prev_x)
        result %= MOD 
        prev_x, prev_y = curr_x, curr_y  # Update previous coordinates

    # Calculate the number of ways to get from the last point to the school
    result *= choose(school[0] - prev_x + school[1] - prev_y, school[0] - prev_x)
    result %= MOD  # Take modulo to prevent overflow
    
    return result

def calculate_result_type_2(school): ## I can make the code more modular by making taking the input a function
    result = 1
    x_points = []
    y_points = []
    amntOfLoc = int(input())
    
    ## Loop x amount of time from input
    for i in range(0,amntOfLoc):
        inputs = input().split()
        x_points.append(int(inputs[0]))  # Convert and append x coordinate
        y_points.append(int(inputs[1]))
    
    #checks if its valid by making sure neither x or y decreases
    if (not if_valid_locations(x_points,school[0]) or not if_valid_locations(y_points,school[1])):
        return 0
    schoolX = school[0]
    schoolY = school[1]
    ## formula1: total ways to school - [ways through bully 1 to school]
    ## formula2: total ways to school - [ways through bully 1 to school * ways through bully 2 to school - paths through both bullies]

    prev_x, prev_y = 0, 0
    # First bully
    result = choose(x_points[0] + y_points[0],x_points[0]) * choose(schoolX - x_points[0] + schoolY - y_points[0],schoolX - x_points[0]) % MOD
    if len(x_points) == 1: ### the case where its only one bully
        pass 
    else: 
        ## When there is two bullies
        result += choose(x_points[1] + y_points[1],x_points[1]) * choose(schoolX - x_points[1] + schoolY - y_points[1],schoolX - x_points[1]) % MOD
        result -= choose(x_points[0] + y_points[0],x_points[0]) * \
            choose(x_points[1] - x_points[0] + y_points[1] - y_points[0],x_points[1] - x_points[0]) * \
            choose(schoolX - x_points[1] + schoolY - y_points[1],schoolX - x_points[1]) % MOD 

    # Calculate the number of ways to get from (0,0) to the school and subtract it 
    result = choose(schoolX + schoolY, schoolX) - result
    result %= MOD  # Take modulo to prevent overflow
    
    return result


def main():
    #get x y cords
    school = [0,0]
    school[0], school[1] = map(int, input().split())
    
    ## get inquries
    inquries = int(input())
    for i in range(0,inquries):
        scenario = int(input())
        
        if scenario == 1:
            print(f"{calculate_result_type_1(school)}")
        else:
            ## scenario 2 avoid bully
            print(f"{calculate_result_type_2(school)}")
            pass
    
    
if __name__ == "__main__":
    main()