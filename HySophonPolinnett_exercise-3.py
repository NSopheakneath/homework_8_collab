def remove_all_after(numbers, n):
    if not numbers:
        return []
    elif n not in numbers:
        return numbers

    new_list = []
    for x in numbers:
        new_list.append(x)
        if x == n:
            break
    return new_list

