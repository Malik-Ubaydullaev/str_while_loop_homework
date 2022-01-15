def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum_of_oddNumbers = 0
    idx = 0
    while idx < len(s):
        if s[idx].isdigit():
            if int(s[idx]) % 2 != 0:
                sum_of_oddNumbers += int(s[idx])
        idx += 1
    return sum_of_oddNumbers