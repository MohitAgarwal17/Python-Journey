# import numpy as np
# print(np.__version__)

# a = np.array([1, 2, 3, 4])
# a = a * 2
# print(a)
# print(type(a))
# print(a.ndim)
# print(a.shape)

# array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
#                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
#                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z','']]])

# print(array[0, 0, 0]) # same as print(array[0][0][0])

# word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]
# print(word)

# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9 ,10, 11, 12],
#                 [13, 14, 15, 16]])
# Slicing
# arr[start:end:step]  -ve indexing for reverse

# rows
# print(arr[1:])
# print(arr[1:3])
# print(arr[1:3:2])
# print(arr[-1::-2])
# print(arr[::-1])

# columns
# print(arr[:, 0])
# print(arr[:, -1])
# print(arr[:, 0:2])
# print(arr[:, 0:3:2])
# print(arr[:, ::2])
# print(arr[:, ::-1])

# rows and columns
# print(arr[0:2, 2:])
# print(arr[0:2, 2:])
# print(arr[2:, 0:2])
# print(arr[2:, 2:])

# Scalar Arithmetic

# array = np.array([1, 2, 3])
# print(array + 1)
# print(array - 1)
# print(array * 3)
# print(array / 4)
# print(array ** 5)

# Vectorized Math Functions

# array = np.array ([1.01, 2.5, 3.99])
# print(np.sqrt(array))
# print(np.round(array))
# print(np.floor(array))
# print(np.ceil(array))
# print(np.pi)

# Exercise

# radii = np.array([1,2,3])
# print(f"{np.pi * radii ** 2}")
# For Formatting
# np.set_printoptions(precision=2)
# print(np.pi * radii ** 2)

# areas = np.pi * radii ** 2
# print([f"{x:.2f}" for x in areas])

# Element-wise Arithmetic

# a1 = np.array([1, 2, 3])
# a2 = np.array([4, 5, 6])

# print(a1 + a2)
# print(a1 - a2)
# print(a1 * a2)
# print(a1 / a2)
# print(a1 ** a2)

# Comparison Operators

# scores = np.array([91, 55, 100, 73, 82, 64])
# print(scores == 100)
# print(scores >= 60)
# scores[scores < 60] = 0
# print(scores)

# Broadcasting

# Broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.

# The dimensions have the same size(for both arrays rows and columns)
# OR
# One of the dimensions has a size of 1.

# array1 = np.array([[1, 2, 3, 4]])
# array2= np.array([[1], [2], [3], [4]])
# print(array1.shape)
# print(array2.shape)
# print(array1 * array2)

# array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9,10]])
# array2 = np.array([[1], [2], [3],[4],[5],[6],[7],[8],[9],[10]])
# print(array1.shape)
# print(array2.shape)
# print(array1 * array2)

# Aggregate Functions

# Aggregate functions = summarize data and typically return a single value

# a = np.array([[1, 2, 3, 4, 5],
#              [6, 7, 8, 9, 10]])

# print(np.sum(a))
# print(np.sum(np.multiply(a,a)))
# print(np.mean(a))
# print(np.std(a))
# print(np.var(a))
# print(np.min(a))
# print(np.max(a))
# print(np.argmin(a))
# print(np.argmax(a))
# print(np.sum(a, axis=0))
# print(np.sum(a, axis=1))

# Filtering

# Filtering = Refers to the process of selecting elements from an array that match a given condition

# ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
#                  [39, 22, 15, 99, 18, 19, 20, 21]])

# teenagers = ages[ages < 20]
# adults = ages[(ages >= 20) & (ages < 65)]
# seniors = ages[(ages >= 65)]
# evens = ages[ages % 2 == 0]
# odds = ages[ages % 2 == 1]
# print(teenagers)
# print(adults)
# print(seniors)
# print(teenagers)
# print(evens)
# print(odds)

# adults = np.where(ages >= 20, ages, 0) # 0 is filler, can use -1
# print(adults)

# Random Numbers

# rng = random number generator
# rng = np.random.default_rng(seed = 1) # seed keeps the same random numbers
# print(rng.integers(1, 7, size = 2))
# print(np.sum(rng.integers(1, 7, size = 2)))
# print(rng.integers(1, 7, size = (3, 2)))

# np.random.seed(seed = 1)
# print(np.random.uniform())
# print(np.random.uniform(1, 101, size = 3))
# print(np.random.uniform(1, 101, size = (3, 3)))

# rng = np.random.default_rng()
# array = np.array([1, 2, 3, 4, 5])
# rng.shuffle(array)
# print(array)

# fruits = np.array(["apple", "banana", "cherry", "orange", "pineapple"])
# fruit = rng.choice(fruits)
# fruits = rng.choice(fruits, size = 3)
# fruits = rng.choice(fruits, size = (3, 3))
# print(fruits)