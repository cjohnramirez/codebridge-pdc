def get_number():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return x, y 
    
def game():
    while True: 
        while True:
            choice_array = [1, 2, 3, 4, 5]  
            
            print('1: Addition \n'
            '2: Subtraction \n'
            '3: Multiplication \n'
            '4: Division \n'
            '5: Exit \n')
            
            # convert input string to int first
            choice = int(input("Enter your user input: "))
            if (choice in choice_array):
                break
            
            if (choice == 1):
                num1, num2 = get_number()
                result = num1 + num2
                print (f"The sum of {num1} and {num2} is {result}")
    
game()