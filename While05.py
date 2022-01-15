def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx = 0
    count_lower = 0
    while idx < len(s):
        if s[idx].islower():
            count_lower += 1
        idx += 1
    return count_lower