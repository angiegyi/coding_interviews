def two_sums(input_list, target):
    for i in range(len(input_list)):
        for j in range(i,len(input_list)):
            if input_list[i] + input_list[j] == target:
                return [i,j]
    return []


def singleNumber(nums):

    for i in range(len(nums)):
        a = nums.count(nums[i])

        if len(nums) > 1:
            if a != 0 and a != 2:
                return i
        else:
            return nums[i]


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

def reverse_a(x):
    x_str = str(x)

    output = ""

    if x > 0:
        for i in range(len(x_str) - 1, -1, -1):
            output += x_str[i]
        output = int(output)

    elif x < 0:
        for i in range(len(x_str) - 1, 0, -1):
            output += x_str[i]
        output = -int(output)

    else:
        output = x

    if (output < -2**31) or (output) > (2**31 - 1):
        return 0

    return output


def reverse_no_string(n):
    negative = False

    if n < 0:
        negative = True
        n = n * -1

    output = 0
    while n > 0:
        output = (output * 10) + (n % 10)
        n //= 10

    if output > 2**32-1 or output < -2**32:
        return 0

    if negative:
        return -1 * output
    else:
        return output

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


def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    # Return the minimum number of characters to make the password strong
    good_counter = 0

    # check length
    if n > 6:
        good_counter += 1

    for i in range (len(password)):
        if password[i] in numbers:
            good_counter += 1
            break


    for i in range (len(password)):
        if password[i] in lower_case:
            good_counter += 1
            break


    for i in range (len(password)):
        if password[i] in upper_case:
            good_counter += 1
            break


    for i in range (len(password)):
        if password[i] in special_characters:
            good_counter += 1
            break


    if n < 6:

        curr = (5-good_counter)
        print(curr)

        a = abs(6 - n - curr)

        return a

    return 5 - (good_counter)



def even_brackets(s: str) -> bool:
    brackets = { "(":0, ")":0, "{":0,"}":0, "[":0, "]": 0}
    bracket_list = ["(",")","{","}","[","]"]

    for bracket in s:
        count = s.count(bracket)
        brackets.update({bracket: count})

    flag = False

    for i in range (0,len(bracket_list)-1,2):
        if brackets.get(bracket_list[i]) == brackets.get(bracket_list[i+1]):
            if brackets.get(bracket_list[i]) > 0 and brackets.get(bracket_list[i+1]) > 0:
                flag = True
        else:
            return False
    return flag


def valid_brackets(s):
    left_stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}

    for i in s:
        if i == "(" or i == "{" or i == "[":
            left_stack.append(i)


        else:
            if len(left_stack) != 0 and i == brackets.get(left_stack[-1]):
                left_stack.pop()
            else:
                return False

    return True


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


def two_sums_efficient(input_list,target):
    input_list.sort()

    for i in range (len(input_list)):
        compliment = target - input_list[i]
        print(compliment)

        find_element = binary_search(input_list,compliment, 0, len(input_list)-1)
        if find_element!= False or find_element == 0 and find_element != i:

            if i < find_element:
                return [i,find_element]
            else:
                return [find_element,i]

    return None

from collections import Counter

def two_sums_hash(input_list,target):

    count = {}

    for i in range(len(input_list)):
        count[input_list[i]] = i

    for i in range(len(input_list)):
        comp = target - input_list[i]

        if comp in count and count.get(comp) != i:
            if i < count.get(comp):
                return [i,count.get(comp)]
            else:
                return [count.get(comp),i]

    return None

#print(two_sums_hash([2,7,11,15],9))

def merge_lists(list1, list2):
    output = []

    while len(list1) != 0 and len(list2) != 0:
        list1_current = list1[-1]
        list2_current = list2[-1]

        if list1_current > list2_current:
            output.append(list2.pop(0))

        elif list1_current < list2_current:
            output.append(list1.pop(0))

        else:
            output.append(list1.pop(0))
            output.append(list2.pop(0))

    if len(list1) == 0 and len(list2) == 0:
        return output
    elif len(list1) == 0:
        return output + list2
    else:
        return output + list1


