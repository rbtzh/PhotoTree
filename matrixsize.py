def get_size(allowed_sizes, length):
    random = True if length > allowed_sizes[-1] else False
    right_size = allowed_sizes[-1]
    for size in allowed_sizes:
        if length <= size**2:
            right_size = size
            break
    return(right_size, random)