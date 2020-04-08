# The `sh` module is not available on Windows, so use this bash script instead.
python3 run_simulations.py test
python3 make_plots.py
python3 calculate_stats.py
