def calculate_average():
    numbers = []  
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num) 
        except ValueError:
            if len(numbers) == 0: 
                print("No valid numbers entered.")
            else:
                
                # Calculate and display average of all entered numbers
               
                average = sum(numbers) / len(numbers)
                print(f"The average of the entered numbers is: {average}")
            break

if __name__ == "__main__":
    calculate_average()
