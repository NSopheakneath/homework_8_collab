def reverse_ascending(numbers):
    if not numbers:
        return []
    result = []
    subseq = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            subseq.append(numbers[i])
        else:
            result.extend(reversed(subseq))
            subseq = [numbers[i]]

    result.extend(reversed(subseq))
    return result
print(reverse_ascending([1, 2, 3, 2, 5, 4, 7, 8]))  # [3, 2, 5, 4, 8, 7]
print(reverse_ascending([1, 2, 3, 4, 5]))
