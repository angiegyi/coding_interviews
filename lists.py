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


def merge(nums1, nums2):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    j = 0
    zero_flag = False
    for i in range(len(nums2)):
        current = nums2[i]

        while j < len(nums1) and nums1[j] < current:
            if nums1[j] == 0:
                nums1[j] = current
                zero_flag = True
                break
            j += 1
        if not zero_flag:
            nums1.insert(j, current)
            nums1.pop()
        else:
            zero_flag = False

    nums1.sort()
    return nums1


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            while i < len(nums)-1:
                prev = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = prev
                i += 1

    return nums

print(moveZeroes([0,0,1]))