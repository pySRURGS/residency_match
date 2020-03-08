# residency_match

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

This software simulates the medical residency match. 
In these simulations, there are 10 specialties, and for each specialty there are 10 programs.
Each specialty has a typical program size, and this is used to generate programs randomly.
A corresponding number of applicants are generated so that the ratio of applicants to programs is 1 to 1. 

We vary the parameters of the match and examine how this affects the match rate and the number of applicants who get no interviews. 

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

### Command line help

```
python3 simulation.py -h
```
