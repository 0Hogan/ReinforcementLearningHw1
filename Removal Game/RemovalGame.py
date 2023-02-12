
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

def OptimalRemovalGameScore(numberOfElements, gameList):
    # Allocate the appropriate amount of memory for the memoization
    memoizationList = [[0 for i in range(0, numberOfElements)] for j in range(0, numberOfElements)]

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

if (__name__ == "__main__"):
    numberOfElements, elementList = ParseInput()
    print(OptimalRemovalGameScore(numberOfElements, elementList))