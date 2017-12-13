from functools import reduce

with open('../input/11.txt') as f:
	aoc_input = f.read();

def step(start, direction):
    goal = start[0]
    if direction == 'n':
        goal['y'] += 1
        goal['z'] -= 1
    if direction == 'ne':
        goal['x'] += 1
        goal['z'] -= 1
    if direction == 'se':
        goal['x'] += 1
        goal['y'] -= 1
    if direction == 's':
        goal['y'] -= 1
        goal['z'] += 1
    if direction == 'sw':
        goal['x'] -= 1
        goal['z'] += 1
    if direction == 'nw':
        goal['x'] -= 1
        goal['y'] += 1

    return (goal, max(start[1], distance(goal)))

def distance(node):
    return max([abs(v) for v in node.values()])

def main():
    inp =  'ne,ne,s,s'
    inp =  aoc_input.strip()
    dirs = inp.split(',')
    start = {'x': 0, 'y': 0, 'z': 0}

    print(reduce(step, dirs, (start, 0)))

if __name__ == "__main__":
    main()
