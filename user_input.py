from sanitize_input import sanitize_input

def get_user_input():
    # Get input from the user
    user_input = input("Please enter your input: ")
    
    # Sanitize the input using the function from the first file
    sanitized_input = sanitize_input(user_input)
    
    # Output the sanitized input
    print("Sanitized input:", sanitized_input)

if __name__ == "__main__":
    get_user_input()