def max_at_index(list1,list2):
    output = []

    for i in range(len(list1)):
        list1_current = list1[i]
        list2_current = list2[i]

        if list1_current > list2_current:
            output.append(list1_current)

        elif list1_current < list2_current:
            output.append(list2_current)

        else:
            output.append(list1_current)

    return output



def removeElement(nums, val) -> int:

    i = 0
    while i < len(nums):
        curr_i = 0
        if nums[i] == val:
            nums.pop(i)
            i = curr_i
        else:
            i += 1
    return nums

from math import pow




def reverseStrings(s):
    """
    Do not return anything, modify s in-place instead.
    """
    i = 0
    j = len(s) - 1

    while i < j:
        front_temp = s[i]
        back_temp = s[j]
        s[i] = back_temp
        s[j] = front_temp
        i += 1
        j -= 1
    return s

def fizzBuzz(n: int):

    output = []

    if n == 0:
        return ['0']

    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            output.append('FizzBuzz')
        elif (i % 3 == 0):
            output.append('Fizz')
        elif (i % 5 == 0):
            output.append('Buzz')
        else:
            output.append(str(i))

    return output


def climbStairs(n: int) -> int:
    memo = [0] * (n + 1)
    # base case 0 stairs
    memo[0] = 0
    # base case 1 stair
    memo[1] = 1
    memo[1] = 2

    for i in range(3, n+1):
        memo[i] = memo[i - 1] + memo[1]
    return memo[-1]




def plusOne(digits):

    output = digits

    for i in range(len(digits)-1,-1,-1):
        #if its not a 9, incremennt
        if digits[i] != 9:
            output[i] = output[i] + 1
            return output
        else:
        #ifit is a 9, set to 0
            output[i] = 0

    output.insert(0,1)
    return output


def majorityElement(nums) -> int:
    quick = Counter(nums)

    for value, count in quick.items():
        if count > len(nums) / 2:
            return value


def pascals_triangle(n):
    """
    Dynammic programming
    """
    if n == 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    memo = [0] * n
    memo[0] = [1]
    memo[1] = [1, 1]

    for i in range(2, len(memo)):

        # this is the list for the current level
        memo_level = [0] * (i + 1)
        memo_level[0], memo_level[i] = 1,1

        # this is the last row in list rep
        last_row = memo[i - 1]
        for j in range(1, len(last_row)):
            memo_level[j] = last_row[j - 1] + last_row[j]

        memo[i] = memo_level

    return memo


def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_counter = 0
    i = 0
    temp = len(nums)

    while i < temp:
        if nums[i] == 0:
            zero_counter = zero_counter + 1
            nums.pop(i)
            temp -=1
        else:
            i += 1

    while zero_counter != 0:
        nums.insert(len(nums),0)
        zero_counter -=1
    return nums


from collections import Counter

def intersect(nums1, nums2):

    output = []

    if len(nums1) > len(nums2):
        count1 = Counter(nums2)
        count2 = Counter(nums1)
    else:
        count1 = Counter(nums1)
        count2 = Counter(nums2)

    for item, count in count1.items():
        if item in count2:
            min_count = min(count2[item], count)
            for i in range(min_count):
                output.append(item)

    return output

def commonChars(A):

    prev = A[0]
    for i in range(len(A)-1):
        b = A[i+1]
        prev = intersect(b,prev)
    return prev


def minsum(arr):
    min_s = abs(arr[0]+arr[1])

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            a =abs(arr[i]+arr[j])
            if abs(arr[j]+arr[i]) < min_s:
                min_s =a
    return min_s

def backspaceCompare(S,T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    S = delete_hash(S)
    T = delete_hash(T)

    return T == S

def delete_hash(string):

    while '#' in string:
        hash_i = string.index('#')

        if hash_i == len(string):
            string = string[:hash_i - 1]

        elif hash_i == 0:
            string = string[1:]

        else:
            string =  string[:hash_i-1] + string[hash_i+1:]
    return string

def countCharacters(words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    length_total = 0

    char_count = Counter(chars)
    print(char_count)

    for word in words:
        temp_word_count = Counter(word)
        for char in word:
            count = temp_word_count[char]
            if char in char_count and char_count[char] >= count:
                flag = True
            else:
                flag = False
                break

        if flag:
            length_total += len(word)

    return length_total
