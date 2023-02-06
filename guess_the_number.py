# Print prompt to ask for the largest number
print("What is the largest number you chose?")

# Get the input number
n = int(input())

# Initialize number of tries and answer variables
tries = 1
answer = ""

# Initial guess is half of the input number
guess = n // 2

# Start guessing until the correct answer is found
while answer != "y":
    # Print current guess
    print("Is the answer:", guess, "?")

    # Get the answer from user
    answer = input("Please type 'y' for correct, 'u' for higher, or 'd' for lower: ")

    # Check if the answer is correct
    if answer == "y":
        # Print the number of tries it took to get the answer
        print("I guessed it right in", tries, "tries.")
    # Check if the answer is higher
    elif answer == "u":
        # Increase the guess by n // 2 ** (tries + 1)
        guess += n // (2 ** (tries + 1))
    # Check if the answer is lower
    elif answer == "d":
        # Decrease the guess by n // 2 ** (tries + 1)
        guess -= n // (2 ** (tries + 1))
    # Invalid answer
    else:
        print("Invalid input.")
    # Increment number of tries
    tries += 1
