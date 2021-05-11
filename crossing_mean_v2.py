# crossing_mean_v2.py

a_list = [0, 0, 3, 0, 4, 5, -2, 3, -4, -2, -3, 1, 6, 0, 4, -3, -2, 6, 7, 8, 2, 0, 5]

def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def sign_change_gaps(a_list):
    start_index = -1

    # Find index of first non-zero value and its sign
    for index, item in enumerate(a_list):
            if item:
                start_index = index
                start_sign = 1 if item > 0 else -1
                break

    # If start_index is -1, all items are zero, and there is no change of sign at all
    if start_index == -1:
        return []
    
    # List of gaps
    gaps = list()

    # While start_index < length of list
    while start_index < len(a_list):
        gap = 0 # Default value for gap, if no sign change found

        # Start looking for sign change
        for index in range(start_index, len(a_list)):
                # Get item at index
                item = a_list[index]
                # If sign of item is different from sign_first and item is not 0
                # we have found a sign change
                if sign(item) != start_sign and sign(item) != 0:
                    gap = index - start_index
                    gaps.append(gap)
                    break

        # If gap = 0, no sign change found
        if gap == 0:
            break
        
        start_index, start_sign = index, sign(item)

    return gaps
