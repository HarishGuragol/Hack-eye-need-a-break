import numpy as np
from scipy import interpolate

DELTA_T = 50 # ms
BLOCK = 1000 # ms
CUTOFF = 5 # min

"""
    interpolate x/y data to make it equally spaced in time
    data: [[x,y,t],[x,y,t],...]
    dt: target time step
    return: x (list), y(list) spaced by dt, and t (an arange)
"""
def make_data_equidistant(data, dt):

    x_coord = [d[0] for d in data]
    y_coord = [d[1] for d in data]
    times = [d[2] for d in data]

    f_x = interpolate.interp1d(times, x_coord)
    f_y = interpolate.interp1d(times, y_coord)

    t_min = times[0]
    t_max = times[-1]
    #t_range = (t_max - t_min) / 60 # in s

    t_new = np.arange(np.ceil(t_min), np.ceil(t_max), dt)
    x_new = f_x(t_new)
    y_new = f_y(t_new)

    return x_new, y_new, t_new

"""
    average series over blocks of num elements
    series: list
    num: int
    return: list of length len(series)/num
"""
def average_blocks(series, num):
    num_chunks = len(series)/num
    series_split = np.array_split(series, num_chunks)
    new_series = [np.mean(chunk) for chunk in series_split]
    return new_series

"""
    apply cutoff: discard data older than CUTOFF minutes
    assuming data is sorted from oldest to latest (otherwise change -1 to 0)
    data: [[x,y,t],[x,y,t],...]
    cutoff: cutoff in min
    return: data [[x,y,t],[x,y,t],...] with times within cutoff
"""
def apply_cutoff(data, cutoff):
    latest = data[-1][2]
    cutoff_ms = cutoff * 60000
    data_filtered = [d for d in data if latest - d[2] <= cutoff_ms]
    return data_filtered

"""
    Calculate standard deviation of 2D data
    x,y: lists with x/y coordinates, equidistant in time
    result: standard dev.
"""
def calc_std(x, y):
    mean = [np.mean(x), np.mean(y)]
    dist = [np.sqrt((xx-mean[0])**2 + (yy-mean[1])**2) for xx,yy in zip(x,y)]
    std = np.std(dist)
    return std

"""
    Calculate standard dev of random numbers
"""
def calc_random_std(x, y, width, height):
    rand_x = np.random.randint(low=1, high=width, size=len(x))
    rand_y = np.random.randint(low=1, high=height, size=len(x))
    rand_std = calc_std(rand_x, rand_y)
    return rand_std

"""
    calculate distraction score from gaze coordinates and sensitivity
    data: [[x,y,t],[x,y,t],...]
    sensitivity: float between 0 and 1
    return: score (float between 0 and 1)
"""
def score_random(data, width, height):

    return np.random.rand()

def score_variance(data, width, height):

    # discard data older than cutoff
    data = apply_cutoff(data, CUTOFF)

    # reshuffle data to x (list) and y (list) equidistant in time
    x, y, t = make_data_equidistant(data, DELTA_T)

    #num = BLOCK / DELTA_T
    #x_avg = average_blocks(x, num)
    #y_avg = average_blocks(y, num)

    std = calc_std(x, y)
    std_random = calc_random_std(x, y, width, height)

    # calculate score + apply threshold
    score = std / std_random

    return score

"""
    TODO: try remodnav package for feature extraction
"""
def score_remodnav(data, width, height):

    x, y, t = make_data_equidistant(data, DELTA_T)
    
    return np.nan

def score(data, width, height):
    return score_variance(data, width, height)

"""
    Transform uniform score to discrete classifier
    For now we use a linear scale which may not be the best choice in the long run...
"""
def is_distracted(score, sensitivity):
    if score > 1 - sensitivity:
        return True
    else:
        return False


"""
    Testing with dummy data
"""
if __name__ == "__main__":
    data = np.loadtxt("dummy_data.txt", delimiter=",")
    score = score_variance(data, 1901, 1034)
    print(score)
    distracted = is_distracted(score, 0.9)
    print(distracted)
