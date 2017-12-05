with open('../input/2.txt') as f:
    aoc_input = f.readlines();

def process_row(row):
    items = list(map(lambda s: int(s), row.strip().split('\t')))
    return max(items) - min(items)

def process_row2(row):
    items = list(map(lambda s: int(s), row.strip().split('\t')))
    for i in range(len(items)):
        for j in range(len(items)):
            if i == j:
                continue
            a = min(items[i], items[j])
            b = max(items[i], items[j])

            if b % a == 0:
                print(b,a)
                return b/a
    raise Exception("ERROR")

def main():
    r = map(process_row2, aoc_input)
    print(sum(r))

if __name__ == "__main__":
    main()
