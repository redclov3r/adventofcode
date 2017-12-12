from graph_tool.all import *

with open('../input/12.txt') as f:
	aoc_input = f.readlines();

v = {}
g = Graph(directed=False)

def get_vertex(label):
    if label in v:
        return v[label]
    new = g.add_vertex()
    v[label] = new
    return new

def main():
    inp = [
            '0 <-> 2',
            '1 <-> 2',
            '2 <-> 0, 1'
            ]
    inp = aoc_input

    for line in inp:
        line = line.strip()
        startv = get_vertex(line.split(' <-> ')[0])
        ends = line.split(' <-> ')[1].split(', ')
        for end in ends:
            endv = get_vertex(end)
            edge = g.edge(startv, endv, add_missing=True)

    print(len(list(filter(lambda x:x, label_out_component(g, get_vertex('0')).a))))
    comp, hist = label_components(g)
    print(len(hist))

if __name__ == "__main__":
    main()
