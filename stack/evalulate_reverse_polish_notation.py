from typing import List
from collections import deque


def evalRPN(tokens: List[str]) -> int:
    stack_num = deque()
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack_num.append(int(token))
        else:
            s2 = stack_num.pop()
            s1 = stack_num.pop()
            stack_num.append(int(eval(f"{s1}{token}{s2}")))
    return stack_num.pop()


# print(evalRPN(["2", "1", "+", "3", "*"]))
# print(evalRPN(["4", "13", "5", "/", "+"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
