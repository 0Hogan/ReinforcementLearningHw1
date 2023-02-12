from pprint import pprint

PROJECTS =  [
    (2, 4, 4), (3, 6, 6),
    (6, 8, 2), (5, 7, 3)
]

def weighted_interval_scheduling(projects, current_day=0):

    # intervals by end day
    projects.sort(key=lambda x: x[1])

    # base case: No more projects to consider
    if not projects:
        return 0
    
    # find the first project that can be attended on or after the current day
    i = 0
    while i < len(projects) and projects[i][0] < current_day:
        i += 1
    
    # Recursive case: Try attending the next project and the rest of the projects after it
    if i < len(projects):
        project_start, project_end, project_reward = projects[i]
        return max(
            project_reward + weighted_interval_scheduling(projects[i+1:], project_end),
            weighted_interval_scheduling(projects[i+1:], current_day))
    else:
        return 0

weighted_interval_scheduling(PROJECTS)