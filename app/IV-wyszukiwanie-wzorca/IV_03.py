"""
    Karpa-Rabina
"""

TEXT = \
    """Ea cupidatat consequat fugiat et minim ex enim nostrud dolor ipsum.
Laborum minim fugiat quis sint reprehenderit sit mollit.
Qui tempor veniam ea qui amet ullamco nulla proident amet laborum
commodo nulla laborum. Laboris non commodo culpa incididunt elit.
Sit do consequat aliqua excepteur aliqua elit et laboris excepteur."
    """
PATTERN = "laborum"

d = 256  # alphabet length


def karpa_rabina(text, pattern, prime):
    """ Rabin Karp pattern search

    Args:
        text: string with text
        pattern: pattern to search
        prime: prime number for hashing

    Returns:
        List of positions that pattern has been found on.
    """
    text_length = len(text)
    pattern_length = len(pattern)
    p = 0  # hash for pattern
    t = 0  # hash for text
    h = 1  # hash
    find = []

    for i in range(pattern_length - 1):
        h = (h * d) % prime

    for i in range(pattern_length):
        p = (d*p + ord(pattern[i])) % prime
        t = (d*t + ord(text[i])) % prime

    for i in range(text_length - pattern_length + 1):
        if p == t:
            for j in range(pattern_length):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == pattern_length:
                find.append(i)

        if i < text_length - pattern_length:
            t = (d * (t - ord(text[i]) * h) +
                 ord(text[i + pattern_length])) % prime
            if t < 0:
                t = t + prime

    return find


result = karpa_rabina(TEXT, PATTERN, 101)
print(f"'{PATTERN}' on positions:")
print(result)
print("'elit' on positions:")
print(karpa_rabina(TEXT, "elit", 101))
