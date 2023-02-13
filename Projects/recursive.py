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
                    Considering the recursive formulation, the state space o
                    the MDP in this problem can be represented by two variables,
                    the list of projects to be analyzed and the current day a
                    particular project ends that is initially set to zero. For
                    the list of projects, each project contains three values
                    (start_day, end_day, project_value).

                    The state space is actually a weighted interval scheduling
                    algorithm, which solves the problem of selecting a subset of
                    non-overlapping projects with maximum total value. The
                    algorithm recursively selects projects to attend, subject
                    to the constraint that no two attended projects overlap in
                    time. The weight of a project is interpreted as its reward,
                    which is to be maximized.

        Action Space:
                    The action space of the MDP in this problem consists of
                    picking or not picking a particular project. When picking
                    a project the function proceeds recursively by considering
                    two possible actions: attending the first project that ends
                    after the current time, or skipping that project and
                    attending the remaining projects. The maximum reward of the
                    two actions is returned as the value of the current state,
                    and is memoized.

                    When selecting the nth project each recursive call would
                    require a subset-project-list not containing the nth project,
                    and the nth project end day. Assuming a recursive call
                    determines another project (nth - 1) can start after the
                    initial nth-project-end-day, the algorithm adds the value of
                    the (nth -1) project to to the overall reward, then removes
                    (nth -1) project from the subset-project-list, providing the
                    reduced project-subset-list and original nth-project-end-day
                    for the next recursive action. The action space stops after
                    the subset-project-list has been completely iterated or
                    becomes empty.

                    Constants:
                        PROJECTS: A list of project tuples, [
                            (start, end_value),
                            (start, end, value)...
                        ]
                    Recursive Signature:
                        weighted_interval_scheduling(projects, current_day=0)
        Reward Space:
                    The reward space for this problem recursively selects projects
                    to attend, subject to the constraint that no two attended projects
                    overlap in time. The value of a project is interpreted as its
                    reward, which is to be maximized. The maximum reward of the two
                    actions, pick or not pick a particular project, becomes the edge
                    cost is returned as the value of the current state, and is memoized.


Recurrence and Memoization:
        This is a suffix problem where the algorithm would need to first work its way
        from the base case down to each leaf node, recursively returning the maximum
        reward for non-overlapping projects back to each parent node, eventually
        making it back to the base case to consider the the optimal sequence of of
        projects yielding the maximum value, subject to the constraint that no two
        attended projects overlap in time.

        The code defines a function called weighted_interval_scheduling which takes
        a list of projects, represented as tuples of start time, end time, and
        reward. The function expects the provided project list to be sorted by end
        time, so that the earliest ending projects are considered first. This is
        because if two projects have the same start time, attending the one that
        ends earlier maximizes the number of remaining projects that can be attended.

        The function then uses memoization to avoid redundant computation, by storing
        the maximum reward for each possible subset of remaining projects and each
        possible end time. This reduces the exponential time complexity of the
        algorithm to polynomial time.

        The function proceeds recursively by considering two possible actions: attending
        the first project that ends after the current time, or skipping that project and
        attending the remaining projects. The maximum reward of the two actions is
        returned as the value of the current state, and is memoized.

        Finally, the function returns the maximum reward for the full set of projects,
        which is the result of the algorithm. The HISTORY list keeps track of the
        sequence of states, actions, and rewards encountered during the execution of
        the algorithm, while the MEMO dictionary stores the maximum rewards for each
        encountered subset of projects and each possible end time.

Time Complexity:
        Considering the recursive implementation, the time complexity of the provided
        code is O(n^2) where n is the number of projects. This is because the algorithm
        uses recursion to consider all possible subsets of projects, and for each subset
        it checks if each project should be picked or not, which results in a total of
        n^2 recursive calls.

        The function then uses memoization to store the maximum reward for each possible
        subset of remaining projects and each possible end time. Since each subset has
        at most n projects, and each end time has at most n possible values, the number
        of possible combinations is O(n^2). For each combination, the function computes
        the maximum reward, which takes constant time. Thus, the total time spent on
        memoization is O(n^2).
"""
from pprint import pprint

# PROJECTS = [
#     (2, 4, 4), (3, 6, 6),
#     (6, 8, 2), (5, 7, 3),
# ]
# PROJECTS.sort(key=lambda x: x[1])
MEMO = {}
HISTORY = []


def weighted_interval_scheduling(projects, current_day=0):

    # projects.sort(key=lambda x: x[1])

    # memoization key
    key = f'{str(["".join(str(line)) for line in projects])}, {current_day}'

    # return previous computation
    if key in MEMO:
        return MEMO[key]

    # base case: No more projects to consider
    if not projects:
        return 0

    # find the first project after current day
    i = 0
    while i < len(projects) and projects[i][0] <= current_day:
        i += 1

    # Recursive case: Try attending the next project and the rest of the projects after it
    if i < len(projects):
        project_start, project_end, project_reward = projects[i]

        # next subset of projects to recurse
        subset_projects = projects[i+1:]

        # action: consider picking the project
        pick = project_reward + weighted_interval_scheduling(subset_projects, project_end)

        # action: consider the next project instead
        not_pick = weighted_interval_scheduling(subset_projects, current_day)

        maximum_value = max(pick, not_pick)

        # memoize the computations
        p = str(["".join(str(line)) for line in subset_projects])
        MEMO[f'{p}, {project_end}'] = pick
        MEMO[f'{p}, {current_day}'] = not_pick

        HISTORY.append(
            {
                f'current_project': projects[i],
                f'current_day': current_day,
                f'picked: {projects[i+1:]}, project_end: {project_end}': pick,
            }
        )

        HISTORY.append(
            {
                f'current_project': projects[i],
                f'current_day': current_day,
                f'not_picked: {projects[i+1:]}, current_day: {current_day}': not_pick,
            }
        )

        HISTORY.append({'maximum_value': maximum_value})
        return maximum_value
    else:
        return 0


# max_value = weighted_interval_scheduling(PROJECTS)
# pprint(HISTORY)
# print(max_value)
# pprint(MEMO)
