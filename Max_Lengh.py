# Problem
# You are given two arrays A and B, of length N. You can select any subarray and then sort the elements in ascending order of that subarray for arrays A and B.
# Find the minimum length of the subarray you can choose to make A and B same after performing the operation. A and B are permutations of each other.
# Input Format:
# • The first line contains an integer T denoting the number of test cases.
# • The first line of each test case contains an integer N.
# • The next line of each test case contains N space-separated integers, elements of array A.
# • The next line of each test case contains N space-separated integers, elements of array B.
# Output Format:
# For each test case, print the minimum length of the subarray you can choose to make A and B same after performing the operation.
# Constraints:
# 1<T<10
# 1 ≤ N ≤ 105
# 1≤ A[i], B[i] ≤ 105
# Writing output to STDOUT

# Function to determine the minimum length of subarray to sort
def min_length_to_sort_subarray(T, test_cases):
    results = []

    for t in range(T):
        N = test_cases[t][0]
        A = test_cases[t][1]
        B = test_cases[t][2]

        # Find the first mismatch from the left
        left = 0
        while left < N and A[left] == B[left]:
            left += 1

        # Find the first mismatch from the right
        right = N - 1
        while right >= 0 and A[right] == B[right]:
            right -= 1

        # If the arrays are already equal
        if left >= right:
            results.append(0)
        else:
            # Length of the subarray to sort
            min_length = right - left + 1
            results.append(min_length)

    return results

def main():
    # This would be used in a competitive programming setup
    # import sys
    # input = sys.stdin.read
    # data = input().split()

    # Example of hardcoded inputs for testing
    data = """
    2
    5
    4 3 1 2 5
    1 2 3 4 5
    5
    1 2 3 4 5
    1 2 3 4 5
    """.strip().split()

    T = int(data[0])
    index = 1
    test_cases = []

    for _ in range(T):
        N = int(data[index])
        index += 1
        A = list(map(int, data[index:index + N]))
        index += N
        B = list(map(int, data[index:index + N]))
        index += N
        test_cases.append((N, A, B))

    # Calculate the results
    results = min_length_to_sort_subarray(T, test_cases)

    # Output the results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
