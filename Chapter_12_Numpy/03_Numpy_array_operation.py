Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> print(sys.path)
['', 'C:\\Users\\us\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip', 'C:\\Users\\us\\AppData\\Local\\Programs\\Python\\Python311\\DLLs', 'C:\\Users\\us\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 'C:\\Users\\us\\AppData\\Local\\Programs\\Python\\Python311', 'C:\\Users\\us\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages', 'C:\\Users\\us\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\win32', 'C:\\Users\\us\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\win32\\lib', 'C:\\Users\\us\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\Pythonwin']
>>> import numpy as np
>>> a = np.array([5,6,9])
>>> a[0]
5
>>> a[2]
9
>>> a = np.array([1,2],[3,4],[5,6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: array() takes from 1 to 2 positional arguments but 3 were given
>>> a = np.array([[1,2],[3,4],[5,6]])
>>> a.ndim
2
>>> a.itemsize
4
>>> a.dtype
dtype('int32')
>>> a = np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
>>> a.size
6
>>> a.shape
(3, 2)
>>> a = np.array([[1,2],[3,4],[5,6]], dtype=complex)
>>> a
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j],
       [5.+0.j, 6.+0.j]])
>>> np.zeros( (3,4) )
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> np.ones( (3,4) )
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
>>> l = range(5)
>>> l
range(0, 5)
>>> l[0]
0
>>> l[1]
1
>>> np.array(1,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Cannot interpret '5' as a data type
>>> np.arange(1,5)
array([1, 2, 3, 4])
>>> np.arange(1,5,2)
array([1, 3])
>>> np.linspace(1,5,10)
array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
       3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
>>> np.linspace(1,5,5)
array([1., 2., 3., 4., 5.])
>>> np.linspace(1,5,20)
array([1.        , 1.21052632, 1.42105263, 1.63157895, 1.84210526,
       2.05263158, 2.26315789, 2.47368421, 2.68421053, 2.89473684,
       3.10526316, 3.31578947, 3.52631579, 3.73684211, 3.94736842,
       4.15789474, 4.36842105, 4.57894737, 4.78947368, 5.        ])
>>> a = np.array([[1,2],[3,4],[5,6]])
>>> a
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> a.shape
(3, 2)
>>> a.reshape(2,3)
array([[1, 2, 3],
       [4, 5, 6]])
>>> a.ravel()
array([1, 2, 3, 4, 5, 6])
>>> a.min()
1
>>> a.max()
6
>>> a.sum()
21
>>> a.sum(axis=0)
array([ 9, 12])
>>> a.sum(axis=1)
array([ 3,  7, 11])
>>> np.sqrt(a)
array([[1.        , 1.41421356],
       [1.73205081, 2.        ],
       [2.23606798, 2.44948974]])
>>> np.std(a)
1.707825127659933
>>>
>>>
>>>
>>>
>>> import numpy as np
>>> a = np.array([[1,2],[3,4]])
>>> b = np.array([[5,6],[7,8]])
>>> a
array([[1, 2],
       [3, 4]])
>>> b
array([[5, 6],
       [7, 8]])
>>> a+b
array([[ 6,  8],
       [10, 12]])
>>> a*b
array([[ 5, 12],
       [21, 32]])
>>> a/b
array([[0.2       , 0.33333333],
       [0.42857143, 0.5       ]])
>>> a.dot(b)
array([[19, 22],
       [43, 50]])
>>>
