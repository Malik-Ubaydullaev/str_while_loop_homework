def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count_evenNumber = 0
    idx = 0
    while idx < len(s):
        if s[idx].isdigit():
            if int(s[idx]) % 2 == 0:
                count_evenNumber += 1
        idx += 1
    return count_evenNumber