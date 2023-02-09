"""
Chun Yu Lim, Wichita State University, 2/6/2023

Problem:
        The edit distance between two strings is the minimum number 
        of operations required to transform one string into the other.

        The allowed operations are:
            Add one character to the string.
            Remove one character from the string.
            Replace one character in the string.

        For example, the edit distance between LOVE and MOVIE is 2, because you can first replace L with M, and then add I.

        Your task is to calculate the edit distance between two strings.

Markov Decision Process (MDP):
        State Space:
                    The state space of the MDP in this problem can be
                    represented by the string indexes. For example, (1, 0),
                    where 1 is the index for first string and 0 is the index
                    for second string at that state.
        Action Space:
                    The action space of the MDP in this problem would be
                    the choice of adding, removing or replacing one character 
                    at each state. For example, actions could be adding an
                    alphabet into string 1 to tranform it into string 2.
        Reward Space:
                    The reward space of the MDP in this problem would be
                    the cost required to edit the string. Each action will 
                    have the same cost. The objective is to minimize the 
                    total cost (maximize the reward) to transform one 
                    string into another.

Recurrence and Memoization:
        
        This is a suffix problem where we decide to perform any operation (add, remove, replace)
        at a time and delegate the rest of the decision to the next recurrence.
        
        The base case for this problem is when all alphabets are being compared, 
        stop the recurrence and return the minimum cost to achieve the solution.
"""



import numpy as np
str = "LOVE"
target = "MOVIE"
memo = [[-1 for x in range(1000)] for x in range(1000)]

def EditDist(a, b):
    #Top down/recursive approach
    if memo[a][b] != -1:
      return memo[a][b]

    if a == 0:
      return b

    if b == 0:
      return a

    if str[a-1] == target[b-1]:
      return EditDist(a-1, b-1)

    add = EditDist(a, b-1)
    remove = EditDist(a-1, b)
    replace = EditDist(a-1, b-1)

    value = 1 + min(add, remove, replace)
    memo[a][b] = value

    return value


print('Top down solution: ', EditDist(len(str),len(target)))

def EditDistDP():
    #Bottom up approach
    dp = [[0 for x in range(len(target)+1)] for x in range(len(str)+1)]
    for i in range(len(str)+1):
        for j in range(len(target)+1):
            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif str[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]
            
            else:
                add = dp[i][j-1]
                remove = dp[i-1][j]
                replace = dp[i-1][j-1]
                dp[i][j] =  1 + min(add, remove, replace)

    return dp[len(str)][len(target)]

print('Bottom up solution:', EditDistDP())

"""
Time Complexity:
        This algorithm runs in O(a*b), where a is the length of string and 
        b is the length of target string. The code has two nested loops: 
        the outer loop iterates through all possible substring in string. 
        The inner loop iterates through all possible substring in target 
        string to determine how many operation is needed to transform the 
        string into target string.
"""
