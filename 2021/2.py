def part1(instructions):
    position = 0 + 0j
    dir2num = {'forward': 1j, 'down': 1, 'up': -1}

    for motion in instructions:
        direction, length = motion.split(' ')
        position += dir2num[direction] * int(length.strip('\n'))
    print(position.real * position.imag)

    return position


def part2(instructions):
    position = 0 + 0j
    aim = 0
    for motion in instructions:
        direction, length = motion.split(' ')
        length = int(length.strip('\n'))
        assert length
        if direction == 'forward':
            position += length * (1j + aim)
        elif direction == 'down':
            aim += length
        elif direction == 'up':
            aim -= length

    print(position.real * position.imag)
    return position

if __name__ == '__main__':
    with open('2.txt') as instructions:
        part1(instructions)
    with open('2.txt') as instructions:
        part2(instructions)