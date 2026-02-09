# 2D list of lists
num_pad = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"]]

# 2D list of tuples
num_pad1 = [(1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            ("*", 0, "#")]

# 2D list of sets
num_pad2 = [{1, 2, 3},
                      {4, 5, 6},
                      {7, 8, 9},
                      {"*", 0, "#"}]

# 2D tuple of lists
num_pad3 = ([1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            ["*", 0, "#"])

# 2D tuple of tuples
num_pad4 = ((1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            ("*", 0, "#"))

# 2D tuple of sets
num_pad5 = ({1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            {"*", 0, "#"})

# 2D set of lists (NOT VALID)
# num_pad6 = {[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9],
#             ["*", 0, "#"]}

# 2D set of tuples
num_pad7 = {(1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            ("*", 0, "#")}

# 2D set of sets (NOT VALID)
# num_pad8 = {{1, 2, 3},
#             {4, 5, 6},
#             {7, 8, 9},
#             {"*", 0, "#"}}

for row in num_pad2:
    for num in row:
        print(num, end=" ")
    print()