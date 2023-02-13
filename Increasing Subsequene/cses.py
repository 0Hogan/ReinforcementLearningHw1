def increasing_subsequence(n, nums):
    memos = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                memos[i] = max(memos[i], memos[j] + 1)
    return max(memos)


def take_input():
    n = int(input())
    array = array = [int(x) for x in input().split()]
    return n, array


if __name__ == "__main__":
    number_of_elements, elements = take_input()
    print(increasing_subsequence(number_of_elements, elements))
