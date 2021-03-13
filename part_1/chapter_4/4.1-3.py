import operator
import random
import time

import matplotlib.pyplot as plt


def max_subarray_brute_force(A, low, high):
    max_sum = float("-inf")
    for i in range(low, high):
        total = 0
        for j in range(i, high):
            total += A[j]
            if total > max_sum:
                max_sum = total
                left = i
                right = j + 1
    return (left, right, max_sum)


def max_crossing_subarray(A, low, mid, high):
    left_sum = float("-inf")
    total = 0
    for i in range(mid - 1, low - 1, -1):
        total += A[i]
        if total > left_sum:
            left_sum = total
            max_left = i
    right_sum = float("-inf")
    total = 0
    for j in range(mid, high):
        total += A[j]
        if total > right_sum:
            right_sum = total
            max_right = j + 1
    return (max_left, max_right, left_sum + right_sum)


def max_subarray_recursive(A, low, high):
    if high - low == 1:
        return (low, high, A[low])
    mid = (low + high) // 2
    return max(
        (
            max_subarray_recursive(A, low, mid),
            max_subarray_recursive(A, mid, high),
            max_crossing_subarray(A, low, mid, high),
        ),
        key=operator.itemgetter(2),
    )


def max_subarray_hybrid(A, low, high):
    if high - low < 58:  # Length below which brute force solution is faster
        return max_subarray_brute_force(A, low, high)
    mid = (low + high) // 2
    return max(
        (
            max_subarray_hybrid(A, low, mid),
            max_subarray_hybrid(A, mid, high),
            max_crossing_subarray(A, low, mid, high),
        ),
        key=operator.itemgetter(2),
    )


def test_runtime(func, data):
    start = time.perf_counter()
    func(data, 0, len(data))
    return time.perf_counter() - start


def main():
    REPEATS = 100
    brute_force_times = []
    recursive_times = []
    hybrid_times = []
    for length in range(1, 100):
        brute_force_times.append(0)
        recursive_times.append(0)
        hybrid_times.append(0)
        for _ in range(REPEATS):
            A = random.choices(range(-100, 101), k=length)
            brute_force_times[-1] += test_runtime(max_subarray_brute_force, A)
            recursive_times[-1] += test_runtime(max_subarray_recursive, A)
            hybrid_times[-1] += test_runtime(max_subarray_hybrid, A)
    plt.plot(brute_force_times, label="brute force")
    plt.plot(recursive_times, label="recursive")
    plt.plot(hybrid_times, label="hybrid")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
