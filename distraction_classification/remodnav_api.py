import remodnav
import inspect

"""
    This is mostly copypasta
"""
__version__ = '1.0'

import logging
lgr = logging.getLogger('remodnav')

import sys
import numpy as np

from remodnav import clf
from remodnav.clf import EyegazeClassifier, events2bids_events_tsv


def remodnav_api(x, y, px2deg=0.02, rate=20, **kwargs):
    
    kwargs = {}
    for func in (EyegazeClassifier.__init__, EyegazeClassifier.preproc):
        # pull kwargs and their defaults out of the function definitions
        argspec = inspect.getargspec(func)
        kwargs.update(zip(argspec.args[::-1], argspec.defaults[::-1]))

    kwargs['px2deg'] = px2deg
    kwargs['sampling_rate'] = rate    


    data = np.recfromcsv(
        args.infile,
        delimiter='\t',
        names=['x', 'y'],
        usecols=[0, 1])
    lgr.info('Read %i samples', len(data))

    clf = EyegazeClassifier(
        **{k: kwargs[k] for k in (
            'px2deg', 'sampling_rate', 'velthresh_startvelocity',
            'min_intersaccade_duration', 'min_saccade_duration',
            'min_pursuit_duration', 'pursuit_velthresh',
            'max_initial_saccade_freq', 'saccade_context_window_length',
            'max_pso_duration', 'min_fixation_duration', 'lowpass_cutoff_freq',
            'noise_factor')}
    )

    pp = clf.preproc(
        data,
        **{k: getattr(args, k) for k in (
            'min_blink_duration', 'dilate_nan', 'median_filter_length',
            'savgol_length', 'savgol_polyord', 'max_vel')}
    )

    events = clf(pp, classify_isp=True, sort_events=True)

    events2bids_events_tsv(events, args.outfile)

if __name__ == "__main__":
    remodnav_api([1,2,3],[1,2,3], foo="bar")