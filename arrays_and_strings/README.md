## arrays and strings

<br>

* arrays and strings hold values of the same type at contiguous memory locations with the advantage of storing multiple elements of the same type with one single variable name.
  
* we are usually concerned with two things: the index of an element, and the element itself.
  
* accessing elements is fast as long as you have the index (as opposed to linked lists that need to be traversed from the head).
  
* addition or removal of elements into/from the middle of an array is slow because the remaining elements need to be shifted to accommodate the new/missing element (unless they are inserted/removed at the end of the list).
  
* **subarray**: a range of contiguous values within an array (for example, in  `[2, 3, 6, 1, 5, 4]`, `[3, 6, 1]` is a subarray while `[3, 1, 5]` is not).
  
* **subsequence**: a sequence derived from the given sequence without changing the order (for example, in  `[2, 3, 6, 1, 5, 4]`, `[3, 1, 5]` is a subsequence but `[3, 5, 1]` is not).

<br>

----

### two-pointer technique 

<br>

* a typical scenario is when you want to iterate the array from two ends to the middle or when pointers can cross each others (or even be in different arrays).
  
* another scenario is when you need one slow-runner and one fast-runner at the same time (so that you can determine the movement strategy for both pointers).

* in any case, this technique is usually used when the array is sorted.

* in the **sliding window** technique, the two pointers usually move in the same direction and never overtake each other. examples are: longest substring without repeating characters, minimum size subarray sum, and minimum window substring.

<br>

----

### intervals

<br>

* checking if two intervals overlap:

```python
def is_overlap(a, b):
  return a[0] < b[1] and b[0] < a[1]
```

<br>

* merging two intervals:

```python
def merge_overlapping_intervals(a, b):
  return [min(a[0], b[0]), max(a[1], b[1])]
```


<br>

---

### two-dimensional arrays

<br>

* a matrix is a 2d array. they can be used to represent graphs where each node is a cell on the matrix which has 4 neighbors (except those cells on the edge and corners).

* in some languages (like C++), 2d arrays are represented as 1d, so an array of `m * n` elements represents `array[i][j]` as `array[i * n + j]`.
  
* creating an empty matrix:

<br>

```python
zero_matrix = [ [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix)) ]
```

<br>

* copying a matrix:

<br>

```python
copied_matrix = [ row[:] for row in mattrix ]
```

<br>

* the transpose of a matrix can be found by interchanging its rows into columns or columns into rows:

<br>

```python
transposed = zip(*matrix)
```

<br>

---

### check if mountain

<br>

```python
def valid_mountain_array(arr: list[int]) -> bool:
        
        last_number, mountain_up = arr[0], True
        
        for i, n in enumerate(arr[1:]):
            
            if n > last_number:
                if mountain_up == False:
                    return False
                
            elif n < last_number:
                if i == 0:
                    return False
                mountain_up = False
            
            else:
                return False
                    
            last_number = n
        
        return not mountain_up
```

<br>

---

### duplicate zeros in place

<br>

```python
def duplicate_zeros(arr: list[int]) -> list[int]:

        i = 0
        while i < len(arr):
            
            if arr[i] == 0 and i != len(arr) - 1:

                range_here = len(arr) - (i + 2)
                while range_here > 0:
                    arr[i + range_here + 1] = arr[i + range_here]
                    range_here -= 1

                arr[i+1] = 0
                i += 2
            
            else:
                i += 1

        return arr
```

<br>

----

### remove duplicates in place

<br>

```python
def remove_duplicates(nums: list[int]) -> int:
        
        arr_i, dup_i = 0, 1
        
        while arr_i < len(nums) and dup_i < len(nums):
        
            if nums[arr_i] == nums[dup_i]:
                dup_i += 1

            else:
                arr_i += 1
                nums[arr_i] = nums[dup_i]
        
        for i in range(arr_i + 1, dup_i):
            nums[i] = '_'
        
        return  dup_i - arr_i - 1, nums
```

<br>

--- 

### anagrams

<br>

* to determine if two strings are anagrams, there are a few approaches:
    - sorting both strings should produce the same string (`O(N log(N))` time and `O(log(N))` space.
    - if we map each character to a prime number and we multiply each mapped number together, anagrams should have the same multiple (prime factor decomposition, `O(N)`).
    - frequency counting of characters can determine whether they are anagram (`O(N)`).

<br>

```python
def is_anagram(string1, string2) -> bool:

    string1 = string1.lower()
    string2 = string2.lower()

    if len(string1) != len(string2):
        return False

    for c in string1:
        if c not in string2:
            return False
    
    return True
```

<br>



----

### palindromes

<br>

* ways to determine if a string is a palindrome:
  * reverse the string and they should be equal.
  * have two pointers at the start and end of the string, moving the pointers until they meet. 

<br>

```python
def is_palindrome(sentence):

    sentence = sentence.strip(' ')
    if len(sentence) < 2:
        return True
    
    if sentence[0] == sentence[-1]:
        return is_palindrome(sentence[1:-1])
    
    return False
```


<br>

```python
def is_permutation_of_palindromes(some_string):

    aux_dict = {}

    for c in some_string.strip():

        if c in aux_dict.keys():
            aux_dict[c] -= 1
        else:
            aux_dict[c] = 1
        
    for v in aux_dict.values():
        if  v != 0:
            return False
    
    return True
```


<br>



---

### intersection of two arrays

<br>

```python
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
        
  result = []
  set_nums = set(nums1) & set(nums2)
  counter = Counter(nums1) & Counter(nums2)
        
  for n in set_nums:
    result.extend([n] * counter[n])
        
  return result
```

<br>

--- 


### check if isomorphic

<br>

```python
def is_isomorphic(s: str, t: str) -> bool:
        
        map_s_to_t = {}
        map_t_to_s = {}
        
        for ss, tt in zip(s, t):
            
            if (ss not in map_s_to_t) and (tt not in map_t_to_s):
                map_s_to_t[ss] = tt
                map_t_to_s[tt] = ss
            
            elif (map_s_to_t.get(ss) != tt) or (map_t_to_s.get(tt) != ss):
                return False

        return True
```

<br>

---

### absolute difference between the sums of a matrix's diagonals

<br>

```python

def diagonal_difference(arr):

    diag_1 = 0
    diag_2 = 0
    
    i, j = 0, len(arr) - 1
    
    while i < len(arr) and j >= 0:
        
        diag_1 += arr[i][i]
        diag_2 += arr[i][j]
        i += 1
        j -= 1
        
    return diag_1, diag_2, abs(diag_1 - diag_2)
```



<br>

---

### find permutations

<br>

```python


def permutations(string) -> list:

    if len(string) == 1:
        return [string]
    
    result = []
    for i, char in enumerate(string):
        for perm in permutation(string[:i] + string[i+1:]):
            result += [char + perm]
    
    return result
```

<br>

---

### length of the longest substring

<br>

```python
def length_longest_substring(s) -> int:
        
        result = ""
        this_longest_string = ""
        i = 0
        
        for c in s:
            j = 0
        
            while j < len(this_longest_string):
                
                if c == this_longest_string[j]:
                    if len(this_longest_string) > len(result):
                        result = this_longest_string
                    this_longest_string = this_longest_string[j+1:]
                    
                j += 1
            
            this_longest_string += c
            
        return result, this_longest_string
```

<br>
