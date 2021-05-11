'''crossing_mean.py

Find the gaps between each time the mean of a list is crossed, i.e, if values are
initially greater than the mean, the first index at which they become (strictly) less
than the mean, and vice versa.
'''

def sign(n):
    '''Returns the sign of a number n.'''
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def sign_change_gaps(a_list):
    ''' Given a_list of numeric values, find the gaps between sign changes.
    
    Argument: a_list - list of numeric values
    
    Returns: list of gaps between sign changes.'''
    start_index = -1

    # Find index of first non-zero value and its sign
    for index in a_list:
        item = a_list[index]
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
        gap = -1 # Default value for gap, if no sign change found

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

        # If gap = -1, no sign change found
        if gap == -1:
            break
        
        start_index, start_sign = index, sign(item)

    return gaps


def mean_crossing_gaps(a_list):
    '''Given a list of numeric values, find the gaps between mean crossings, i.e,
    the indices at which values change from being greater than mean to less than mean,
    or vice versa.
    
    Argument: a_list of numeric values
    Returns: list of gaps between mean crossings
    '''
    # First, find mean of list
    mean = sum(a_list) / len(a_list)

    # Then, find deviation of each element from mean
    # Note: if item is < mean, its deviation is < 0,
    #       if item is > mean, its deviation is > 0
    deviations = [item - mean for item in a_list]

    # Find the gaps between sign changes in list of deviations
    return sign_change_gaps(deviations)


def average_mean_crossover(a_list):
    '''Returns the average number of times mean crossings occur in a_list.'''
    gaps = mean_crossing_gaps(a_list)
    crossovers = len(gaps)
    return len(a_list) / crossovers

