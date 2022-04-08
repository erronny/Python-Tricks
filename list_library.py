# List Library Module
def length(array):
    counted_length = 0
    for i in array:
        counted_length += 1
    return counted_length

# driver/explanation code

# c = [1, 2, 3, 4, 5, 6]
# print(length(c))

 # checking for mixed data types
 
# d = ['1', '2', 'a', 4.5, -5, "6", [1, 2], (1, 2), {'key':'value', 'key2': 2}, {1, 2, 3}]
# print(length(d))

def poping(array):
    lst = []
    for i in range(length(array)-1):
        lst = lst + [array[i]]
    return lst

# driver/explanation code
# x = [1, 2, 3, 4, 5, 6]
# print(poping(x))

def appending(array, item):
    lst = []
    for i in range(length(array)):
        lst = lst + [array[i]]
        if len(lst) == len(array):
            lst = lst + [item]
    return lst

# driver/explanation code

# h = [1, 2, 3, 4, 5, 6]
# print(appending(h, 6))

def inserting(array, index, item):
    lst = []
    for i in range(length(array)):
        if i == index:
            lst = lst + [item]
            lst = lst + [array[i]]
        else:
            lst = lst + [array[i]]

    return lst

# driver/explanation code

# y = [1, 2, 4, 5]
# print(inserting(y, 2, 3))

def removing(array, item):
    lst = []
    for i in range(length(array)):
        if array[i] != item:
            lst = lst + [array[i]]
    return lst

# driver/explanation code

# z = [1, 2, 3, 4]
# print(removing(z, 4))

def reverse(array):
    lst  = []
    for i in range(length(array)):
        lst = lst + [array[length(array)-1-i]]
    return lst

# driver/explanation code

# p = [1, 2, 3]
# print(reverse(p))
