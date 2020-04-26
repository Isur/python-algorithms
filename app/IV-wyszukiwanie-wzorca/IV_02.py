"""
    Boyer-Moore
"""

TEXT = \
    """Ea cupidatat consequat fugiat et minim ex enim nostrud dolor ipsum.
Laborum minim fugiat quis sint reprehenderit sit mollit.
Qui tempor veniam ea qui amet ullamco nulla proident amet laborum
commodo nulla laborum. Laboris non commodo culpa incididunt elit.
Sit do consequat aliqua excepteur aliqua elit et laboris excepteur."
    """
PATTERN = "laborum"


def helper(pattern, symbol):
    """ Returns last occurence of symbol in text"""
    pos = -1
    for i in range(len(pattern)):
        if pattern[i] == symbol:
            pos = i
    return pos


def boyer_moore(text, pattern):
    """ Boyer-Moore pattern search

    Args:
        text: string with text
        pattern: pattern to search

    Returns:
        List of positions that pattern has been found on.
    """
    text_lenght = len(text)
    pattern_length = len(pattern)
    find = []
    i = pattern_length - 1
    j = pattern_length - 1
    while True:
        if pattern[j] == text[i]:
            if j == 0:
                find.append(i)
                i += pattern_length
            else:
                i -= 1
                j -= 1
        else:
            i = i + pattern_length - min(j, 1 + helper(pattern, text[i]))
            j = pattern_length - 1
            if i > text_lenght - 1:
                break
    return find


result = boyer_moore(TEXT, PATTERN)
print(f"'{PATTERN}' on positions:")
print(result)
print("'elit' on positions:")
print(boyer_moore(TEXT, "elit"))