"""
Akhil Nagubandi, Wichita State University, S839S984

Problem:-
        There is money system containing n coins. Each
        coin has a certain positive face value. Using the minimum number
        of coins, need to produce the sum x.


This problem can be sloved by Reinforcement learning as the goal
is the maximize the expected rewards using minimmum resources. In this case, using 
minimun number of coins produce a maximum sum.

Markov Decision process:-
    State spcae:
                The state space for this problem can be defined as all possible
                sums that can be made using the coins. The varibales used for the
                subproblem are the number of coins 'n' and required sum 'x' and value
                of the coins.
    Action space:
                The action space for this problem is the set of coins available.
                eg- {1,5,7} for the given
    Reward spcae:
                The reward space would be number of coins used. If no sum can
                be made using the coins, then zero reward. Greter than zero if the sum can be made.

Recurrence and Memoization:
        This is not a suffix, prefix, substring problem as the goal is to find the minimum
        noumber of coins to make a sum of money x.
        
        We can consider this as a optimization
        problem and this involves breaking the problem into smaller sub problems and solving them
        in a bottom up manner.

        A recurrence relation is a mathematical equation that defines a sequence recursively in
        terms of its previous terms. In this situation we can define it as minimum of coins we 
        require to produce a sum.

        C[x] = Min(C[x], C[x-v] + 1)
        where C[x] =  minimum number of coin
                x  =  Desired sum
                v  =  Value of given coin

        Memoization is a technique for improving the performance of recursive
        algorithms by storing the results of expensive function calls and
        returning the cached result when the same inputs occur again.

        In this problem, memoization can be used to store the results of calls which are used to 
        find the minimum number of coins needed to make a sum x.

Time Complexity
        The time complexity of this code is O(n x), where n is the number of
        coins and x is the desired sum. This is because the inner loop (j) iterates through all the
        suns (1 to x ), and the outer loop (i) iterates through
        all the coins (1 to n).

Problem graph:
        The graph for this problem can be drawn using a directed acyclic graph (DAG). 
        The nodes of the graph represent the sums that can be made using the available 
        coins. The edges of the graph represent the transitions from one sum to another and 
        are labeled with the value of the coin used for the transition. For example,
        if the coins are {1, 5, 7} and the desired sum is 11, then the graph will have the following nodes and edges:

        Nodes: 1, 5, 7, 11

        Edges: (1, 5) with label 1, (1, 7) with label 5, (5, 11) with label 7.
"""
def minCoins(coins, n, x):
 
    # base case
    if (x == 0):
        return 0
 
    # Initialize result
    res = float('inf')
     
    # Try every coin that has smaller value than V
    for i in range(0, n):
        if (coins[i] <= x):
            sub_res = minCoins(coins, n, x-coins[i])
 
            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != float('inf') and sub_res + 1 < res):
                res = sub_res + 1
 
    return res
 
# Driver program to test above function
coins = [1,5,7]
n = len(coins)
x = 11
print("Minimum coins required is",minCoins(coins, n, x))
