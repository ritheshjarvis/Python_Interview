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

# https://www.youtube.com/watch?v=wiGpQwVHdE0
class Solution:
    def lenOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        _max = 0

        for right in range(len(s)):
            # print(right)
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            _max = max(_max, len(char_set))
        return _max, char_set

    def lenOfLongestSubstring1(self, s: str) -> tuple:
        char_set = set()
        left = 0
        _max = 0
        start = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            if right - left + 1 > _max:
                _max = right - left + 1
                start = left

        return _max, s[start:start + _max]



max_, char_set_ = Solution().lenOfLongestSubstring1('abcafg')
print(max_, char_set_)

if __name__ == "__main__":
    s = input("Enter a string: ")
    length, substring = longest_substring_without_repeating(s)
    print("Length of the longest substring without repeating characters:", length)
    print("Longest substring without repeating characters:", substring)
