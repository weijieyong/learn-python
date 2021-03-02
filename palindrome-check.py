# write a function that takes in a non-empty string and 
# that returns a boolean representing whether the string is a palindrome

string = "abcdcba"

######### my solutions #########
### iterative
# def isPalindrome(string):
#     return string == string[::-1]

### I want to try comparing the first half and second half only.. doesnt work with single-letter string
# def isPalindrome(string):
    # length = len(string)
    # half = round(length/2)
    # if half != length/2:
    #     return string[:half:] == string[length:half-2:-1]
    # else:
    #     return string[:half:] == string[length:half-1:-1]

###### after listening to explaination ######
# O(N) time | O(1) space
# def isPalindrome(string):
#     left = 0
#     right = len(string)-1
#     while left < right:
#         if string[left] != string[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

###### Algo's solutions ######
def isPalindrome(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i+1)

print(isPalindrome(string))
