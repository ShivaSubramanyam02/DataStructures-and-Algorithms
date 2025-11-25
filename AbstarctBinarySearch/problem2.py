# # CLASSIC SEARCH
# while low <= high:
#     mid = (low + high) // 2
#     if condition(mid):
#         return mid
#     elif go_right:
#         low = mid + 1
#     else:
#         high = mid - 1


# # ANSWER SEARCH
# while low <= high:
#     mid = (low + high) // 2
#     if check(mid):   # feasible?
#         result = mid
#         high = mid - 1  # if minimizing
#     else:
#         low = mid + 1


