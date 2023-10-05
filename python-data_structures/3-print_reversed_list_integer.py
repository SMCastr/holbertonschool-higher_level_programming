def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list and returns True or False for each."""
    result = []  # Initialize an empty list to store True/False values
    for num in my_list:
        if num % 2 == 0:
            result.append(True)  # If the number is a multiple of 2, append True
        else:
            result.append(False)  # Otherwise, append False
    return result  # Return the list of True/False values
