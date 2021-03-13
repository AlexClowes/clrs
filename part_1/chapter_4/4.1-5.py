def max_subarray_linear(A):
    best_sum = float("-inf")
    current_sum = 0
    for j in range(len(A)):
        if current_sum > 0:
            current_sum += A[j]
        else:
            current_sum = A[j]
            current_left = j
        if current_sum > best_sum:
            best_sum = current_sum
            best_left = current_left
            best_right = j + 1
    return best_left, best_right, best_sum
