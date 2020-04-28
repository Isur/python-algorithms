"""
    Konwersja odwrotnej notacji polskiej (w obie strony)
"""

operators = ["+", "-", "/", "*", "(", ")", "^", "~", "="]


def operator_value(a):
    if a in ["^"]:
        a = 5
    elif a in ["/", "*", "~"]:
        a = 4
    elif a in ["+", "-"]:
        a = 3
    elif a in ["("]:
        a = 2
    elif a in ["="]:
        a = 1
    else:
        a = 0
    return a


def compare_operators(a, bs):
    """
    Compare operator with first operator from stack
    returns true only if a is bigger then bs[0]
    or bs is empty
    """
    if bs == [] or a == "(":
        return True
    b = bs[0]
    v1 = operator_value(a)
    v2 = operator_value(b)

    return v1 > v2


def reverse_polish_notation(arg):
    """
    Args:
        str: string with normal notation

    Returns:
        string with reverse polish notation
    """
    chars = []
    ops = []
    print()
    print("Normal: ", end=" ")
    print(arg)
    for char in arg:
        if char in operators:
            if char == ")":
                while True:
                    x = ops.pop(0)
                    if x == "(":
                        break
                    chars.append(x)
            else:
                tmp = char
                while True:
                    if compare_operators(tmp, ops):
                        ops.insert(0, char)
                        break
                    else:
                        tmp = ops.pop(0)
                        chars.append(tmp)
        else:
            chars.append(char)
    final = "".join(chars)
    final += "".join(ops)

    print("RPN:", end=" ")
    print(final)
    return final


def normal_notation(arg):
    """
    Args:
        str: string with reverse polish notation

    Returns:
        string with normal notation
    """
    print()
    s = []
    for char in arg:
        if char not in operators:
            s.insert(0, char)
        else:
            o1 = s[0]
            s.pop(0)
            o2 = s[0]
            s.pop(0)
            s.insert(0, f"({o2}{char}{o1})")

    print(f"RPN: {arg}")
    print(f"Normal: {s[0]}")
    return s[0]


q1 = 'a+b*(c-d)'
q2 = "(2+3)*5"
q3 = "3+4*2/(1-5)^2"
q4 = "x^y/(5*z)+1"
r1 = reverse_polish_notation(q1)
r2 = reverse_polish_notation(q2)
r3 = reverse_polish_notation(q3)
r4 = reverse_polish_notation(q4)
n1 = normal_notation(r1)
n2 = normal_notation(r2)
n3 = normal_notation(r3)
n4 = normal_notation(r4)
