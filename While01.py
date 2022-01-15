from curses.ascii import isdigit


def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx = 0
    count_number = 0
    while idx < len(s):
        if s[idx].isdigit():
            count_number += 1
        idx += 1
        
    return count_number