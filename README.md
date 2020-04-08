# residency_match

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build Status](https://travis-ci.org/pySRURGS/residency_match.svg?branch=master)](https://travis-ci.org/pySRURGS/residency_match)

This software simulates the medical residency match. It does so by spawning 10 randomly generated specialties, and for each specialty it generates 10 programs. Each specialty has a typical number of spots per program, which is randomly assigned a value between 1 and 50. The number of applicants is forced to equal the number of program spots. 

## Getting Started

The main script is `residency_match.py`. Download the repository and run the computations using python3.6 via a terminal.

### Prerequisites

You can install the prerequisite packages with pip

### Installing

Clone the repo then install the prerequisites. The software is designed to work for Ubuntu Linux 18.04, but should work on Mac OSX and also Windows if you are using git bash. 

```
git clone https://github.com/pySRURGS/residency_match.git
cd residency_match
pip install -r requirements.txt --user
```

### Running the Simulations

You can run a quick run of the entire process by running `python3 test.py`, which executes the entire process with only 10 repetitions per set. Windows users can run `test.sh` instead of `test.py`, since the `sh` module is only available on Linux. The figure is generated in `figure.png` and the statistics spreadsheet is generated in `stats.csv`.

### Running a Single Simulation

You can use `residency_match.py` to run a single simulation. 

The manual for its command line interface's usage can be generated using `python residency_match.py -h`, which should printout the following:

```
usage: residency_match.py [-h] [-n_interviews_per_spot N_INTERVIEWS_PER_SPOT]
                          [-n_spec_per_applicant N_SPEC_PER_APPLICANT]
                          [-denominator_variance_specialty_choice DENOMINATOR_VARIANCE_SPECIALTY_CHOICE]
                          [-n_runs N_RUNS]
                          output_file

positional arguments:
  output_file           the file to append the results of the run

optional arguments:
  -h, --help            show this help message and exit
  -n_interviews_per_spot N_INTERVIEWS_PER_SPOT
                        the number of interviews for each residency spot
                        (default: 10)
  -n_spec_per_applicant N_SPEC_PER_APPLICANT
                        the number of specialties to which applicants apply
                        (default: 2)
  -denominator_variance_specialty_choice DENOMINATOR_VARIANCE_SPECIALTY_CHOICE
                        a value which determines variability in applicants'
                        specialty choice. smaller values mean more variance.
                        (default: 0.2)
  -n_runs N_RUNS        the number of repetitions in this set of simulations
```

## Author

**Sohrab Towfighi**

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENSE) file for details

## Community

If you would like to contribute to the project or you need help, then please create an issue.

With regards to community suggested changes, I would comment as to whether it would be within the scope of the project to include the suggested changes. If both parties are in agreement, whomever is interested in developing the changes can make a pull request, or I will implement the suggested changes.
