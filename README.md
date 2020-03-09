# residency_match

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build Status](https://travis-ci.org/pySRURGS/residency_match.svg?branch=master)](https://travis-ci.org/pySRURGS/residency_match)

This software simulates the medical residency match. It does so by spawning 10 randomly generated specialties, and for each specialty it generates 10 programs. Each specialty has a typical number of spots per program, which is randomly assigned a value between 1 and 50. The number of applicants is forced to equal the number of program spots. 

## Getting Started

The main script is `simulation.py`. Download the repository and run it using python3.6 via a terminal.

### Prerequisites

You can install the prerequisite packages with pip

### Installing

Clone the repo then install the prerequisites.

```
git clone https://github.com/pySRURGS/residency_match.git
cd residency_match
pip install -r requirements.txt --user
```

### Running the Simulations

You can run a quick run of the entire process by running `python3 test.py`, which executes the entire process with only 10 repetitions per set. The figure is generated in `figure.png` and the statistics spreadsheet is generated in `stats.csv`

## Author

**Sohrab Towfighi**

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENSE) file for details
