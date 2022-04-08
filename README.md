# Python-Tricks
1. Download it and extract file
2. Use `import list_library' to import and start using
https://github.com/erronny/Python-Tricks/blob/main/list.md



# Python List Small Tricks For Begineers

## 1. How to create own `len()` function for Python List?
Algorithms
1. create `counted_length` variable and store 0
2. iterate through list for size of list times
3. Update `counted_length` by adding 1 in them, when for loop iterate
4. Now return the `counted_length`
<b>Code</b>
```
def length(array):
    counted_length = 0
    for i in array:
        counted_length += 1
    return counted_length
```
<b>Driver/Execution code for Testing</b>
```
c = [1, 2, 3, 4, 5, 6]
print(length(c))

 # checking for mixed data types
d = ['1', '2', 'a', 4.5, -5, "6", [1, 2], (1, 2), {'key':'value', 'key2': 2}, {1, 2, 3}]
print(length(d))
```
<b>Output</b>
```
6
10

```


## 2. How to create own `append` Function for Python List?

Algorithm :- 
1. First create empty list
2. Iterate over an array of list, for size of array time.
3. Add every iteration of array in previous array. 
4. 4. If Size of new_array reached equal to array then add item. Break the loop

```
def appending(array, item):
    lst = []
    for i in range(length(array)):
        lst = lst + [array[i]]
        if len(lst) == len(array):
            lst = lst + [item]
    return lst
    
 # driver/execution code
x = [1, 2, 3, 4, 5, 6]
print(appending(x, 6))
```
Output
```
[1, 2, 3, 4, 5, 6]
```
Explanation : - 

## 3. How to create custom `insert()` function for python list?
Algorithms:-

```
def inserting(array, index, item):
    lst = []
    for i in range(length(array)):
        if i == index:
            lst = lst + [item]
            lst = lst + [array[i]]
        else:
            lst = lst + [array[i]]

    return lst

 # driver/execution code
y = [1, 2, 4, 5]
print(inserting(y, 2, 3))
```
<b>output</b>
```
[1, 2, 3, 4, 5]
```

Explanation:-

## 4. How to create Custom/Own `remove()` function for Python List?
Algorithms:-

```
def removing(array, item):
    lst = []
    for i in range(length(array)):
        if array[i] != item:
            lst = lst + [array[i]]
    return lst
    
# driver/ececution code
z = [1, 2, 3, 4]
print(removing(z, 4))
```
<b>output</b>
```
[1, 2, 3]
```
Explanation:-
## 5. How to create Custom `reverse()` function for Python List?
Algorithms:

```
def reverse(array):
    lst  = []
    for i in range(length(array)):
        lst = lst + [array[length(array)-1-i]]
    return lst

# driver/execution code
p = [1, 2, 3]
print(reverse(p))
```
<b>output</b>
```
[3, 2, 1]
```
Explanation:-

## 6. How to create Custom `poping'()` function for Python List?
Algorithm:-
```
def poping(array):
    lst = []
    for i in range(length(array)-1):
        lst = lst + [array[i]]
    return lst
# driver/execution code
x = [1, 2, 3, 4, 5, 6]
print(poping(x))
```
<b>output</b>
```
[1, 2, 3, 4, 5]
```
Explanation:-
