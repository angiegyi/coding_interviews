
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


def coin_problem(denominations,cost):
    memo = [0] * cost
    memo[0] = 0

    for i in range(1,len(memo)):
        if cost > memo[i]:
            memo[i] = max(1+memo[cost-i],memo[i])
    return memo[-1]

print(coin_problem([9,5,6,1],12))