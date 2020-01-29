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

files = ["10_2_0point2.csv", "2_2_0point2.csv", "20_2_0point2.csv", "10_2_10.csv","10_4_0point2.csv"]
if __name__ == '__main__':
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
        sh.python3('simulation.py', arg0, arg1, arg2, file, _fg=True)