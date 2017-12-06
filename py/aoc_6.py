with open('../input/6.txt') as f:
    aoc_input = f.read();

def get_largest(mem):
    return list(sorted(enumerate(mem), key=lambda a: a[1], reverse=True))[0][0]

def save(mem, s, i):
    s[','.join(map(str,mem))] = i

def exists(mem, s):
    return ','.join(map(str,mem)) in s.keys()

def load(mem, s):
    return s[','.join(map(str,mem))]

def realloc(mem, i):
    l = len(mem)
    value = mem[i]
    mem[i] = 0
    base = value // l
    rest = value % l
    for j in range(l):
        added = base
        if 1 <= (j-i) % l <= rest:
            added = added + 1
        mem[j] = mem[j] + added

    return mem

def main():
    mem = list(map(int, aoc_input.strip().split('\t')))
    s = {}
    counter = 0
    while not exists(mem,s):
        save(mem,s,counter)
        i = get_largest(mem)
        mem = realloc(mem, i)
        counter = counter + 1
        print(counter, mem)
    start = load(mem, s)
    print(start, counter - start)

if __name__ == "__main__":
    main()
