# HOW TO MEASURE EXECUTION TIME IN PYTHON

import time

start_time = time.perf_counter()

# YOUR CODE GOES HERE
for i in range(100):
    pass

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.8f} seconds")