
from tokenize import Double


def average():
    """
    Calculate and print two float values from user input 
    """

    try:
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        print((x+y)/2)
    except ValueError:
        print("That's not a float!")
        average()


average()
