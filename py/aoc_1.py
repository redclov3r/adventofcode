with open('../input/1.txt') as f:
    aoc_input = f.read();
    aoc_input = aoc_input[:-1]


# aoc_input = "1234"
# aoc_input = "1221"
# aoc_input = "1212"
# aoc_input = "912121219"


def main():
    aoc_list = list(aoc_input)
    diff = len(aoc_list)/2
    numlist = aoc_list + aoc_list[:diff]
    result = 0
    for i, v in enumerate(numlist):
        # print i,v
        if i >= len(aoc_list):
            continue
        # print 'add', numlist[i], numlist[i+diff]
        if numlist[i] == numlist[i+diff]:
            result += int(v)
    print result
if __name__ == "__main__":
    main()
