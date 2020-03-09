import os 
import sys
import sh

sh.python3('run_simulations.py', 'test')
sh.python3('make_plots.py')
sh.python3('calculate_stats.py')
