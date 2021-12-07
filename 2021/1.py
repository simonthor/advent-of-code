import numpy as np

if __name__ == '__main__':
    depths = np.loadtxt('1.txt')
    print(np.sum(np.diff(depths) > 0))

    cum_depths = depths[:-2] + depths[1:-1] + depths[2:]
    print(np.sum(np.diff(cum_depths) > 0))
