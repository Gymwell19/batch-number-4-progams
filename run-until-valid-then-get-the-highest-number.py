def print_highest_number():
    numbers = []  
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)     
        
        #will stop the loop if the user enters a non-integer value 
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            break
    if numbers: 
        
        #max to get the highest number
        print("Highest number:", max(numbers)) 

if __name__ == "__main__":
    print_highest_number()


