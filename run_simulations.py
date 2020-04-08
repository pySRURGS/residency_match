'''
 This script wraps around `residency_match.py`, runs several sets of 
 simulations, and then saves the results to files.

 Each set of simulations is described using a file name and a corresponding 
 alias, which is a name used to describe the simulation set in the plot we 
 generate using `make_plots.py`.

 Sohrab Towfighi 2020
'''
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

# Here, we list the files which will be generated. 
# The naming convention is that the filename specifies the values used in the 
# simulations.
# Parameter values are separated by underscores in the filename.
# For example, 10_2_5.csv
# details the case where there are `10` interviews per residency spot, 
# applicants apply to all programs in `2` specialties, and the probability 
# distribution determining specialty preference has noise equal to number of 
# spots in a given specialty times `5`.

files = ["10_2_5.csv", 
         "2_2_5.csv", 
         "20_2_5.csv", 
         "10_2_0point1.csv", 
         "10_4_5.csv", 
         "10_1_5.csv"]
         
# for each file, there is a corresponding human-readable alias which is used 
# when generating the plots 
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
        n_interviews_per_spot = int(args[0])
        n_spec_per_applicant = int(args[1])
        specialty_choice_stddev_multiplier = args[2]
        specialty_choice_stddev_multiplier = specialty_choice_stddev_multiplier[:-4]
        if specialty_choice_stddev_multiplier == '0point1':
            specialty_choice_stddev_multiplier = 0.1
        else:
            specialty_choice_stddev_multiplier = float(specialty_choice_stddev_multiplier)
        sh.python3('residency_match.py', '-n_interviews_per_spot', 
                                         n_interviews_per_spot, 
                                         '-n_spec_per_applicant', 
                                         n_spec_per_applicant, 
                                         '-specialty_choice_stddev_multiplier', 
                                         specialty_choice_stddev_multiplier, 
                                         '-n_runs', n_runs, 
                                         file, _fg=True)
