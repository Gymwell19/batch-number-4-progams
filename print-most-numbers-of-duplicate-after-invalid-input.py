def most_frequent_number():
    numbers = []  
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Exiting...")
            break
    
    # the number with the highest frequency
    most_frequent = max(numbers, key=numbers.count)
    
    # will display the number with the most duplicates
    print("The number with the most duplicates is:", most_frequent)

if __name__ == "__main__":
    most_frequent_number()
