from itertools import cycle, islice

with open('../input/10.txt') as f:
	aoc_input = f.read();

def twist(l, curlist, i, s):
    length = len(curlist)
    cycled = cycle(curlist)
    clist = list(islice(cycled, i, i+length))
    clist[0:l] = reversed(clist[0:l])
    return list(islice(cycle(clist), length - i, length - i + length))

def knot_round(lengths, curlist, i, s):
    for l in lengths:
        # print(curlist, l, i, s)
        curlist = twist(l, curlist, i ,s)
        i = (i+l+s) % len(curlist)
        s += 1

    return curlist, i, s

def main():
    inp =  '94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243'
    inp =  '1,2,4'
    # inp =  aoc_input.strip()
    print("input:", inp)
    lengths = [ord(i) for i in inp]
    lengths += [17,31,73,47,23]
    # lenths = [int(i) for i in inp.split(",")]
    size = 256
    curlist = range(size)
    i = 0
    s = 0
    print("lengths:", lengths)

    for j in range(64):
        curlist, i, s = knot_round(lengths, curlist, i, s)
        # print(i,s)

    dense_hash = []
    for i in range(16):
        sublist = curlist[i*16:i*16+16]
        result = None
        for item in sublist:
            if result is None:
                result = item
                continue
            result = result ^ item
        dense_hash.append(result)
    print("dense:", dense_hash)
    print("hash:","".join(["%x" % i for i in dense_hash]))
    
    # print(curlist[0] * curlist[1])
if __name__ == "__main__":
    main()
