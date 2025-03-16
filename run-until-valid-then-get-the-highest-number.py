def sort_numbers_descending():
    numbers = []  
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num) 
        except ValueError:
            print("Invalid input. Sorting and displaying numbers...")
            break
    
    # Sort numbers in descending order
   
    numbers.sort(reverse=True)
    
    # Display sorted numbers
   
    print("Numbers from highest to lowest:", numbers)

if __name__ == "__main__":
    sort_numbers_descending()


