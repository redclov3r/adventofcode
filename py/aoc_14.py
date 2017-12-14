from aoc_10 import knot_hash

def unhexlify(h):
    return '{0:020b}'.format(int(h, 16)).rjust(128, '0')

with open('../input/12.txt') as f:
	aoc_input = f.readlines();


def main():
    inp = 'ljoxqyyw'
    grid = [unhexlify(knot_hash('%s-%s' % (inp, i))) for i in range(128)]

    print(sum([sum([int(c) for c in row]) for row in grid]))

if __name__ == "__main__":
    main()
