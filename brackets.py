def even_brackets(s: str) -> bool:
    brackets = { "(":0, ")":0, "{":0,"}":0, "[":0, "]": 0}
    bracket_list = ["(",")","{","}","[","]"]

    for bracket in s:
        count = s.count(bracket)
        brackets.update({bracket: count})

    print(brackets)

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