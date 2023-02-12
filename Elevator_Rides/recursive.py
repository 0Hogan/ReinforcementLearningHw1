"""
Kyle Lanier, Wichita State University, 2/4/2023

Problem:
        There are n people who want to get to the top of a
        building which has only one elevator. You know the
        weight of each person and the maximum allowed weight
        in the elevator.

        What is the minimum number of elevator rides?

Markov Decision Process (MDP):
        State Space:
        Considering the recursive formulation, the state space of the MDP in
        this problem can be represented by three variables, such as the number
        of people needing an elevator ride, the current cost representing the
        number of elevator rides taken, and the current elevator weight.

        Action Space:
        The action space of the MDP in this problem would be the choice of
        picking or not picking a person who is waiting for an elevator ride.
        If there are three people for example, the starting action could be to
        pick up p1 (adding the weight of p1 to the current elevator) or to not
        pick up p1, the action for the second state could be to pick up p2
        (adding the weight of p2 to the current elevator) or to not pick up p2,
        and the final state could pick up p3 (adding the weight of p3 to the
        current elevator) or to not pick up p3.

        Using the list of people weights [9, 1, 2] and maximum elevator weight (10)
        as constants, each recursive call would require the number_of_people,
        current_elevator_weight, and current_cost. Each recursive iteration would
        be called with one less person, the current elevator weight for people
        who’ve been picked, and the current cost for the number of elevator rides
        needed along the recursive sequence.

        Constants:
            MAX_WEIGHT as the maximum elevator weight capacity
            PEOPLE WEIGHTS as the weight for each person
        Recursive Signature:
            min_elevator_rides(num_people, current_elevator_weight, cost)

Reward Space:
        The reward space for this problem would be the cost for the number of
        rides needed to move all the people. With a recursive base cost starting
        at 0, if adding a person is within the current available elevator capacity
        the cost would stay the same. However, if adding a person would fill or
        exceed the remaining capacity, the cost would increment by 1 to account
        for the use of an elevator ride.

        When there are no more actions to take, as in the case after each person
        has been picked or not picked, each leaf node in the graph would contain
        the total cost for the number of rides needed for the sequence of actions
        leading to the particular leaf node. Then, the reward space would
        recursively return the maximum reward between pick and not_pick as the
        edge cost, starting from the leaf nodes to each parent node, allowing each
        parent node to select the most efficient action for any given state,
        ultimately returning the optimal solution for the minimum number of
        elevator rides needed to transport ‘n’ people.


Recurrence and Memoization:R
        This is a suffix problem where the algorithm would need to first work its
        way from the base case down to each leaf node, recursively returning the
        number of elevator rides taken back to each parent node, eventually making
        it back to the base case to consider the the optimal solution for the
        minimum number of elevator rides needed to transport ‘n’ people.

        The python code below implements a recursive function minimum_elevator_rides
        that finds the minimum number of elevator rides required to transport N
        people, where each person has a specific weight specified in the list WEIGHTS,
        and the maximum capacity of the elevator is MAX_WEIGHT.

        The function uses memoization to optimize its runtime. Memoization is a
        technique where the function stores the result of its computation for a
        specific input so that it can avoid recomputing the same input again in the future.

        The function uses a recurrence relation to compute the result. The base case
        is when n is 0, in which case it returns the cost. The function recursively
        calls itself twice - once by considering not picking the nth person and once
        by picking the nth person.

        If the weight of the nth person is less than or equal to the remaining capacity
        of the elevator, the function picks that person and increments the current weight
        of the elevator by the weight of the nth person. It then calls itself recursively
        with one less person, the updated current weight of the elevator, and the
        same cost. If the weight of the nth person is greater than the remaining
        capacity of the elevator, the function increases the current cost by one to
        account for the start of a new elevator, adds the weight of the nth person to
        the new elevator, and recursively calls the function with the one less person,
        the updated cost, and the weight of the elevator now containing just the nth person.

        The result of the function is the maximum result between both actions, pick
        or not_pick, actions, which are stored in the MEMO dictionary. The final result
        is the minimum number of elevator rides required to transport all N people,
        which is printed at the end of the code.


Context:
        This code is solving the minimum elevator rides problem
        using a dynamic programming approach with bit-masking.
        Given the number of people, maximum weight of the elevator,
        and the weight of each person, it finds the minimum number
        of rides required to transport all the people from one floor
        to another.

Pseudocode:
        1) The maximum number of subsets is 2^n for a set of size n.
        2) Use a dp array to store the minimum number of rides for each subset.
        2) Start with a base case that is an empty elevator ride.
        2) Iterate through each subset of people and update the dp array.
        3) For each person, do the following:
           a. If the current elevator weight plus the weight of the person
              does not exceed the maximum weight, add the person's weight.
           b. If the current elevator weight plus the weight of the person
              exceeds the maximum weight the the person catches the next ride
              increment number of elevator rides and set the weight of the
              next elevator to the weight of the new person.
        5) As a bottom-up solution return the last value of the dp array.

Time Complexity:
        The recursive implementation is dependent on the size of the input
        array WEIGHTS. Specifically, the time complexity of the code is
        exponential, O(2^N), where N is the length of WEIGHTS. This is
        because the function minimum_elevator_rides() is called recursively
        twice at each step, which results in a binary tree of recursive calls
        with a depth of N. Additionally, memoization is used to avoid
        duplicate recursive calls and reduce the number of computations,
        but this only reduces the constant factor and does not affect the
        overall time complexity.
"""

HISTORY = []
MEMO = {}
MAX_WEIGHT = 10
WEIGHTS = [4, 8, 6, 1]
N = len(WEIGHTS)


def minimum_elevator_rides(n, current_weight=0, cost=0):

    # if we've previously done the calculation
    if f'p{n}, {cost}, {current_weight}' in MEMO:
        return MEMO[f'p{n}, {cost}, {current_weight}']

    # corner case, everyone fits in one elevator
    if sum(WEIGHTS) <= MAX_WEIGHT:
        return 1

    # terminal recursive condition
    if n == 0:
        return cost

    # consider not picking the person
    not_pick = minimum_elevator_rides(n-1, current_weight, cost)
    MEMO[f'p{n}, {cost}, {current_weight}'] = not_pick
    HISTORY.append(f'p{n}, {cost}, {current_weight} = {not_pick}')

    capacity = MAX_WEIGHT - current_weight
    persons_weight = WEIGHTS[n - 1]
    pick_weight = 0

    # if persons weight <= elevator capacity
    if persons_weight <= capacity:

        # add the person to the elevator at no additional cost
        pick_weight = current_weight + persons_weight

        # if persons weight fills remaining elevator capacity
        if persons_weight == capacity:

            # elevator is 100% full and needs to go
            # costs 1 for sending the elevator
            cost = cost + 1

    # persons weight exceeds the available elevator capacity
    elif persons_weight > capacity:
        # costs 1 for sending the elevator with the current people
        cost = cost + 1

        # new elevator now has the weight of person n
        pick_weight = WEIGHTS[n - 1]

    pick = minimum_elevator_rides(n-1, pick_weight, cost)
    MEMO[f'p{n}, {cost}, {pick_weight}'] = pick
    HISTORY.append(f'p{n}, {cost}, {pick_weight} = {pick}')

    return max(pick, not_pick)


# print(minimum_elevator_rides(N))
# print(HISTORY)
# print(MEMO)
