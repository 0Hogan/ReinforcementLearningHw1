""""
Arannya Saha, Wichita State University, 2/8/2023

Problem
    Increasing Subsequence
        
"""


def increasing_subsequence(n, nums):
    memos = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                memos[i] = max(memos[i], memos[j] + 1)
    return max(memos)


def take_input():
    n = int(input())
    array = [int(x) for x in input().split()]
    return n, array


if __name__ == "__main__":
    # number_of_elements, elements = take_input()
    number_of_elements = 8
    elements = [7, 3, 5, 3, 6, 2, 9, 8]
    # number_of_elements = 10
    # elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(increasing_subsequence(number_of_elements, elements))

'''
Time Complexity:
        The time complexity of this code is O(n * n). This because we are iterating
        through each element and comparing sub-arrays of length equal to the index
        of that element.
'''
