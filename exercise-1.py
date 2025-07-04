

def replace_last(numbers):
    if len(numbers)==0:
        return numbers
    new_list= [numbers[-1]] + numbers[:-1]
    return new_list

    ...
