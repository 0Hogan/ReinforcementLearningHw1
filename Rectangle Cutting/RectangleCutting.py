#=================================================================
# Rectangle Cutting Problem (https://cses.fi/problemset/task/1744)
# Solution by M.Hogan (V674R446)
#=================================================================
# a.) State Space:
#           The state space of the MDP for the Rectangle Cutting Problem consists of two variables: the height and the width of the given rectangle. 
#           Within the memoization table, `a` corresponds to the height/first inputted dimension, and `b` corresponds to the width/second inputted dimension.
#     Action Space:
#           The action space of the MDP for the Rectangle Cutting Problem consists of all the possible cuts that may be made to divide the current rectangle into two rectangles that each have a height and width that are both positive integers, to the point that the original rectangle is entirely composed of squares
#           These options may divide the height OR the width (but not both) of a rectangle into two smaller segments. For each rectangle, there are (height+width-2) possible actions that may be taken.
#     Reward Space:
#            The reward space of the MDP for the Rectangle Cutting Problem consists of a "-1" for each cut that is made, where the goal is to maximize the score while still achieving the endgoal.
#
# b.) Yes, this is indeed a substring problem as the defined approach begins by finding the optimal number of cuts for each possible sub-rectangle (or substring, if you will) that may result from a cut at a given height/width, and the results are then combined to find the optimal solution for the original rectangle. It is not a prefix/suffix problem, as there is no clear place to start.
#
# c.) See below.

import numpy

def ParseInput(inputString):
    inputList = inputString.split() # Split the input string on ' ' characters.
    for i in range(0, len(inputList)):
        inputList[i] = int(inputList[i]) # Cast the string version of the ints to ints.
    return inputList[0], inputList[1]


def IterativeCutRectangle(a, b):
    # Create an array to memoize all the optimal rectangle cutting solutions.
    memoizationList = [[0 for i in range(b+1)] for j in range(a+1)]

    # A rectangle of size nx1 will require n-1 cuts.
    for height in range(1, a + 1):
        memoizationList[height][1] = height - 1
    
    # A rectangle of size 1xn will require n-1 cuts.
    for width in range (1, b + 1):
        memoizationList[1][width] = width - 1

    # This set of loops is a big time-sucker: O(a*b*(a+b))
    for height in range(2, a + 1):
        for width in range(2, b + 1):
            # If the height == width, then it does not need to be cut (because it's already a square).
            if height == width:
                memoizationList[height][width] = 0
                
            else:
                # Declare and initialize minNumberOfCuts to the first possible answer.
                minNumberOfCuts = 501

                # For each possible cut (height-wise):
                for n in range(1, (height + 2) // 2):
                    # Calculate the cost of cutting the rectangle into two rectangles of size n*width and (height-n)*width respectively
                    minNumberOfCuts = min(minNumberOfCuts, (memoizationList[n][width] + memoizationList[height-n][width] + 1))

                # For each possible cut (width-wise):
                for n in range(1, (width + 2) // 2):
                    # Calculate the cost of cutting the rectangle into two rectangles of size height*n and height*(width-n) respectively
                    minNumberOfCuts = min(minNumberOfCuts, (memoizationList[height][n] + memoizationList[height][width-n] + 1))
                
                # Add 1 to the optimal solutions of the sub-problems to get the min number of cuts for a rectangle of size height*width
                memoizationList[height][width] = minNumberOfCuts

    # Return the optimal (minimal) number of cuts for a rectangle of height a and width b.
    return memoizationList[a][b]

memoizationArray = numpy.ones((501, 501)) * -1

def RecursiveCutRectangle(a,b):
    # Base case (given sides form a square):
    if (a == b):
        return 0
    
    # Secondary case (x*y rectangle where y==1 will require x-1 cuts to yield x squares):
    if (a == 1):
        return b - 1
    if (b == 1):
        return a - 1
    
    # If it's already been calculated:
    if (memoizationArray[a][b] > 0):
        return memoizationArray[a][b]

    # Otherwise, look for the best solution:
    # Find the optimal cut that can be made to divide a into two pieces.
    for n in range(1, (a+2)//2):
        numCuts = RecursiveCutRectangle(a-n, b) + RecursiveCutRectangle(n, b) + 1
        if (numCuts < memoizationArray[a][b] or memoizationArray[a][b] < 0):
            memoizationArray[a][b] = numCuts
    
    # Find the optimal cut that can be made to divide b into two pieces, and keep it if it's better than the optimal cut that can be made to divide a into two pieces.
    for n in range(1, (b+2)//2):
        numCuts = RecursiveCutRectangle(a, b-n) + RecursiveCutRectangle(a, n) + 1
        if (numCuts < memoizationArray[a][b]):
            memoizationArray[a][b] = numCuts
    
    # Return the optimal (minimal) number of cuts for a rectangle of height a and width b.
    return int(memoizationArray[a][b])

    

if (__name__ == "__main__"):
    inputString = input()
    a, b = ParseInput(inputString)
    print(IterativeCutRectangle(a, b))
    print("\n===================\n")
    print(RecursiveCutRectangle(a, b))


# d.) (Will be present in document...)
# 
# e.) Time Complexity The most expensive computation is the set of nested for loops in the `CutRectangle()` function.
#     The outermost `for` loop executes `a` times, where a is the first given integer.
#     The second-outermost `for` loop executes `b` times, where b is the second given integer.
#     There are two `for` loops nested within the immediately aforementioned `for` loop, the first of which executes in O(a) time and the second of which executes in O(b) time.
#     Thus, the total runtime can be described as O(a)*O(b)*(O(a)+O(b)), or:    
#           O(a*b*(a+b))