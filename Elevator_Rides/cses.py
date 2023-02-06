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
                    The state space of the MDP in this problem can be
                    represented by all possible combinations of people
                    and their weights in the elevator at a given time.
                    For example, (3, 100), where 3 is the number of
                    people and 100 is the total weight of the people in
                    the elevator at that state.
        Action Space:
                    The action space of the MDP in this problem would be
                    the choice of the number of people to pick up or drop
                    off at each floor. For example, actions could be to
                    pick up 1, 2, or 3 people or to drop off 1, 2, or 3
                    people.
        Reward Space:
                    The reward space of the MDP in this problem would be
                    the cost or reward associated with transporting the
                    people from one floor to another. For example, a
                    reward of -1 for each ride of the elevator or a reward
                    of -10 for each ride that exceeds the maximum weight
                    capacity of the elevator. The objective is to minimize
                    the total cost or maximize the total reward.

Recurrence and Memoization:R
        This is not a suffix, prefix, or substring problem where the goal is
        to find certain patterns in strings, which have nothing to do with
        finding the minimum number of rides required to transport people in
        an elevator.

        In suffix, prefix, and substring problems, the goal is to find
        substrings within a given string that match certain patterns. For
        example, in a suffix problem, the goal might be to find the longest
        common suffix of two strings. In a prefix problem, the goal might be
        to find the longest common prefix of two strings. In a substring
        problem, the goal might be to find the longest common substring of
        two strings.

        The problem of finding the minimum number of rides required to transport
        people in an elevator is an optimization problem, specifically a dynamic
        programming problem, where the goal is to find the optimal solution to a
        given problem by breaking it down into smaller sub-problems and solving
        them in a bottom-up manner.

        A recurrence relation is a mathematical equation that defines a sequence
        recursively in terms of its previous terms. In the case of finding the
        minimum number of rides required to transport all people, a recurrence
        relation could be used to describe the minimum number of rides needed to
        transport a certain number of people, given the maximum weight of the
        elevator and the weight of each person.

        Memoization is a technique for improving the performance of recursive
        algorithms by storing the results of expensive function calls and
        returning the cached result when the same inputs occur again. In this
        problem, memoization could be used to store the results of the minimum
        number of rides for a given number of people, so that the same calculation
        is not repeated multiple times.

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
        This algorithm runs in O(2^n * n), where n is the number of people.
        The code has two nested loops: the outer loop iterates through all
        the subsets of people represented as bit-masks, which has a total of
        2^n subsets. The inner loop iterates through each person to determine
        if the person should be included in the current subset.

        Since each iteration of the inner loop takes constant time, the overall
        time complexity is O(2^n * n).
"""
import sys


def minimum_elevator_rides(num_people, max_weight, person_wts):
    """Finds the minimum number of rides required to transport
    all the people from one floor to another.

    Args:
        num_people int: number of people needing an elevator
        max_weight int: maximum weight the elevator can hold
        person_wts list(int): the weight of each person

    Returns:
        int: The minimum number of elevator rides in dp[]
    """

    # uses bit-masking, if n == 4
    # bit_mask-0 == (1 << 0) ==  0001
    # bit_mask-1 == (1 << 1) ==  0010
    # bit_mask-2 == (1 << 2) ==  0100
    # bit_mask-3 == (1 << 3) ==  1000
    # bit_mask-n == (1 << 4) == 10000 == 2^n
    # 2^n == maximum number of subsets for a set of size n
    num_subsets = 1 << num_people

    # dp is an array used to store the minimum
    # number of rides for each subset
    dp = [{}] * num_subsets

    # base case = empty elevator ride
    dp[0] = {
        "num_rides": 1,
        "ride_wt": 0
    }

    # calculate bottom-up solution
    for current_mask in range(1, num_subsets):
        best_result = {
            "num_rides": sys.maxsize,
            "ride_wt": sys.maxsize
        }

        for person in range(num_people):
            # convert person to a bit-mask
            person_bit_mask = 1 << person

            # if the person matches the current bit-mask
            if bool(person_bit_mask & current_mask):

                subset = dp[
                    # ^ is Binary XOR which sets each position to 1 if
                    # only one of the bits is 1, but will be 0 if both
                    # are 0 or both are 1
                    person_bit_mask ^ current_mask
                ]

                # if the person's weight is less than
                # the available weight capacity for
                # the given subset of people in the
                # elevator
                if subset['ride_wt'] + person_wts[person] <= max_weight:
                    # let the person in the elevator with the other people
                    subset['ride_wt'] += person_wts[person]
                else:
                    # let the person enter the next elevator
                    subset['num_rides'] += 1
                    subset['ride_wt'] = person_wts[person]

                best_result['num_rides'] = min(
                    best_result['num_rides'],
                    subset['num_rides']
                )

                best_result['ride_wt'] = min(
                    best_result['ride_wt'],
                    subset['ride_wt']
                )

        dp[current_mask] = best_result

    # bottom-up solution returns the value
    # of the last subset in the dp array
    return dp[num_subsets - 1]['num_rides']


if __name__ == "__main__":
    print(
        minimum_elevator_rides(
            4,            # num_people,
            10,           # max_weight
            [4, 8, 6, 1]  # person_wts
        )
    )
