def sum13(l):
    tot = 0
    prev = 0
    for i in range(len(l)):
        if l[i] != 13 and prev != 13:
            tot += l[i]
        prev = l[i]
    return tot


# def sum13(l):
#     prev, tot = 0, 0
#     for i in l:
#         if i != 13 and prev != 13:
#             tot += i
#         prev = i
#     return tot


# def sum13(l):
#     tot = 0
#     i = 0
#     while i < len(l):
#         if l[i] != 13:
#             tot += l[i]
#             i += 1
#         else:
#             i += 2
#     return tot


# def sum13(l):
#     tot = 0
#     l_iter = iter(l)
#     for i in l_iter:
#         if i == 13:
#             try:
#                 next(l_iter)
#             except StopIteration:
#                 break
#         else:
#             tot += i
#     return tot


if __name__ == "__main__":

    assert sum13([1, 2, 2, 1]) == 6
    assert sum13([1, 1]) == 2
    assert sum13([1, 2, 2, 1, 13]) == 6
    assert sum13([1, 2, 13, 2, 1, 13]) == 4
    assert sum13([13, 1, 2, 13, 2, 1, 13]) == 3
    assert sum13([]) == 0
    assert sum13([13]) == 0
    assert sum13([13, 13]) == 0
    assert sum13([13, 0, 13]) == 0
    assert sum13([13, 1, 13]) == 0
    assert sum13([5, 7, 2]) == 14
    assert sum13([5, 13, 2]) == 5
    assert sum13([0]) == 0
    assert sum13([13, 0]) == 0

    print("all asserts passed")

