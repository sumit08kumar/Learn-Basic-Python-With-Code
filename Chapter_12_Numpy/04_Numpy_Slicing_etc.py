Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> n = [6,7,8]
>>> n[0:2]
[6, 7]
>>> n[-1]
8
>>> a = np.array([6,7,8]
...
... a[0:2]
  File "<stdin>", line 1
    a = np.array([6,7,8]
                 ^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a = np.array([6,7,8])
>>> a[0:2]
array([6, 7])
>>> a[-1]
8
>>> a = np.array([[6,7,8], [1,2,3],
... a = np.array([[6,7,8], [1,2,3],
  File "<stdin>", line 2
    a = np.array([[6,7,8], [1,2,3],
    ^^^^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>>
>>>
>>> a = np.array([[6,7,8], [1,2,3], [9,3,2]])
>>> a
array([[6, 7, 8],
       [1, 2, 3],
       [9, 3, 2]])
>>> a[1,2]
3
>>> a[0:2,2]
array([8, 3])
>>> a[-1]
array([9, 3, 2])
>>> a[-1,0:2]
array([9, 3])
>>> a[:,1:3]
array([[7, 8],
       [2, 3],
       [3, 2]])
>>> for row in a:
... print(row)
  File "<stdin>", line 2
    print(row)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> a
array([[6, 7, 8],
       [1, 2, 3],
       [9, 3, 2]])
>>> for row in a:
... print(row)
  File "<stdin>", line 2
    print(row)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> print(row)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'row' is not defined. Did you mean: 'pow'?
>>> print(a)
[[6 7 8]
 [1 2 3]
 [9 3 2]]
>>> for cell in a.flat:
...     print(cell)
...
6
7
8
1
2
3
9
3
2
>>> a = np.arange(6).reshape(3,2)
>>> b = np.arange(6,12).reshape(3,2)
>>> a
array([[0, 1],
       [2, 3],
       [4, 5]])
>>> b
array([[ 6,  7],
       [ 8,  9],
       [10, 11]])
>>> np.vstack((a,b))
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11]])
>>> np.hstack((a,b))
array([[ 0,  1,  6,  7],
       [ 2,  3,  8,  9],
       [ 4,  5, 10, 11]])
>>> a = np.arange(30).reshape(2,15)
>>> a
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])
>>> np.hsplit(a,3)
[array([[ 0,  1,  2,  3,  4],
       [15, 16, 17, 18, 19]]), array([[ 5,  6,  7,  8,  9],
       [20, 21, 22, 23, 24]]), array([[10, 11, 12, 13, 14],
       [25, 26, 27, 28, 29]])]
>>> result = np.hsplit(a,3)
>>> result[0]
array([[ 0,  1,  2,  3,  4],
       [15, 16, 17, 18, 19]])
>>> result[1]
array([[ 5,  6,  7,  8,  9],
       [20, 21, 22, 23, 24]])
>>> result[2]
array([[10, 11, 12, 13, 14],
       [25, 26, 27, 28, 29]])
>>> result = np.vsplit(a,2)
>>> result[0]
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]])
>>> result[1]
array([[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])
>>>
>>> a = np.arange(12).reshape(3,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> b = a > 4
>>> b
array([[False, False, False, False],
       [False,  True,  True,  True],
       [ True,  True,  True,  True]])
>>> a[b]
array([ 5,  6,  7,  8,  9, 10, 11])
>>> a[b] = -1
>>> a
array([[ 0,  1,  2,  3],
       [ 4, -1, -1, -1],
       [-1, -1, -1, -1]])
>>>
