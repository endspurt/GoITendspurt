import random

def get_numbers_ticket(min, max, quantity):
    # Validate input parameters to ensure they meet the requirements
    if not (1 <= min <= max and 1 <= quantity <= (max - min + 1)):
        return []  # Return an empty list if the parameters are invalid

    # Generate a set of unique random numbers within the specified range
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    # Return the sorted list
    return sorted(numbers)

# Example usage
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery ticket numbers:", lottery_numbers)
