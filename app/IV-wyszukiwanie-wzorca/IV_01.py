"""
    Naive Pattern Search
"""

TEXT = \
    """Ea cupidatat consequat fugiat et minim ex enim nostrud dolor ipsum.
Laborum minim fugiat quis sint reprehenderit sit mollit.
Qui tempor veniam ea qui amet ullamco nulla proident amet laborum
commodo nulla laborum. Laboris non commodo culpa incididunt elit.
Sit do consequat aliqua excepteur aliqua elit et laboris excepteur."
    """
PATTERN = "laborum"


def naive_pattern_search(text, pattern):
    """ Naive pattern search

    Args:
        text: string with text
        pattern: pattern to search

    Returns:
        List of positions that pattern has been found on.
    """
    text_lenght = len(text)
    pattern_length = len(pattern)
    find = []
    for i in range(text_lenght - pattern_length + 1):
        for j in range(pattern_length):
            if pattern[j] != text[i + j]:
                break
        if j == pattern_length - 1:
            find.append(i)

    return find


result = naive_pattern_search(TEXT, PATTERN)
print(f"'{PATTERN}' on positions:")
print(result)
print("'Ea' on positions:")
print(naive_pattern_search(TEXT, "Ea"))
