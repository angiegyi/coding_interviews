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



def majorityElement(nums) -> int:
    quick = Counter(nums)

    for value, count in quick.items():
        if count > len(nums) / 2:
            return value


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
