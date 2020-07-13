def afunction(n,b,a):
    count = 0
    #stores the number of items i can take
    memo = [0]*(n)

    for i in range(n):
        if b-a[i] >= 0:
            memo[i] = max()
            b -= a[i]
    return count


# t = int(input())
# for i in range(1, t + 1):
#     n, b = [int(s) for s in input().split(" ")]
#     a = list(map(int, input().split()))
#     print(a)
#     answer = afunction(n,b,a)
#     print("Case #{}: {}".format(i, answer))
#
#

def stats(input_list):
    fruits = dict()
    for fruit_tuple in input_list:
        if fruit_tuple[0] not in fruits:
            fruits[fruit_tuple[0]] = [fruit_tuple[1]]
        else:
            fruits[fruit_tuple[0]].append(fruit_tuple[1])

    fruit_names = sorted(fruits)
    out = []

    for fruit, cost in fruits.items():
        cost_temp = cost
        output = []
        output.append(fruit)

        for _ in cost_temp:
            max_price = max(cost_temp)
            cost_temp.remove(max_price)
            output.append(max_price)

            min_price = min(cost_temp)
            cost_temp.remove(min_price)
            output.append(min_price)

            median = 0
            if len(cost_temp) > 0:
                for i in range(len(cost_temp)):
                    median += cost_temp[i]

                median = median/len(cost_temp)
                output.append(median)

        out.append(output)

    return out

print(stats([('apple', 10),('banana',20),('apple',33),('pear',40)]))


