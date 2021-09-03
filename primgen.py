import argparse
import math
import random


def miller_rabin_method(odd_integer: int, p: float) -> bool:
    """
    Implement the Miller-Rabin primality test
    :param odd_integer: a odd number
    :param p: probability of success
    :return: True if odd_integer is a probably primer number, False otherwise
    """
    rounds = int(-math.log2(1 - p))

    if odd_integer == 2:
        return True

    if odd_integer % 2 == 0:
        return False

    r, s = 0, odd_integer - 1

    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(rounds):
        witness = random.randrange(2, odd_integer - 1)
        x = pow(witness, s, odd_integer)
        if x == 1 or x == odd_integer - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, odd_integer)
            if x == odd_integer - 1:
                break
        else:
            return False

    return True


def random_odd_integer(bits: int) -> int:
    """
    Generate a odd integer of bits of length

    :param bits: number of bits that must be the odd integer
    :return n: a odd integer of length bits
    """
    n = random.randint(2 ** (bits - 1), 2 ** bits - 1)

    if n % 2 == 0:
        n += 1

    return n


def generate_probable_prime_number(bits: int, success_probability: float) -> int:
    """
    Generate a probable prime number of length "bits" and "success_probability"
    :param bits: length of the probable prime number
    :param success_probability: probability of success between (0, 1)
    :return: a probable prime number
    """
    probable_prime_number = random_odd_integer(bits)

    while miller_rabin_method(probable_prime_number, success_probability) is False:
        probable_prime_number += 2

    return probable_prime_number


def cast(number):
    """
    if number is str then typecasting according to int or float, if number is float
    typecasting to int
    :param number: str with a number (int or float) or any number
    :return: int or float
    """
    for t in (int, float):
        try:
            n = t(number)
            return n
        except ValueError:
            pass


def check_bits(parameter):
    value = cast(parameter)

    if type(value) is not int or value < 0:
        msg = "bits must be a positive integer"
        raise argparse.ArgumentTypeError(msg)

    return value


def check_probability(parameter):
    value = cast(parameter)

    if value <= 0 or value >= 1:
        msg = "probability must by a float between (0, 1)"
        raise argparse.ArgumentTypeError(msg)

    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="primgen",
        description="This module allows you to find a probably prime number given a length in bits and a probability "
                    "of success"
    )

    parser.add_argument(
        "-b", "--bits",
        help="int >0: Specify the number of bits length of the prime number",
        type=check_bits,
        required=True
    )

    parser.add_argument(
        "-p", "--probability",
        help="float between (0, 1): Specify a probability of success",
        type=check_probability,
        required=True
    )

    args = parser.parse_args()

    print(generate_probable_prime_number(args.bits, args.probability))
