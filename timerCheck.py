# Concept: A larger range in outer loop (i) should take longer to execute than a larger range in inner loop (j) with the same range values

import time 

# when outer loop is large
t0 = time.time()
k = 0
for i in range (1, 10000000):
    for j in range (1, 10):
        k = k+1
t1 = time.time()

# when inner loop is large
print ("time when i is large =", t1-t0)

t2 = time.time()
l = 0
for i in range (1, 10):
    for j in range (1, 10000000):
        l = l + 1
t3 = time.time()

print ("time when j is large =", t3-t2)


