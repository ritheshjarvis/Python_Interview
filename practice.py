# Reverse a string - Two Pointer Technique

def reverse(str_):
    if len(str_) < 1:
        return str_
    else:
        return reverse(str_[1:]) + str_[:1]


input_str = "abcd"
print(reverse(input_str))