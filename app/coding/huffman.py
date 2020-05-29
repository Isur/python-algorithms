"""
    Huffmana.
"""


class Tree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return f"{self.left}_{self.right}"


def Huffman(node, left=True, s=""):
    if type(node) is str:
        return {node: s}

    l, r = node.children()
    d = dict()
    d.update(Huffman(l, True, s+"0"))
    d.update(Huffman(r, False, s+"1"))
    return d


def main(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    nodes = freq

    while len(nodes) > 1:
        k1, c1 = nodes[-1]
        k2, c2 = nodes[-2]
        nodes = nodes[:-2]
        node = Tree(k1, k2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    code = Huffman(nodes[0][0])
    return code


if __name__ == "__main__":
    some_text = "This is some random text."
    coded = main(some_text)
    for char in coded:
        print(f"'{char}' | {coded[char]}")
