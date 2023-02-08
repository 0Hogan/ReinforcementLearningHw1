"""
Chun Yu Lim, Wichita State University, 2/6/2023

Problem:
        You are in a book shop which sells n different books. 
        You know the price and number of pages of each book.

        You have decided that the total price of your purchases will be at most x. 
        What is the maximum number of pages you can buy? You can buy each book at most once.

Markov Decision Process (MDP):
        State Space:
                    The state space of the MDP in this problem can be
                    represented by the book ID and the current price. 
                    For example, (1, 5), where 1 is the book ID
                    and 5 is the current price at that state.
        Action Space:
                    The action space of the MDP in this problem would be
                    the choice of picking or not picking the book at each
                    state. For example, actions could be picking book 1
                    and increase the current price to 5 or not picking 
                    book 1 and maintain the current price.
        Reward Space:
                    The reward space of the MDP in this problem would be
                    the cost or reward associated with page count while
                    making each decision. For example, picking book 1 will
                    get a reward of 5 or not picking book 1 will get a
                    reward of 0. The objective is to maximize the total
                    reward without exceeding the price limit.

Recurrence and Memoization:
        
        This is a prefix problem where we decide to pick or not to pick 1 book
        at a time and delegate the rest of the decision to the next recurrence.
        
        The base case for this problem is when there is no book left to pick, 
        stop the recurrence and return the current price.
"""



import numpy as np
page = [5, 12, 8, 1]   
price = [4, 8, 5, 3]
max_cap = 10

def BookShop(id, current_pr):
    #Top down/recursive approach
    if id == 4:
      return 0
    
    value_for_pick = 0
    if current_pr + price[id] <= max_cap:
        #pick
        value_for_pick = page[id] + BookShop(id+1, current_pr = current_pr + price[id])
    #do not pick
    value_for_not_pick = BookShop(id+1, current_pr = current_pr)
    
    value = max(value_for_pick, value_for_not_pick)

    return value

print('Top down solution: ', BookShop(0,0))

def BookShopDP():
    #Bottom up approach
    dp = [[0 for x in range(max_cap+1)] for x in range(len(page)+1)]
    for i in range(0, len(page)+1):
        for j in range(0, max_cap+1):
            if i == 0 or j == 0:
                dp[i][j] = 0

            elif j >= price[i-1]:
                dp[i][j] = max (dp[i-1][j],dp[i-1][j-price[i-1]] + page[i-1])

            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(page)][max_cap]

print('Bottom up solution:', BookShopDP())

"""
Time Complexity:
        This algorithm runs in O(n*max_cap), where n is the number of books.
        The code has two nested loops: the outer loop iterates through all
        possible price capacity.The inner loop iterates through each book 
        to determine if the book should be included in the current subset.
"""
