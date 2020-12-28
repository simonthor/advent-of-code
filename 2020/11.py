# Day 11
import numpy as np
import numba as nb

#%% part 1

original_seat_state = []
with open('11.txt') as original_seat_file:
    for row in original_seat_file:
        original_seat_state.append(list(row)[:-1])

state_str_withoutpad = np.array(original_seat_state, dtype=str)
state_str = np.full(np.array(state_str_withoutpad.shape)+2, '.')
state_str[1:-1, 1:-1] = state_str_withoutpad
state = np.zeros(state_str.shape, dtype=bool)
seat_locs = np.array((state_str == 'L').nonzero()).T


@nb.njit
def next_seat_configuration(seat_locs, state):
    new_state = state.copy()
    for index in (seat_locs):
        seats_around = state[index[0]-1:index[0]+2, index[1]-1:index[1]+2]
        if (state[index[0], index[1]]
            and (seats_around.sum() >= 5)):
            new_state[index[0], index[1]] = False
        elif not seats_around.any():
            new_state[index[0], index[1]] = True
    return new_state


while True:
    new_state = next_seat_configuration(seat_locs, state)
    if (state == new_state).all():
        print((state == True).sum())
        break
    state = new_state

#%% part 2
# Not done yet

#%%

#@nb.njit
def find_seats_around(seat_locs, state, index):
    seats_around = np.zeros((2, 8), dtype=int)
    for i, motion in enumerate(np.array([[0, 1], [0, -1], [1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, 1]], dtype=int)):
        diagonal = index + motion
        while (state_str[tuple(diagonal)] == '.') and ((0 < diagonal) & (diagonal < np.array(state.shape)-1)).all():
            diagonal += motion
        seats_around[:, i] = diagonal
    return seats_around

#@nb.njit
#def next_seat_configuration2(seat_locs, state):
#    new_state = state.copy()
#    for index in (seat_locs):
#        seats_around = find_seats_around(seat_locs, state, index)
#        if (state[index[0], index[1]] and (seats_around.sum() >= 6)):
#            new_state[index[0], index[1]] = False
#        elif not seats_around.any():
#            new_state[index[0], index[1]] = True
#    return new_state

def next_seat_configuration2(seat_locs, all_seats_around, state):
    new_state = state.copy()
    for seat, seats_around in zip(seat_locs, all_seats_around):
        if (state[tuple(seat)] and (state[seats_around[0, :], seats_around[1, :]].sum() >= 6)):
            new_state[tuple(seat)] = False
        elif not state[seats_around[0, :], seats_around[1, :]].any():
            new_state[tuple(seat)] = True
    return new_state

#%%

all_seats_around = np.zeros((*seat_locs.shape, 8), dtype=int)
for i, seat in enumerate(seat_locs):
    all_seats_around[i, ...] = find_seats_around(seat_locs, state, seat)

#%%

i = 0
while i < 100:
    new_state = next_seat_configuration2(seat_locs, all_seats_around, state)
    if (state == new_state).all():
        print(state.sum())
        break
    state = new_state
    i += 1

#%%

seat_locs = np.array((state_str == 'L').nonzero()).T + 1
# Only allow 100 loops as it should not do require more than that. Mainly for debugging purposes
i=0
while i < 100:
    new_state = next_seat_configuration2(seat_locs, state)
    if (state == new_state).all():
        print(state.sum())
        break
    state = new_state
    i += 1
