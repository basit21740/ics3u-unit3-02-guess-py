#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Nov 2021
# this program does the number guessing game


def main():
    # this program is the number guessing game

    guess = int(input("Enter a number between 0-9: "))

    if guess == 4:
        print("You guessed right!")
        print("")
    if guess is not 4:
        print("You guessed wrong!")
        print("")


if __name__ == "__main__":
    main()
    print("Done.")
