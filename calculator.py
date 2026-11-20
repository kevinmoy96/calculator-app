# def function_name(parameter1, parameter2):
#     """Optional docstring describing what the function does."""
#     # Function body (indented by 4 spaces)
#     result = parameter1 + parameter2
#     return result

def temp_convert():
    """Converting between Fahrenheit and Celsius."""    
    print("\nPlease select one of the following: ")
    print('1. Fahrenheit to Celsius')
    print('2. Celsius to Fahrenheit')
    user_input = input().strip()
    # if starting in F
    if user_input == "1":
        result = 0
        temp = int(input("\nPlease enter a temperature value in Fahrenheit: "))
        result = (temp-32)*(5/9)
        return (f"The converted temperature is: {result} degrees Celsius.") 
    elif user_input == "2":
        # if starting in C
        result = 0
        temp = int(input("\nPlease enter a temperature value in Celsius: "))
        result = (temp*(9/5))+32
        return (f"\nThe converted temperature is: {result} degrees Fahrenheit.") 

def height_convert():
    """Converting between Inches and Centimeters."""
    print("\nPlease select one of the following: ")
    print("1. Inches to Centimeters")
    print("2. Centimeters to Inches")
    user_input = input().strip()
        # if starting in F
    if user_input == "1":
        result = 0
        len = int(input("\nPlease enter a measurement in inches: "))
        result = len*2.54
        return (f"\nThe converted length is: {result} centimeters.") 
    elif user_input == "2":
        # if starting in C
        result = 0
        len = int(input("\nPlease enter a measurement in centimeters: "))
        result = len/2.54
        return (f"\nThe converted length is: {result} inches.")

def weight_convert():
    """Converting between Pounds and Kilograms."""
    result = 0
    return result
   
def currency_convert():
    """Converting between Dollars and RMB."""
    result = 0
    return result

def time_convert():
    """Converting international time, from CST to EST."""
    # china is 13 hours ahead
    given = input("\nPlease enter a time, followed by 'am' or'pm': ")
    result = 0
    return result



def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Temperature Conversions (Between Fahrenheit and Celsius)")
        print("2. Height Converstions (Between Inches and Centimeters)")
        print("3. Weight Conversions (Between Pounds and Kilograms)")
        print("4. Currency Conversions (Between Dollars and RMB)")
        print("5. Time Conversions (CST annd EST)")
        print("0. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            print(temp_convert())
        elif choice == "2":
            print(height_convert())
        elif choice == "3":
            print(weight_convert())
        elif choice == "4":
            print(currency_convert())
        elif choice == "5":
            print(time_convert())
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()