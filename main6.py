import numpy as np
# a = np.array([20, 30, 40, 50])
# b = np.array(4)
# b2 = ([2,4,5,6])
# c = a + b
# print(c)
# print(b**2)
#
# print(np.exp(b))
# print(np.sort(b2))
# d = np.sort(b2)
# e = d + b
# print(e)



# a = np.arange(12).reshape((3,4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.cumsum(axis=1))



# a = np.arange(3)
# b = np.arange(3)
#
# print(a.dot(b))
#
# c = np.array([[2, 3, 6], [5, 1, 3]])
# d = np.array([[1, 4], [2, 1], [3, 5]])
# e = c.dot(d)
# print(e)


# a = np.arange(6).reshape(3, 2)
# print(a)
# for b in a:
#     for c in b:
#         print(b)

# for b in a.flat:
#     print(b)


# a = np.arange(6)
# print(a)
# b = a.reshape([3,2])
# c = a.reshape([2,3])
# print(b)
# print(c)
# d = c.ravel()
# print(d)
# e = c.T
# print(e)



# zad 1

# a = np.arange(3)
# b = np.arange(3)
# print(a*b)

# zad 2

# a = np.arange(9).reshape(3,3)
# b = np.arange(16).reshape(4,4)
# print(a)
# print(b)
# print()
# print(a.sum(axis = 0))
# print(a.sum(axis = 1))
# print()
# print(b.sum(axis = 0))
# print(b.sum(axis = 1))

# zad 3

# a = np.arange(3)
# b = np.arange(3)
# c = a.dot(b)
# print(c)

# zad 4

# a = np.array([2, 4, 5, 6, 9])
# b = np.array([2.5, 3.2, 1.5, 7.4, 6.5])
# print(a*b)

# # zad 5 i 6 i 7
#
# b = np.arange(6).reshape(2,3)
# print(b)
# for a in b:
#     a = np.sin(b)
# print(a)
#
# # zad 6
#
# a = np.arange(6).reshape(2,3)
# print(a)
# for b in a:
#     b = np.cos(a)
# print(b)
#
# # zad 7
#
# print(a+b)

# zad 8

# a = np.arange(9).reshape(3,3)
# for b in a:
#     print(b)

# zad 9

# a = np.arange(9).reshape(3,3)
# for b in a.flat:
#     print(b)

# zad 10

# a = np.arange(81).reshape(9,9)
# print(a)
# print()
# b = a.ravel()
# print(b)
# print()
# c = a.T
# print(c)

# zad 11

# a = np.arange(12)
# b = a.reshape(3,4)
# print("3x4")
# print(b)
# c = a.reshape(4,3)
# print("4x3")
# print(c)
# d = a.reshape(2,6)
# print("2x6")
# print(d)
#
# print("3x4")
# for x in b.flat:
#     print(x)
# print("4x3")
# for x2 in c.flat:
#     print(x2)
# print("2x6")
# for x3 in d.flat:
#     print(x3)