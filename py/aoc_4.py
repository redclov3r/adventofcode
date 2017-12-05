from itertools import groupby
with open('../input/4.txt') as f:
    aoc_input = f.readlines();

def is_valid(words):
    a = sorted(map(lambda word: "".join(sorted(word)),words))
    valid = all(map(lambda c: c == 1, [len(list(group)) for key, group in groupby(a)]))
    if valid:
        return 1
    return 0

def main():
    rows = list(map(lambda row: is_valid(row.strip().split(" ")), aoc_input))
    print(sum(rows))

if __name__ == "__main__":
    main()
