# residency_match

[![Build Status](https://travis-ci.org/pySRURGS/nlp_ml.svg?branch=master)](https://travis-ci.org/pySRURGS/nlp_ml)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

This software simulates the medical residency match. 
In these simulations, there are 10 specialties, and for each specialty there are 10 programs.
Each specialty has a typical program size, and this is used to generate programs randomly.
A corresponding number of applicants are generated so that the ratio of applicants to programs is 1 to 1. 

We vary the parameters of the match and examine how this affects the match rate and the number of applicants who get no interviews. 
