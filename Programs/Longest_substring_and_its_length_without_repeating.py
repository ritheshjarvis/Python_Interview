def longest_substring_without_repeating(s: str) -> tuple:
    start = 0                # Start index of the current window
    max_len = 0              # Maximum length found so far
    best_substring = ""      # The longest substring without repeating characters
    used_chars = {}          # Dictionary to store the last seen index of each character

    for i, ch in enumerate(s):
        # If the character is found in the current window, move the start next to its last occurrence.
        if ch in used_chars and used_chars[ch] >= start:
            start = used_chars[ch] + 1
        # Record/update the last seen index of the current character.
        used_chars[ch] = i

        # Calculate current window length
        current_len = i - start + 1
        if current_len > max_len:
            max_len = current_len
            best_substring = s[start:i + 1]
    print(used_chars)
    return max_len, best_substring

if __name__ == "__main__":
    s = input("Enter a string: ")
    length, substring = longest_substring_without_repeating(s)
    print("Length of the longest substring without repeating characters:", length)
    print("Longest substring without repeating characters:", substring)
