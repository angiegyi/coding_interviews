def two_sums(input_list, target):
    for i in range(len(input_list)):
        for j in range(i,len(input_list)):
            if input_list[i] + input_list[j] == target:
                return [i,j]
    return []

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


def singleNumber(nums):

    for i in range(len(nums)):
        a = nums.count(nums[i])

        if len(nums) > 1:
            if a != 0 and a != 2:
                return i
        else:
            return nums[i]


def reverse_a(x):
    """
    reverse an integer using strings
    """
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
    """
    reverse an integer using no strings
    """
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

def numberOfSteps(self, num: int) -> int:

    if num == 0:
        return 0

    if num % 2 == 0:
        return 1 + self.numberOfSteps(num // 2)
    else:
        return 1 + self.numberOfSteps(num - 1)


