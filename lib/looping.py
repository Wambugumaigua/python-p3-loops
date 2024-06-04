def happy_new_year():
    # Countdown from 10 to 1
    for i in range(10, 0, -1):
        print(i)
    # Print "Happy New Year!" at the end of the countdown
    print("Happy New Year!")


def square_integers(int_list):
    # Create an empty list to store the squared integers
    squared_list = []
    # Iterate through the elements of int_list
    for num in int_list:
        # Square each integer and append it to squared_list
        squared_list.append(num ** 2)
    # Return the list of squared integers
    return squared_list


def fizzbuzz():
    # Initialize an empty list to store the results
    result = []
    # Iterate through numbers from 1 to 100
    for i in range(1, 101):
        # Check for FizzBuzz condition first
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        # Check for Fizz condition
        elif i % 3 == 0:
            result.append("Fizz")
        # Check for Buzz condition
        elif i % 5 == 0:
            result.append("Buzz")
        # If none of the conditions are met, append the number itself
        else:
            result.append(i)
    # Return the list of FizzBuzz results
    return result
