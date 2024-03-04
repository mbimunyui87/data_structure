import math
import time
import random

# Brute force method
def FindMaxSubarrayBruteForce(A, low, high):
    left = low
    right = high
    sum = math.inf
    for i in range(low, high):
        tempSum = 0
        for j in range(i, high):
            tempSum = tempSum + A[j]
            if tempSum > sum:
                sum = tempSum
                left = i
                right = j
    return (left, right, sum)

# Method for finding crossing maximum sub-array
def FindMaxCrossingSubarray(A, low, mid, high):
    left = low
    right = high
    leftSum = -math.inf
    rightSum = -math.inf
    sum = 0
    for i in reversed(range(low, mid)):
        sum += A[i]
        if sum > leftSum:
            leftSum = sum
            left = i

    sum = 0
    for j in range(mid, high):
        sum += A[j]
        if sum > rightSum:
            rightSum = sum
            right = j

    return (left, right, leftSum + rightSum)

# Recursive method
def FindMaxSubarrayRecursive(A, low, high):
    if low + 1 == high:
        return (low, low, A[low])

    mid = (low + high) // 2
    left = FindMaxSubarrayRecursive(A, low, mid)
    right = FindMaxSubarrayRecursive(A, mid, high)
    cross = FindMaxCrossingSubarray(A, low, mid, high)
    if left[2] >= right[2] and left[2] >= cross[2]:
        return left
    elif right[2] >= left[2] and right[2] >= cross[2]:
        return right
    else:
        return cross

# Number of iterations to run the algorithms to average out
NUM_ITERATIONS = 10

print("Size            BruteForce Time             Recursive Time")
print("==========================================================")

for input_size in range(2, 100):
    arr = [random.randint(-100, 100) for _ in range(input_size)]

    # Run brute force method and measure time
    start = time.time()
    for _ in range(NUM_ITERATIONS):
        bf = FindMaxSubarrayBruteForce(arr, 0, len(arr))
        bf_time = time.time() - start

    # Run recursive method and measure time
    start = time.time()
    for _ in range(NUM_ITERATIONS):
        rc = FindMaxSubarrayRecursive(arr, 0, len(arr))
        rc_time = time.time() - start

    print(str(input_size)+ "                      "+str(bf_time) + "                   " + str(rc_time) )

    if bf_time > rc_time:
        print("Cross over point ="+ str(input_size))
        break
