# Python List Small Tricks For Begineers

# 1. How to create own `len()` function for Python List?
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


# 2. How to create own `append` Function for Python List?

Algorithm :- 
1. First create empty list
2. Iterate over an array of list, for size of array time.
3. Add every iteration of array in previous array. 
4. 4. If Size of new_array reached equal to array then add item. Break the loop

```
def append(array, item):
    lst = []
    for i in range(len(array)):
        lst = lst + [array[i]]
        if len(lst) == len(array):
            lst = lst + [item]
    return lst
  
 # Driver Code for test
x = [1, 2, 3, 4, 5]
print(append(x, 6))
```
Output
```
[1, 2, 3, 4, 5, 6]
```
Explanation : - 
