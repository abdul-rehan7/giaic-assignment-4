def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far = 0
    for number in numbers:
        total_so_far += number
    return total_so_far

def main():
    numbers = [1, 2, 3, 4, 5]
    print(add_many_numbers(numbers))

if __name__ == '__main__':
    main()
