# Day 13
import numpy as np
import numba as nb

#%% part 1

with open('13.txt') as notes:
    time = int(notes.readline().strip('\n'))
    busses = np.array([int(bus_id) for bus_id in notes.readline().split(',')
                       if bus_id != 'x'], dtype=int)

bus_arrival_time = np.abs(time % busses - busses)
busses[bus_arrival_time.argmin()] * bus_arrival_time.min()

#%% part 2
# Not done yet
with open('13.txt') as notes:
    notes.readline()
    busses_with_shift = np.array([(int(bus_id), i % int(bus_id))
                                  for i, bus_id in enumerate(notes.readline().split(','))
                                  if bus_id.isnumeric()], dtype=np.int64).T


@nb.njit
def find_t(busses_with_shift, min_val):
    longest_bus = busses_with_shift[:, busses_with_shift[0, :].argmax()]
    min_val = 100000000000000
    (min_val + longest_bus[1]) % longest_bus[0] + min_val

    t = longest_bus[0] * ((min_val // longest_bus[0]) + 1) - longest_bus[1]

    while t < min_val * 100:
        if ((t + busses_with_shift[1, :]) % busses_with_shift[0, :] == 0).all():
            return t
            break
        t += longest_bus[0]


print(find_t(busses_with_shift, 100000000000000))

# %%

longest_bus = busses_with_shift[:, busses_with_shift[0, :].argmax()]
min_val = 100000000000000
(min_val + longest_bus[1]) % longest_bus[0] + min_val

t = longest_bus[0] * ((min_val // longest_bus[0]) + 1) - longest_bus[1]

while t < np.iinfo(np.int64).max - longest_bus[0]:
    if ((t + busses_with_shift[1, :]) % busses_with_shift[0, :] == 0).all():
        print(t)
        break
    t += longest_bus[0]

# %%

longest_bus = busses_with_shift[:, busses_with_shift[0, :].argmax()]
min_val = 100000000000000

((min_val + longest_bus[1]) % longest_bus[0] + min_val + longest_bus[1]) % longest_bus[0]
