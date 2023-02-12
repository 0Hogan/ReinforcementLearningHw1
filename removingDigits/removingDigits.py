"""
Akhil Nagubandi, Wichita State University, S839S984

Problem:-

        There is a integer n, on each step we are asked to subtracts one of the digit value.
        Need to find the minimum number of steps in order to reduce the number to zero.


This problem can be sloved by Reinforcement learning as the goal
is the maximize the expected rewards using minimmum resources. In this case, the agent receives
rewards on making the number zero. The best reward is achieved by minimizing the number of actions.

Markov Decision process:-
    State spcae:
                The state space for this problem can be defined as the intervel between 0 and
                the integer [0,n]. The varibales used for the
                subproblem are the integer n, value of the digit being subtracted d, and minimum 
                number of steps to reduce the number to zero minSteps.
    Action space:
                The action space for this problem is the set of all possible values of digits 
                that can be subtracted.
    Reward spcae:
                The reward space would be either 1 or 0. If the current is 0, reward is 1 and else 
                reward id zero.

Recurrence and Memoization:
        This is not a suffix, prefix, substring problem as the goal is to find the minimum
        number of steps to reduce the number to zero.
        
        We can consider this as a optimization problem and this involves breaking the 
        problem into smaller sub problems and solving them in a bottom up manner. For this scenario,
        small subproblems would involve subtracting one of the values of the digit from the current number 
        and calculating the minimum nuber of steps needed to make it zero. But the larger problem is taking 
        account of all possible states.  

        A recurrence relation is a mathematical equation that defines a sequence recursively in
        terms of its previous terms. In this situation we can define it as minimum of steps needed to
        reduce the numbe to zero while subtracting one of the value of a digit on each step.

        dp[i] = min(dp[i],
                        dp[i - int(str(i)[j])] + 1)
                   
        where dp[i] is the minimum steps required to reduce number i to zero
        int(str(i)[j]) is the jth digit in the number i.

        Memoization is a technique for improving the performance of recursive
        algorithms by storing the results of expensive function calls and
        returning the cached result when the same inputs occur again.

        In this problem, memoization can be used to store the minimum no of steps to reduce to zero
        each state.

Time Complexity
        The time complexity of this code is O(n^2), where n is the number given. This is because
        there are two nested loops which go through each of n action and n possible states.

Problem graph:
        The nodes of the graph are the states and the edges are the actions. The rewards 
        are represented by arrows pointing from the current state to the next state. 
        The policy is represented by arrows pointing from each state to the state that results 
        in the minimum number of steps required to make the number equal to 0.
"""
#  minimum number of steps required to make the number equal to 0.
def reduceZero(N):
     
    # Initialise dp[] to steps
    dp = [float('inf') for i in range(N + 1)]
 
    dp[0] = 0
 
    # Iterate for all elements
    for i in range(N + 1):
         
        # For each digit in number i
        for j in range(len(str(i))):
            # Subtract the digit from the number
            dp[i] = min(dp[i],
                        dp[i - int(str(i)[j])] + 1)
 
    # dp[N] will give minimum
    # step for N
    return dp[N]

print(reduceZero(27))
