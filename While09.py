def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum_numbers = 0
    idx = 0
    while idx < len(s):
        if s[idx].isdigit():
            sum_numbers += int(s[idx])
        idx += 1
    return sum_numbers