![health](image/icon_public_domain_noun_project.svg)
# residency_match

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build Status](https://travis-ci.org/pySRURGS/residency_match.svg?branch=master)](https://travis-ci.org/pySRURGS/residency_match)

This software simulates the medical residency match. It does so by spawning 10 randomly generated specialties, and for each specialty it generates 10 programs. Each specialty has a typical number of spots per program, which is randomly assigned a value between 1 and 50. The number of applicants is forced to equal the number of program spots. 

## Getting Started

The main script is `residency_match.py`. Download the repository and run the computations using python3.6 via a terminal.

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
                          [-specialty_choice_stddev_multiplier SPECIALTY_CHOICE_STDDEV_MULTIPLIER]
                          [-n_runs N_RUNS]
                          output_file

positional arguments:
  output_file           the file to append the results of the run

optional arguments:
  -h, --help            show this help message and exit
  -n_interviews_per_spot N_INTERVIEWS_PER_SPOT
                        The number of interviews for each residency spot.
                        (default: 10)
  -n_spec_per_applicant N_SPEC_PER_APPLICANT
                        The number of specialties to which applicants apply.
                        (default: 2)
  -specialty_choice_stddev_multiplier SPECIALTY_CHOICE_STDDEV_MULTIPLIER
                        A number value which determines variability in
                        applicants' specialty choice. Larger values mean more
                        variability. (default: 5)
  -n_runs N_RUNS        The number of repetitions in this set of simulations.
                        (default: 10)
```

## Community

If you would like to contribute to the project or you need help, then please create an issue.

With regards to community suggested changes, I would comment as to whether it would be within the scope of the project to include the suggested changes. If both parties are in agreement, whomever is interested in developing the changes can make a pull request, or I will implement the suggested changes.

## Author

**Sohrab Towfighi**

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENSE) file for details

## Acknowledgements

The icon is in the public domain and is from the Noun Project: [Link](https://commons.wikimedia.org/wiki/File:Public_health_icon_-_Noun_Project_6435.svg)
