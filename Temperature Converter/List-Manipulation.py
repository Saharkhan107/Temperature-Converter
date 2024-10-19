# List Manipulation
# Student: Sahar Iqbal
# Date: 10/19/2024


def main():
    """Main function to handle user input and list manipulation."""
    # Prompt user for input
    user_input = input("Enter a list of numbers separated by commas: ")
    
    # Convert input string to a list of integers
    try:
        number_list = [int(num.strip()) for num in user_input.split(',')]
        
        # Calculate maximum, minimum, and sum
        max_number = max(number_list)
        min_number = min(number_list)
        total_sum = sum(number_list)
        sorted_list = sorted(number_list)
        
        # Print the results
        print(f"Maximum number: {max_number}")
        print(f"Minimum number: {min_number}")
        print(f"Sum of all numbers: {total_sum}")
        print(f"Sorted list: {sorted_list}")
        
    except ValueError:
        print("Please enter valid numbers separated by commas.")

if __name__ == "__main__":
    main()
