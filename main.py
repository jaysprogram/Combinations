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
    

def calculate_result1(school):
    result = 1
    x_points = []
    y_points = []
    amntOfLoc = int(input())
    
    ## Loop x amount of time from input
    for i in range(0,amntOfLoc):
        inputs = input().split()
        x_points.append(int(inputs[0]))  # Convert and append x coordinate
        y_points.append(int(inputs[1]))
    
    #checks if its valid by making sure the sum of them all dont pass
    if (not if_valid_locations(x_points,school[0]) or not if_valid_locations(y_points,school[1])):
        return 0
    
    ##starting point is 0
    prev_x, prev_y = 0, 0
    for i in range(0,amntOfLoc):
        curr_x = x_points[i]
        curr_y = y_points[i]
        # Calculate the number of ways to get from (prev_x, prev_y) to (curr_x, curr_y)
        result *= choose(curr_x - prev_x + curr_y - prev_y, curr_x - prev_x)
        result %= MOD  # Take modulo to prevent overflow
        prev_x, prev_y = curr_x, curr_y  # Update previous coordinates

    # Calculate the number of ways to get from the last point to the school
    result *= choose(school[0] - prev_x + school[1] - prev_y, school[0] - prev_x)
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
            print(f"{calculate_result1(school)}")
        else:
            ## scenario 2 avoid bully
            pass
    
    
if __name__ == "__main__":
    main()