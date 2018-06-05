def length_of_longest_substring(s):
    """
    return the length of longest substring

    Args:
        s: string
    Returns:
        length: int
    Raises:
        None
    """
    start = 0
    max_length = 0
    dic = {}
    for i, char in enumerate(s):
        if char in dic:
            max_length = max(i - start, max_length)
            start = dic[char] + 1 if start <= dic[char] else start
            dic[char] = i
        else:
            dic[char] = i
    max_length = max(max_length, dic[s[-1]] - start + 1)
    return max_length
