def count_consonant(ch):
    if ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u' or ch == 'Y' or ch == 'y':
        return 1
    else:
        return 0

def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    idx = 0
    count_cons = 0
    while idx < len(s):
        count_cons += count_consonant(s[idx])
        idx += 1
    return count_cons