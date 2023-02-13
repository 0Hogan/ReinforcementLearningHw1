#=================================================================
# Removal Game Problem (https://cses.fi/problemset/task/1097)
# Solution by M.Hogan (V674R446)
#=================================================================
# a.) State Space:
#           The state space of the MDP for the Removal Game Problem consists of a total of two variables: the number of values in the given list (represented by `numberOfElements`) and the list of values (represented by `gameList`).
#    
#     Action Space:
#           The action space of the MDP for the Removal Game Problem consists of choosing to remove the first item or the last item in the given list.
#
#     Reward Space:
#            The reward space of the MDP for the Removal Game Problem consists of a "+gameList[x]", where gameList[x] is the value associated with the item removed from the list as a result of the selected action.
#
# b.) Yes, this is a substring problem, as the defined approach begins with solving for the optimal solution of each sub-list of elements, gradually expanding the number of elements in that sub-list so that the optimal solution for each possible sub-list (or substring, if you will) of the original list is found. It is not a prefix/suffix problem, as there is no clear place to start.
#
# c.) See below.

import numpy
memoizationArray = numpy.ones((5001, 5001)) * -1

def ParseInput():
    # Get the inputs:
    numberOfElements = int(input())
    stringOfElements = input()

    # Split the string of elements on whitespace and cast each element to an int
    elementList = stringOfElements.split()
    for i in range(0, len(elementList)):
        elementList[i] = int(elementList[i])
    
    # Return the number of elements in the list as well as the list itself.
    return numberOfElements, elementList

def BottomUpOptimalRemovalGameScore(numberOfElements, gameList):
    # Allocate the appropriate amount of memory for the memoization
    # memoizationList = [[0 for i in range(0, numberOfElements)] for j in range(0, numberOfElements)]
    memoizationList = numpy.zeros((5001, 5001))
    # This is the big time-suck. Runs in O(n^2), where n is the given number of elements in the given list.
    for distance in range(0, numberOfElements):
        for i in range(distance, numberOfElements):
            choices = [0,0,0]

            # i is already the last element of the sub-list.
            # Set j equal to the first element of the sub-list of size distance.
            j = i - distance

            # First and second players both choose front of list
            if ((j+2) <= (i)):
                choices[0] = memoizationList[j+2][i]
            # First player chooses front of list, second player chooses back of list.
            if ((j+1) <= (i-1)):
                choices[1] = memoizationList[j+1][i-1]
            # First and second players both choose back of list
            if ((j) <= (i-2)):
                choices[2] = memoizationList[j][i-2]
            # The optimal choice between i and j nets the max of either:
            memoizationList[j][i] = max(gameList[j] + min(choices[0], choices[1]), # The value of the j-th element in the game plus the lesser value of the second player's choices (since the second player will pick the option that carries greater value)
                                        gameList[i] + min(choices[1], choices[2])) # The value of the i-th element in the game plus the lesser value of the second player's choices (since the second player will pick the option that carries greater value)
    
    # Return the value of the optimal choice for the entire list.
    return memoizationList[0][-1]


def RecursiveOptimalRemovalGameScore(startIndex, stopIndex, gameList):
    if (stopIndex - startIndex == 1):
        # Choose the option (of the two choices) that contains the most points, as there is nothing else about which you need to worry.
        return max(gameList[startIndex], gameList[stopIndex])
    else:
        # Find the choice with the maximum number of points associated with all remaining elements given that your opponent will choose the next most optimal choice.
        memoizationArray[startIndex][stopIndex] = max(gameList[startIndex] + min(RecursiveOptimalRemovalGameScore(startIndex+2, stopIndex, gameList), RecursiveOptimalRemovalGameScore(startIndex+1, stopIndex-1, gameList)),
                                                        gameList[stopIndex] + min(RecursiveOptimalRemovalGameScore(startIndex, stopIndex-2, gameList), RecursiveOptimalRemovalGameScore(startIndex+1, stopIndex-1, gameList)))
        # Return the number of points associated with that choice.                                                
        return int(memoizationArray[startIndex][stopIndex])


if (__name__ == "__main__"):
    numberOfElements, elementList = ParseInput()
    print("Bottom-Up DP Removal Game Max Score: ")
    print(BottomUpOptimalRemovalGameScore(numberOfElements, elementList))
    print("\nRecursive DP Removal Game Max Score: ")
    print(RecursiveOptimalRemovalGameScore(0, numberOfElements - 1, elementList))

    
# d.) (Will be present in document...)
#
# e.) The runtime of this algorithm is O(n^2), where n == numberOfElements. This is because the for loops must iterate over each element, calculating the optimal solution for a sublist that expands to include each other element that appears later in the list than the first element.