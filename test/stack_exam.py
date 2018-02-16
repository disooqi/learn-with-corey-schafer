def validate(num):
    if 0 <= num <= 1048575:
        return num
    else:
        return -1


def solution(S):
    # write your code in Python 3.6
    stack = list()
    ops = ['POP', 'DUP', '+', '-']
    op_seq = S.strip().split()
    last_num = None
    for command in op_seq:

        if command not in ops:
            num = int(command)
            num = validate(num)
            if num == -1:
                return -1
            stack.append(num)

        if command == 'DUP':
            if stack:
                stack.append(stack[-1])
            else:
                return -1

        if command == 'POP':
            if stack:
                p = stack.pop()
            else:
                return -1

        if command == '+':
            if len(stack) > 1:
                p1 = stack.pop()
                p2 = stack.pop()
                s = p1 + p2
                s = validate(s)
                if s == -1:
                    return -1
                stack.append(s)
            else:
                return -1

        if command == '-':
            if len(stack) > 1:
                p_last = stack.pop()
                p2 = stack.pop()
                s = p_last - p2
                s = validate(s)
                if s == -1:
                    return -1
                stack.append(s)
            else:
                return -1
    else:
        if stack:
            return stack[-1]
        else:
            return -1