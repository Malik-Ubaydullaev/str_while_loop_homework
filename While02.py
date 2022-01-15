def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count_alpha = 0
    idx = 0
    while idx < len(s):
        if s[idx].isalpha():
            count_alpha += 1
        idx += 1
    return count_alpha