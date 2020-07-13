def binary_search_sqrt(i, x, low, high):

    mid = (low + high + 1)//2

    if low > high:
        return False
    elif pow(i, 2) == x:
        return (int(x / (i)))
    elif pow((i + 1), 2) > x > pow(i, 2):
        return binary_search(i, x, mid, high)
    else:
        return False


def mySqrt(x: int):

    """
    needs work
    :param x:
    :return:
    """

    if x == 0:
        return 0

    if x == 1:
        return 1

    for i in range(1, (x // 2) + 1):
        if pow((i + 1), 2) > x > pow(i, 2):
            return ((i) + (i + 1)) // 2
        elif pow(i, 2) == x:
            return (int(x / (i)))


def binary_search(input_list, target, low, high):

    mid = (low + high + 1)//2

    if low > high:
        return False
    elif input_list[mid] == target:
        return mid
    elif target > input_list[mid]:
        return binary_search(input_list, target, mid, high)
    elif target < input_list[mid]:
        return binary_search(input_list, target, low, mid)
    else:
        return False


def removeDuplicates(input_list):
    """
    not complete
    :param input_list:
    :return:
    """
    counter = 0
    i = 0


    if len(input_list) == 1:
        return 1

    while i < len(input_list):
        curr = input_list[i]
        j = i+1
        #while there are duplicates, pop them all
        while 0 < j < (len(input_list)) and input_list[j] == curr:
            input_list.pop(j)
        i += 1
        counter += 1

    return counter

def isSubsequence(s: str, t: str) -> bool:
    """
    needs work
    :param s:
    :param t:
    :return:
    """

    if s == "":
        return True

    if t == "":
        return False

    memo = [-1] * len(s)

    if len(memo) == 1:
        if s[0] == t[0]:
            return True
        return False

    j = 0
    for i in range(len(s)):
        #while element is not target
        while t[j] != s[i] and j < len(t)-1:
            j += 1
        #if element found or not found
        memo[i] = j

    print(memo)

    for j in range(len(memo)-1):
        if memo[j] >= memo[j+1]:
            print('yay')
            return False
    return True


def lengthOfLastWord(s: str) -> int:
    """
    edge cases
    :param s:
    :return:
    """

    arr = []

    if s == " " or "":
        return 0

    for index, char in enumerate(s):
        if char == " ":
            arr.append(index)

    print(arr)

    if len(arr) == 0:
        return 1
    else:
        last_index = arr[-1]
        return len(s[last_index + 1: len(s)])

def addBinary(a: str, b: str) -> str:
    """
    needs work
    """
    output = ""

    # check for length
    if len(a) > len(b):
        b = abs(len(a)-len(b)) * '0' + b
    else:
        a = abs(len(a) - len(b)) * '0' + a

    for i in range(len(a)-1, -1, -1):
        if a[i] == "1" and b[i] == "1":
            output += "0"
        elif a[i] == "0" and b[i] == "0":
            output += "0"
        else:
            output += "1"

        print(output)

    if output[0] == '0':
        return "1" + output

    return output
