from operator import add

class Grid():
    def __init__(self):
        self.fields = {}
        self.set_value((0,0), 1)

    def set_value(self, coord, value):
        key = "%d,%d" % coord
        self.fields[key] = value

    def get_value(self, coord):
        key = "%d,%d" % coord
        return self.fields.get(key, 0)

def adjacent(coord):
    x = coord[0]
    y = coord[1]
    return [(x-1, y-1),(x, y-1),(x+1, y-1),(x-1, y),(x, y),(x+1, y),(x-1, y+1),(x, y+1),(x+1, y+1),]

def turn_left(direction):
    if direction == (0,1):
        return (-1, 0)
    if direction == (-1,0):
        return (0, -1)
    if direction == (0,-1):
        return (1, 0)
    if direction == (1,0):
        return (0, 1)

    raise Exception("ERROR")

def step(coord, direction):
    return tuple(map(add, coord, direction))

def main():
    g = Grid()
    cur = (1,0)
    direction = (0,1)
    i = 1
    result = 0
    while result < 289326:
        result = sum(map(g.get_value, adjacent(cur)))
        g.set_value(cur, result)

        left_direction = turn_left(direction)
        if g.get_value(step(cur, left_direction)) == 0:
            direction = left_direction

        cur = step(cur, direction)
        i = i+1

    print(i, result)


if __name__ == "__main__":
    main()
