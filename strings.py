def isPalindrome(x: int) -> bool:
    str_version = str(x)
    i = 0
    j = len(str_version) - 1

    while i != j or i < len(str_version) or j > 0:

        if i == j:
            return True
        if str_version[i] != str_version[j]:
            return False
        i += 1
        if i == j:
            return True
        j -= 1
    return True


def romanToInt(s: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    output = 0
    i = 0
    while i < len(s):

        if i == len(s)-1:
            output += roman_dict.get(s[i])
            return output

        #because the list is descending order, if we find an element on the right > left, we can detect the exceptions
        if roman_dict.get(s[i]) < roman_dict.get(s[i+1]):
            output += roman_dict.get(s[i + 1]) - roman_dict.get(s[i])
            i += 2
        #otherwise just get the value from the dictionary normally
        else:
            output += roman_dict.get(s[i])
            i += 1

    return output


def longestCommonPrefix(strs) -> str:
    output = ""

    if len(strs) == 0:
        return output

    if len(strs) == 1:
        output += strs[0]
        return output

    longest_common = strs[0]

    #iterate letter
    for i in range(len(strs)):
        current = (strs[i])
        j = 0
        while j < len(current) and j < len(longest_common) and current[j] == longest_common[j]:
            j += 1
        if j == 0:
            longest_common = ""
        else:
            longest_common = current[:j]

    return longest_common

def sockMerchant(n, ar):
    ar.sort()

    pairs = 0
    i = 0
    while i < (n-1):
        if ar[i] == ar[i+1]:
            pairs += 1
            i += 2
        else:
            i += 1
    return pairs

def defangIPaddr(address):
    copy = address
    copy.replace("a", "1")
    return copy


def isPalindromeStr(x):
    i = 0
    j = len(x) - 1

    while i != j or i < len(x) or j > 0:

        if i == j:
            return True
        if x[i] != x[j]:
            return False
        i += 1
        if i == j:
            return True
        j -= 1