# Day 12
#%% part 1

class Ship:
    def __init__(self, start_direction: str, start_position: complex):
        # TODO: change start_position to tuple of str
        self.direction_converter = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
        self.rotation_converter = {'L': 1j, 'R': -1j}
        self.direction = self.direction_converter[start_direction]
        self.start_position = start_position
        self.position = start_position

    def move(self, instructions: list):
        # TODO: to make this efficient, I should probably convert all instructions to numbers first
        # TODO: use reduce?
        for i in instructions:
            instruction, amount = i[0], int(i[1:])
            if instruction in self.rotation_converter.keys():
                self.direction *= self.rotation_converter[instruction] ** (amount // 90)
            elif instruction in self.direction_converter.keys():
                self.position += self.direction_converter[instruction] * amount
            elif instruction == 'F':
                self.position += self.direction * amount
            else:
                raise KeyError(f"invalid instruction '{instruction}'")

    @property
    def manhattan_distance(self):
        complex_distance = self.position - self.start_position
        return abs(complex_distance.real) + abs(complex_distance.imag)


with open('12.txt') as instruction_file:
    instructions = instruction_file.read().split('\n')
ferry = Ship(start_direction='E', start_position=0)
ferry.move(instructions)
print(ferry.manhattan_distance)


#%% part 2

class WayPointShip(Ship):
    def __init__(self, start_position: complex, start_waypoint: complex, start_direction: str = 'E'):
        # start_direction will not be used by this class
        super().__init__(start_direction, start_position)
        # TODO: change waypoint to tuple of str and convert to complex
        self.waypoint = start_waypoint

    def move(self, instructions: list):
        for i in instructions:
            instruction, amount = i[0], int(i[1:])
            if instruction in self.rotation_converter.keys():
                self.waypoint *= self.rotation_converter[instruction] ** (amount // 90)
            elif instruction in self.direction_converter.keys():
                self.waypoint += self.direction_converter[instruction] * amount
            elif instruction == 'F':
                self.position += self.waypoint * amount
            else:
                raise KeyError(f"invalid instruction '{instruction}'")


waypoint_ferry = WayPointShip(start_position=0, start_waypoint=10 + 1j)
waypoint_ferry.move(instructions)
print(waypoint_ferry.manhattan_distance)
