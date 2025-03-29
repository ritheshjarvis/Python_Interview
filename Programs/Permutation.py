def permutations(s):
    n = len(s)
    s = list(s)  # Convert string to list for swapping
    stack = [(0, s[:])]  # Stack stores (index, current permutation)

    while stack:
        left, arr = stack.pop()
        if left == n - 1:
            print("".join(arr))  # Print when at last position
        else:
            for i in range(left, n):
                arr[left], arr[i] = arr[i], arr[left]  # Swap
                stack.append((left + 1, arr[:]))  # Push new state to stack
                arr[left], arr[i] = arr[i], arr[left]  # Backtrack

# Example usage
input_str = "ABC"
permutations(input_str)