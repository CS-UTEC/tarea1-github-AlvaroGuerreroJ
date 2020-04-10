#!/usr/bin/env python3
import math
import sys


def main():
    try:
        number = int(input("Give me a positive number: "))
    except ValueError:
        print("Not a valid number!", file=sys.stderr)
        return

    if number < 1:
        print("The number must be positive!", file=sys.stderr)

    if is_prime(number):
        print("Prime")
    else:
        print("Not prime")


def is_prime(n: int):
    return all(n % a != 0 for a in range(2, int(math.floor(n**.5)) + 1))


if __name__ == '__main__':
    main()
