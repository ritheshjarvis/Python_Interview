def check_palindrome(_input : str) -> bool:
    return _input == input_[::-1]

input_ = 'abcba'
print(f'Is Palindrome!: {check_palindrome(input_)}')