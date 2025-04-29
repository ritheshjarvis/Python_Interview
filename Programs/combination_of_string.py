def get_combinations(s):
    combinations = []

    def generate_combinations(prefix, remaining):
        if remaining:
            for i in range(len(remaining)):
                new_prefix = prefix + remaining[i]
                combinations.append(new_prefix)
                generate_combinations(new_prefix, remaining[i + 1:])

    for i in range(len(s)):
        generate_combinations("", s[i:])

    return combinations


# Example usage
input_string = "abc"
result = get_combinations(input_string)
print(result)
