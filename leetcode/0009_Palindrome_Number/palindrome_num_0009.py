# 2024-11-10
# Palindrome_number
# If input a Palindrome number return TRUE, and FALSE otherwise

def main(x : int):
    length = len(str(x))
    x_str = str(x)
    if x < 0:
        return False
    for i in range(length // 2):
        if x_str[i] != x_str[-i-1]:
            return False
    return True

main(121)
main(123)