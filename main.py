import random


def miller_rabin_method(largest_odd_integer: int, rounds: int):
    if largest_odd_integer == 2:
        return True

    if largest_odd_integer % 2 == 0:
        return False

    r, s = 0, largest_odd_integer - 1

    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(rounds):
        a = random.randrange(2, largest_odd_integer - 1)
        x = pow(a, s, largest_odd_integer)
        if x == 1 or x == largest_odd_integer - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, largest_odd_integer)
            if x == largest_odd_integer - 1:
                break
        else:
            return False

    return True


def random_odd_integer(bits: int):
    """
    Generate a odd integer of bits of length

    :param bits: number of bits that must be the odd integer
    :return n: a odd integer of length bits
    """
    n = random.randint(2 ** (bits - 1), 2 ** bits - 1)

    if n % 2 == 0:
        n += 1

    return n


def generate_probable_prime_number(bits: int):
    probable_prime_number = random_odd_integer(bits)

    while miller_rabin_method(probable_prime_number, 40) is False:
        probable_prime_number += 2

    return probable_prime_number


print(generate_probable_prime_number(1024))
