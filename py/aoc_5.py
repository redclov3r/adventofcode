with open('../input/5.txt') as f:
    aoc_input = f.readlines();

def main():
    instructions = list(map(int, aoc_input))
    # instructions = [0,3,0,1,-3]
    count = len(instructions)
    pointer = 0
    i = 0
    error = False
    while not error:
        instruction = instructions[pointer]
        new_pointer = pointer + instruction
        i = i + 1
        if new_pointer not in range(count):
            error = True
            print("ERROR at Instruction #%d, going from %d to %d" % (i, pointer, new_pointer))
            continue
        # print("Instruction #%d, Pointer from %d to %d" % (i, pointer, new_pointer))
        if instruction >= 3:
            instructions[pointer] = instruction - 1
        else:
            instructions[pointer] = instruction + 1
        pointer = new_pointer

if __name__ == "__main__":
    main()
