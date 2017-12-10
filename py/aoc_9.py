from lark import Lark, Transformer

with open('../input/9.txt') as f:
	aoc_input = f.read();

class GroupTransformer(Transformer):
    def group(self, items):
        return sum(items)
        return list([i for i in items if type(i) is list])

    def garbage(self, items):
        if items:
            return len(items[0])
        return 0

    def char(self, x):
        return x[0]

    def string(self, c):
        return "".join(c)


def score(l, base = 0):
    lscore = base + 1
    return lscore + sum([score(c, lscore) for c in l])

def main():
    parser = Lark(r"""
        group: "{" [_inner_group ("," _inner_group)*] "}"
        garbage: "<" [(ignore | string)] ">"
        _inner_group: group | garbage

        char: /[a-z<{},"']/
        string: char+
        ignore: "!" (char | ">")

        %import common.WS
        %ignore WS
    """, start='group')

    text = '{{<a},{<a>},{<a>},{<a>}}'
    text = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
    # text = '{{<!>},<!>},{<!>},{<a>}}'
    # text = '{<{!>}>}'
    text = aoc_input
    def preprocess(string):
        def it(string):
            c = 0
            while c < len(string):
                char = string[c]
                if char == "!":
                    c += 2
                    continue
                yield(char)
                c += 1
        return "".join(list(it(string)))

    ptext = preprocess(text)
    tree = parser.parse(ptext)
    lists = GroupTransformer().transform(tree)
    print(lists)


if __name__ == "__main__":
    main()
