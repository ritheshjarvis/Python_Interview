from itertools import permutations, combinations

def string_permutations(s):
    perm = [''.join(p) for p in permutations(s)]
    return perm

def string_combinations(s):
    comb = []
    for r in range(1, len(s) + 1):
        comb.extend([''.join(c) for c in combinations(s, r)])
    return comb

# Example usage
s = "ABC"
#
# print("Permutations:", string_permutations(s))
# print("Combinations:", string_combinations(s))
for p in combinations(s):
    print(p)