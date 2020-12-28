# Day 5
import numpy as np
#%% part 1

with open('5.txt') as seat_file:
    seats = seat_file.read()
bin_seats = seats.replace('F', '0')
bin_seats = bin_seats.replace('B', '1')
bin_seats = bin_seats.replace('L', '0')
bin_seats = bin_seats.replace('R', '1')
rows = np.array([int(s[:-3], base=2) for s in bin_seats.split('\n')], dtype=int)
columns = np.array([int(s[-3:], base=2) for s in bin_seats.split('\n')], dtype=int)
seat_id = np.array([int(s, base=2) for s in bin_seats.split('\n')])

print((rows*8+columns).max(), seat_id.max())    # Both should produce same output

#%% part 2

seat_id.sort()
print(seat_id[np.append(np.diff(seat_id) != 1, False)] + 1)
