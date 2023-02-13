"""
Kyle Lanier, Wichita State University, 2/4/2023

Problem:
        There are n projects you can attend. For each project,
        you know its starting and ending days and the amount of
        money you would get as reward. You can only attend one
        project during a day.

        Note: Project end days are considered working days,
              hence a project cannot start on the same day
              another project ends.

        What is the maximum amount of money you can earn?

Markov Decision Process (MDP):
        State Space:
                    The state space of the MDP in this problem can be
                    represented by the current day and the set of projects that
                    have not been started or completed yet. For example, state
                    (day=5, {1, 2, 4}) represents the 5th day and projects 1, 2,
                    and 4 have not been started or completed yet.
        Action Space:
                    The action space of the MDP in this problem would be the
                    choice of the project to start at each day. For example,
                    actions could be to start project 1, 2, or 4.
        Reward Space:
                    The reward space of the MDP in this problem would be the
                    reward associated with starting a project. For example, a
                    reward of 50 for starting project 1, a reward of 100 for
                    starting project 2, etc. The objective is to maximize the
                    total reward.

Recurrence and Memoization:
        This is not a suffix, prefix, or substring problem where the goal is
        to find certain patterns in strings, which have nothing to do with
        finding the maximum reward from a list of projects.

        In suffix, prefix, and substring problems, the goal is to find
        substrings within a given string that match certain patterns. For
        example, in a suffix problem, the goal might be to find the longest
        common suffix of two strings. In a prefix problem, the goal might be
        to find the longest common prefix of two strings. In a substring
        problem, the goal might be to find the longest common substring of
        two strings.

        The problem of finding the maximum reward from a list of projects is
        an optimization problem, specifically a dynamic programming problem,
        where the goal is to find the optimal solution to a given problem by
        breaking it down into smaller sub-problems and solving them in a
        bottom-up manner.

        A recurrence relation is a mathematical equation that defines a
        sequence recursively in terms of its previous terms. In the case of
        finding the maximum reward from a list of projects, a recurrence
        relation could be used to describe the maximum reward that can be
        earned for a certain range of projects, given the start and end days
        and the reward for each project.

        Memoization is a technique for improving the performance of recursive
        algorithms by storing the results of expensive function calls and
        returning the cached result when the same inputs occur again. In this
        problem, memoization could be used to store the results of the maximum
        reward for a given range of projects, so that the same calculation is
        not repeated multiple times.

Context:
        This problem is known as the "Weighted Interval Scheduling Problem"
        and can be solved using dynamic programming. The idea is to sort the
        intervals in decreasing order of their end time and then select the
        intervals such that no two intervals overlap. The maximum reward that
        can be earned is the sum of rewards of the selected non-overlapping
        intervals.

Pseudocode:
        1) Sort the intervals in decreasing order of their end time.
        2) Initialize an array dp[] with all values as 0.
        3) For each interval, do the following:
           a. Find the maximum value of j such that the end time of interval
              j is less than the start time of the current interval i.
           b. dp[i] = max(dp[i], dp[j] + reward for interval i).
           4) Return the maximum value in dp[].

Time Complexity:
        The time complexity of this code is O(n^2), where n is the number of
        projects. This is because the inner loop (j) iterates through all the
        previous projects (0 to i-1), and the outer loop (i) iterates through
        all the projects. In the worst case scenario, this will result in
        n * (n-1) / 2 comparisons, leading to a time complexity of O(n^2).
"""
from copy import deepcopy


def weighted_interval_scheduling(num_projects, projects):
    """Returns the maximum reward that can be earned
    for selecting non-overlapping projects.

    Args:
        num_projects int: the number of projects
        projects list(tuple):
            tuple(int, int, int):
                - starting_day
                - end_day
                - reward_money

    Returns:
        int: The maximum value in dp[]
    """

    # sort intervals by end day
    projects.sort(key=lambda x: x[1])

    dp = [0] * num_projects
    table = []
    # initialize the first interval's reward
    dp[0] = projects[0][2]

    iteration = 0
    for i in range(1, num_projects):

        # initialize with the reward of the current interval
        dp[i] = projects[i][2]

        for j in range(i):

            # find the maximum reward for non-overlapping projects
            # Note: use '<' if end days are working days
            # Note: use '<=' if end days are not working days
            if projects[j][1] < projects[i][0]:
                dp[i] = max(dp[i], dp[j] + projects[i][2])

                iteration += 1
                item = {
                    "iteration": iteration,
                    "i": i,
                    "j": j,
                    f'dp[{i}]': dp[i]
                }
                table.append(deepcopy(item))

    return max(dp)
