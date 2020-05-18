# Reverse string by using left -1 index slicing.
def checkPalindrome(inputString):
    return inputString == inputString[::-1]

print(checkPalindrome("aabcaa"))