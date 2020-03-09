#
# This script wraps around `residency_match.py`, runs several sets of simulations,
# and then saves the results to files.
#
# Each set of simulations is described using a file name and a corresponding 
# alias, which is a name used to describe the simulation set in the plot we generate
# using `make_plots.py`.
#
# SPECIFYING A SET OF SIMULATIONS
# The parameters used in the simulation set are specified in the filename.
# The parameters are separated by an underscore. For example, 10_2_0point2.csv
# details the case where there are `10` interviews per residency spot, applicants apply to
# all programs in `2` specialties, and the probability distribution determining specialty
# preference has noise equal to number of spots in a given specialty divided by `0.2`.
#
# Sohrab Towfighi 2020
#
import os
import sys
import pdb
try:
    import sh
except ImportError:
    # fallback: emulate the sh API with pbs
    import pbs

    class Sh(object):
        def __getattr__(self, attr):
            return pbs.Command(attr)
    sh = Sh()

files = ["10_2_0point2.csv", 
         "2_2_0point2.csv", 
         "20_2_0point2.csv", 
         "10_2_10.csv", 
         "10_4_0point2.csv", 
         "10_1_0point2.csv"]
aliases = ['Baseline', 
           'Two interviews\nper spot',
           'Twenty interviews\nper spot', 
           'Applicants choose\nspecialties perfectly', 
           'Applicants apply\nto four specialties', 
           'Applicants apply\nto one specialty']

if __name__ == '__main__':
    args = sys.argv[1:]
    if args[0] == 'test':
        n_runs = 10
    else:
        n_runs = 10000
    for file in files:
        sh.touch(file)
        sh.rm(file)
        args = file.split('_')
        arg0 = int(args[0])
        arg1 = int(args[1])
        arg2 = args[2]
        arg2 = arg2[:-4]
        if arg2 == '0point2':
            arg2 = 0.2
        else:
            arg2 = float(arg2)
        sh.python('residency_match.py', arg0, arg1, arg2, n_runs, file, _fg=True)
