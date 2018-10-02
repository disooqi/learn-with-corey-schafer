def runningTime(arr):
    shifts_count = 0
    for h in range(1, len(arr)):
        e = arr[h]
        for i in range(h-1,-1, -1):
            if e < arr[i]:
                arr[i+1] = arr[i]
                arr[i] = e
                shifts_count += 1
            else:
                break

runningTime([2, 1, 3, 1, 2])
# import math
#
#
# def solution(A, B):
#     if A < 0 and B < 0:
#         return 0
#
#     if A < 0:
#         A = 0
#
#     sqrt = math.sqrt(A)
#     start = math.ceil(sqrt)
#     end = math.floor(math.sqrt(B))
#
#     count = 0
#     for x in range(int(start), int(end) + 1):
#         count += 1
#     else:
#         return count
# ############################# 2 ######################
# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
#
# def validate(num):
#     if 0 <= num <= 1048575:
#         return num
#     else:
#         return -1
#
#
# def solution(S):
#     # write your code in Python 3.6
#     stack = list()
#     ops = ['POP', 'DUP', '+', '-']
#     op_seq = S.strip().split()
#     last_num = None
#     for command in op_seq:
#
#         if command not in ops:
#             num = int(command)
#             num = validate(num)
#             if num == -1:
#                 return -1
#             stack.append(num)
#
#         if command == 'DUP':
#             if stack:
#                 stack.append(stack[-1])
#
#         if command == 'POP':
#             if stack:
#                 p = stack.pop()
#             else:
#                 return -1
#
#         if command == '+':
#             if len(stack) > 1:
#                 p1 = stack.pop()
#                 p2 = stack.pop()
#                 s = p1 + p2
#                 s = validate(s)
#                 if s == -1:
#                     return -1
#                 stack.append(s)
#             else:
#                 return -1
#
#         if command == '-':
#             if len(stack) > 1:
#                 p_last = stack.pop()
#                 p2 = stack.pop()
#                 s = p_last - p2
#                 s = validate(s)
#                 if s == -1:
#                     return -1
#                 stack.append(s)
#             else:
#                 return -1
#     else:
#         if stack:
#             return stack[-1]
#         else:
#             return -1
# ############################# 3 ######################
# # SELECT inv_num, sum(price) from invoice_items group by inv_num;
# ############################# 4 ######################
# def solution(A, K):
#     n = len(A)
#     for i in range(n - 1):
#         if not ((A[i] == A[i + 1]) or (A[i + 1] == A[i] + 1)):
#             return False
#     if (A[0] != 1 or A[n - 1] != K):
#         return False
#     else:
#         return True



