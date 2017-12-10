import re

regex = r"(?P<reg>\w+) (?P<op>(inc)|(dec)) (?P<sign>-)?(?P<value>\d+) if (?P<creg>\w+) (?P<cmp>[!<>=]+) (?P<csign>-)?(?P<cvalue>\d+)"

with open('../input/8.txt') as f:
	aoc_input = f.readlines();

def process(matches, reg):
    cvalue = int(matches.group('cvalue'))
    if matches.group('csign'):
        cvalue = cvalue * -1

    creg = reg.get(matches.group('creg'), 0)
    c = matches.group('cmp')
    comparison = False
    if c == '==':
        comparison = creg == cvalue
    if c == '!=':
        comparison = not(creg == cvalue)
    if c == '>':
        comparison = creg > cvalue
    if c == '>=':
        comparison = creg >= cvalue
    if c == '<':
        comparison = creg < cvalue
    if c == '<=':
        comparison = creg <= cvalue

    if not comparison:
        return

    value = int(matches.group('value'))
    if matches.group('sign'):
        value = value * -1

    r = reg.get(matches.group('reg'), 0)
    op = matches.group('op')
    if op == 'inc':
        reg[matches.group('reg')] = r + value
    if op == 'dec':
        reg[matches.group('reg')] = r - value



def main():
    reg = {}
    # aoc_input = [
            # 'b inc 5 if a > 1',
            # 'a inc 1 if b < 5',
            # 'c dec -10 if a >= 1',
            # 'c inc -20 if c == 10',
            # ]
    totalmax = 0
    curmax = 0
    for line in aoc_input:
        line = line.strip()
        matches = re.search(regex, line)
        process(matches, reg)
        if reg.values():
            curmax = max(reg.values())
        totalmax = max(totalmax, curmax)

    print(reg)
    print(totalmax)

if __name__ == "__main__":
    main()
