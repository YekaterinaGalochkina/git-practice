def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max_number = numbers[0]

    for num in numbers:
        if num > max_number:
            max_number = num

    return max_number


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
