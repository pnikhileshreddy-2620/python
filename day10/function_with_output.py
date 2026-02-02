"""
Basic calculator (fixed)
"""

def add(first, second):
    return first + second

def sub(first, second):
    return first - second

def mul(first, second):
    return first * second  # fixed

def div(first, second):
    if second == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return first / second

def mod(first, second):
    if second == 0:
        raise ZeroDivisionError("Modulo by zero is not allowed.")
    return first % second

def compute(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        return div(a, b)
    elif op == '%':
        return mod(a, b)
    else:
        raise ValueError("Please check the input operator!")

def display(first_number, second_number, operand):
    # FIX: compute directly instead of accumulating from 0
    result = compute(first_number, second_number, operand)
    print(result)
    return result

# Input loop
def main():
    """"This main function used to start the program"""
    output = None
    keep_going = True

    while keep_going:
        """
        This loop we continue unit ,user stop the program
        """
        try:
            """This try block used to take the input from the variable."""
            first_number = float(input("Enter the number: "))
            print("Please select below operators to perform ")
            print('\n + \n - \n * \n / \n % ')
            operand = input("Please choose which operation to perform: ").strip()
            second_number = float(input("Enter the number: "))

            output = compute(first_number, second_number, operand)
            print('Here is the output:', output)

            user = input("Type 'yes' to continue, or 'no' to exit: ").strip().lower()
            if user == 'yes':
                third_number = float(input("Enter the next number: "))
                print('\n + \n - \n * \n / \n % ')
                operand = input("Please choose which operation to perform: ").strip()
                output = display(first_number=output, second_number=third_number, operand=operand)
            else:
                keep_going = False

        except ValueError as ve:
            print("Input error:", ve)
        except ZeroDivisionError as zde:
            print("Math error:", zde)

if __name__ == "__main__":
    main()