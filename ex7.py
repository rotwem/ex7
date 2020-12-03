from typing import *


# PART 1
# can't use any kind of loops


def print_to_n(n: int):
    """receives an int and returns akk ints from 1 to n (if input under 1 prints nothing)"""
    if n < 1:
        return
    print_to_n(n - 1)
    print(n)


def digit_sum(n: int) -> int:
    """receives a positive int and returns the sum of the ints digits (can't use strings)"""
    if 0 <= n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def is_prime(n: int) -> bool:
    """receives an int and returns True\False if the number is prime"""
    return not has_divisor_smaller_than(n, 2)


def has_divisor_smaller_than(n: int, i: int) -> bool:
    """helper for is_prime(n) - checks if n has a divider that is smaller than i"""
    if n <= 2:
        if n == 2:
            return False
        else:
            return True
    if n % i == 0:
        return True
    if i * i > n:
        return False
    return has_divisor_smaller_than(n, i + 1)


# PART 2
# can use loops from here


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any):
    if n <= 0:
        return
    if n == 1:
        hanoi.move(src, dst)
    else:
        play_hanoi(hanoi, n - 1, src, temp, dst)
        hanoi.move(src, dst)
        play_hanoi(hanoi, n - 1, temp, dst, src)


def print_sequences(char_list: List[str], n: int):
    """receives an a string of chars and prints all the potential combinations with n length with repetitions"""
    chosen: List[str] = ["0"] * n
    end = len(char_list) - 1
    _print_sequence_helper(chosen, char_list, 0, n, 0, end)


def _print_sequence_helper(chosen: List[str], char_list: List[str], ind: int, n: int, start: int, end: int):
    if ind == n:
        for i in range(n):
            print(chosen[i], end="")
        print()
        return
    if start > end:
        return
    chosen[ind] = char_list[start]
    _print_sequence_helper(chosen, char_list, ind + 1, n, start, end)
    _print_sequence_helper(chosen, char_list, ind, n, start + 1, end)


def print_no__repetition_sequences(char_list, n):
    """receives an a string of chars and prints all the potential combinations with n length with no repetitions"""
    pass


def parentheses(n):
    """"""
    pass


def flood_fill(image, start):
    """"""
    pass
