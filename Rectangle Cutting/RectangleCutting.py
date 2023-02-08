# Given an a*b rectangle, your task is to cut it into squares. On each move you can select a rectangle and cut it into two rectangles in such a way that all side lengths remain integers. What is the minimum possible number of moves?
# 
#   ----------------------
#   |                    |
# a |                    |
#   |                    |
#   ----------------------
#             b
import time

def ParseInput(inputString):
    inputList = inputString.split() # Split the input string on ' ' characters.
    for i in range(0, len(inputList)):
        inputList[i] = int(inputList[i]) # Cast the string version of the ints to ints.
    return inputList[0], inputList[1]


def CutRectangle(a, b):
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

    return memoizationList[a][b]

if (__name__ == "__main__"):
    startTime = time.perf_counter()
    inputString = input()
    a, b = ParseInput(inputString)
    print(CutRectangle(a, b))
    stopTime = time.perf_counter()
    runTime = stopTime - startTime
    print(f"Program ran in {runTime} seconds!")