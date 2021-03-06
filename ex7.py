from typing import *


# PART 1
# can't use any kind of loops


def print_to_n(n: int) -> None:
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


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    if n <= 0:
        return
    if n == 1:
        hanoi.move(src, dst)
    else:
        play_hanoi(hanoi, n - 1, src, temp, dst)
        hanoi.move(src, dst)
        play_hanoi(hanoi, n - 1, temp, dst, src)


def print_sequences(char_list: List[str], n: int) -> None:
    """receives an a string of chars and prints all the potential combinations with n length with repetitions"""
    if n == 0 or len(char_list) == 0:
        print("")
        return
    if len(char_list) == 1:
        print(char_list[0] * n)
        return
    combinations: List[str] = find_combinations(char_list, n)
    for combo in combinations:
        print(combo)


def find_combinations(char_list: List[str], n: int) -> List[str]:
    if n == 1:
        return char_list
    else:
        combinations: List[str] = []
        add_list = find_combinations(char_list, n - 1)
        for i in range(len(char_list)):
            for j in range(len(add_list)):
                combinations.append(char_list[i] + add_list[j])
        return combinations


def print_no_repetition_sequences(char_list: List[str], n: int) -> None:
    """receives an a string of chars and prints all the potential combinations with n length with no repetitions"""
    if n > len(char_list):
        return
    else:
        _no_repetition_helper("", n, char_list)


def _no_repetition_helper(seq: str, n: int, char_list: List[str]) -> None:
    if n == 0 or len(char_list) == 0:
        print(seq)
        return
    for i in range(len(char_list)):
        _no_repetition_helper(seq + char_list[i], n - 1, char_list[:i] + char_list[i + 1:])


def parentheses(n: int) -> Optional[List[str]]:
    """receives an int and returns all str with valid couples of parentheses"""
    if n < 0:
        return None
    result: List[str] = []
    _parentheses_helper("", n, 0, 0, result)
    return result


def _parentheses_helper(seq: str, n: int, right: int, left: int, result: List[str]) -> None:
    if right == n:
        result.append(seq)
    if left < n:
        _parentheses_helper(seq + "(", n, right, left + 1, result)
    if right < left:
        _parentheses_helper(seq + ")", n, right + 1, left, result)


def flood_fill(image: List[List[str]], start: Tuple[int, int]) -> None:
    """"""
    x, y = start
    if image[x][y] == "*":
        return
    image[x][y] = "*"
    flood_fill(image, (x + 1, y))  # right step
    flood_fill(image, (x, y + 1))  # down step
    flood_fill(image, (x - 1, y))  # left step
    flood_fill(image, (x, y - 1))  # up step
