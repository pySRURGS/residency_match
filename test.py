import os 
import sys
try:
    import sh
except ImportError:
    # fallback: emulate the sh API with pbs
    import pbs

    class Sh(object):
        def __getattr__(self, attr):
            return pbs.Command(attr)
    sh = Sh()

sh.python3('run_simulations.py', 'test')
sh.python3('make_plots.py')
sh.python3('calculate_stats.py')
