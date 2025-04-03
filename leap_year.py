#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: April 3, 2025

# Leap year determining program in python


def main():

    # Get year from user
    year = input("What is the year? ")

    # Try converting year to an integer
    try:

        # Convert
        year = int(year)

        # Checking year multiples of 4, 100 and 400, print leap year result
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("It's a leap year")
                else:
                    print("It's not a leap year")
            else:
                print("It's a leap year")
        else:
            print("It's not a leap year")

    except:
        # If cant convert to int
        print("Please enter a valid number, you entered", year)


if __name__ == "__main__":
    main()
