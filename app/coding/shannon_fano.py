"""
    Shannona-Fano.
"""
from operator import itemgetter


def shannon_fano(code, freq, Shannon_dict):
    a = {}
    b = {}
    if len(freq) == 1:
        Shannon_dict[freq.popitem()[0]] = code
        return 0
    for i in sorted(freq.items(), key=itemgetter(1), reverse=True):
        if sum(a.values()) < sum(b.values()):
            a[i[0]] = freq[i[0]]
        else:
            b[i[0]] = freq[i[0]]
    shannon_fano(code + "0", a, Shannon_dict)
    shannon_fano(code + "1", b, Shannon_dict)


def main(string):
    Shannon_dict = {}
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    shannon_fano("", freq, Shannon_dict)
    return Shannon_dict


if __name__ == "__main__":
    some_text = "This is some random text"
    sd = main(some_text)
    for char in sd:
        print(f"'{char}' | {sd[char]}")
