def count_punctuation(ch):
    if ch == ',' or ch == '.' or ch == ';' or ch == ':' or ch == '?' or ch == '!':
        return 1
    else:
        return 0    
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx = 0
    count_punct = 0
    while idx < len(s):
        count_punct += count_punctuation(s[idx])
        idx += 1
    return count_punct