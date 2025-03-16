def display_duplicates():
    # Ask the user to input 10 numbers
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
    
    # Find numbers that appear more than once
    duplicates = set(num for num in numbers if numbers.count(num) > 1)
    
    # Display the duplicate numbers
    print("Numbers with duplicates:", list(duplicates))

if __name__ == "__main__":
    display_duplicates()


