#
# residency_match.py
# (C) Sohrab Towfighi 2020
# Licence: GPL v 3.0
# 
# Run the script using `python residency_match.py -h` to see the help docs

from matching.games import HospitalResident
import numpy as np
from copy import deepcopy
import os 
import sys
import pdb
import csv
import multiprocessing as mp
import parmap
import tqdm
import argparse

class Specialty(object):
    def __init__(self, specialty_id):
        self._id = specialty_id
        self._mean_spots = np.random.randint(2, 50)
        self._std_spots = np.ceil(self._mean_spots/5)

class Program(object):
    def __init__(self, program_id, specialty, n_interviews_per_spot):
        self._id = program_id
        self._specialty = specialty
        self._spots = int(np.random.normal(specialty._mean_spots, 
                                       specialty._std_spots))
        if self._spots <= 0:
            self._spots = 1
        self._list_of_applicants = []
        self._list_of_interviewees = []
        self._rank_of_applicants_list = []
        self._matched_applicants = []
        
class Applicant(object):
    def __init__(self, applicant_id, specialty_spots_distribution, 
                 n_specialties, n_spec_per_applicant, n_programs_per_specialty):
        self._id = applicant_id
        self._specialties_id = np.random.choice(list(range(0, n_specialties)), 
                                                  size=(n_spec_per_applicant), 
                                                  replace=False, 
                                                  p=specialty_spots_distribution)
        self._specialties_id = self._specialties_id.tolist()
        self._n_applications = n_programs_per_specialty * n_spec_per_applicant
        self._programs_to_which_applied = []
        self._programs_at_which_interviewed = []
        self._applicant_rank_list = []
        self._matched_program = []

def find_all_programs_for_specialty(list_of_programs, specialty_id):
    list_of_matching_program_ids = []
    for i in range(0,len(list_of_programs)):
        program = list_of_programs[i]
        if program._specialty._id == specialty_id:
            list_of_matching_program_ids.append(i)
    return list_of_matching_program_ids 

def sum_all_matched_applicants(result_dict):
    number = 0
    for key in result_dict.keys():
        number += len(result_dict[key])
    return number 

def find_all_unfilled_spots(result_dict, programs_list):
    number = 0
    for program in programs_list:
        number = number + program._spots
    matched_applicants = sum_all_matched_applicants(result_dict)
    unfilled_spots = number - matched_applicants
    return unfilled_spots

class Match(object):
    def __init__(self, n_interviews_per_spot, n_spec_per_applicant, 
                  denominator_variance_specialty_choice):        
        # GLOBAL VARIABLES
        self.n_specialties = 10
        self.n_spec_per_applicant = n_spec_per_applicant
        self.n_interviews_per_spot = n_interviews_per_spot
        self.n_programs_per_specialty = 10
        self.n_programs = self.n_specialties*self.n_programs_per_specialty
        self.denominator_variance_specialty_choice = denominator_variance_specialty_choice
    
    def generate(self):
        # create the specialties 
        list_of_specialties = []
        for i in range(0, self.n_specialties):
            list_of_specialties.append(Specialty(i))
            
        # create the programs 
        list_of_programs = []    
        for i in range(0, self.n_specialties):
            specialty = list_of_specialties[i]
            for j in range(0, self.n_programs_per_specialty):
                list_of_programs.append(Program(i*self.n_programs_per_specialty + j,
                                                specialty, self.n_interviews_per_spot))

        # create the probability distribution applicant specialty selection 
        list_specialty_spots_distribution = []
        for specialty in list_of_specialties:
            n_spots = 0
            for program in list_of_programs:
                if program._specialty == specialty:
                    n_spots += program._spots
            list_specialty_spots_distribution.append(n_spots)
        total_spots = int(np.sum(list_specialty_spots_distribution))
        list_specialty_spots_distribution = np.array(list_specialty_spots_distribution)
        list_specialty_spots_distribution = [x + np.abs(np.random.normal(0, x/self.denominator_variance_specialty_choice)) 
                                             for x in list_specialty_spots_distribution]
        list_specialty_spots_distribution = [np.max(x, 0) for x in list_specialty_spots_distribution]
        list_specialty_spots_distribution = list_specialty_spots_distribution / np.sum(list_specialty_spots_distribution)
        # create the applicants 
        list_of_applicants = []
        n_applicants = total_spots
        for i in range(0, n_applicants):
            list_of_applicants.append(Applicant(i, list_specialty_spots_distribution, 
                                                self.n_specialties, self.n_spec_per_applicant, 
                                                self.n_programs_per_specialty))

        # assign the programs to which the applicants applied
        for i in range(0, n_applicants):
            applicant = list_of_applicants[i]
            list_of_specialties_to_which_applicant_applied = applicant._specialties_id
            programs_applied = []
            for specialty in list_of_specialties_to_which_applicant_applied:
                programs_applied += find_all_programs_for_specialty(list_of_programs, specialty)
            applicant._programs_to_which_applied = programs_applied
            for program_index in programs_applied:
                program = list_of_programs[program_index]
                program._list_of_applicants.append(applicant._id)
        
        # assign the applicants who received interviews
        for i in range(0, self.n_programs):
            program = list_of_programs[i]
            applicants_to_program = program._list_of_applicants
            interview_spots = program._spots * self.n_interviews_per_spot
            if len(applicants_to_program) < interview_spots:
                interviewed_applicants = applicants_to_program
            else:
                interviewed_applicants = np.random.choice(applicants_to_program, 
                                                  size=(interview_spots), 
                                                  replace=False)
            program._list_of_interviewees = interviewed_applicants
            for applicant_index in interviewed_applicants:
                try:
                    applicant = list_of_applicants[applicant_index]
                    applicant._programs_at_which_interviewed.append(program._id)
                except TypeError:
                    pdb.set_trace()
        # create the applicants' rank lists
        for applicant in list_of_applicants:
            rank_list = deepcopy(applicant._programs_at_which_interviewed)
            np.random.shuffle(rank_list)
            applicant._applicant_rank_list = rank_list
        # create the programs' rank lists
        for program in list_of_programs:
            rank_list = deepcopy(program._list_of_interviewees)
            np.random.shuffle(rank_list)
            program._rank_of_applicants_list = rank_list
        applicant_prefs = {applicant._id: applicant._applicant_rank_list for applicant in list_of_applicants}
        applicants_without_interviews = []
        for key in applicant_prefs.keys():       
            applicant_pref = applicant_prefs[key]
            if len(applicant_pref) == 0:
                applicants_without_interviews.append(key)                
        for applicant in applicants_without_interviews:
            del applicant_prefs[applicant]
        applicant_prefs_keys = list(applicant_prefs.keys())
        for key in applicant_prefs_keys:
            applicant_prefs['applicant'+str(key)] = ['program'+str(x) for x in applicant_prefs[key]]
            del applicant_prefs[key]        
        program_prefs = {program._id: program._rank_of_applicants_list for program in list_of_programs}
        program_prefs_keys = list(program_prefs.keys())
        for key in program_prefs_keys:
            program_prefs['program'+str(key)] = ['applicant'+str(x) for x in program_prefs[key]]
            del program_prefs[key]
        capacities = {'program'+str(program._id): program._spots for program in list_of_programs}
        game = HospitalResident.create_from_dictionaries(applicant_prefs, program_prefs, capacities)
        result = game.solve()    
        num_applicants = len(list_of_applicants)
        number_matched = sum_all_matched_applicants(result)
        number_unmatched = len(list_of_applicants) - number_matched
        match_rate = number_matched/len(list_of_applicants)
        unfilled_spots = find_all_unfilled_spots(result, list_of_programs)
        n_applicants_no_interviews = len(applicants_without_interviews)
        return {'num_applicants': num_applicants,
                'fraction_applicants_no_interviews':n_applicants_no_interviews/num_applicants, 
                'match_rate':match_rate}

def append_to_csv(file_path, my_dict):
    with open(file_path, 'a', newline='') as file:
        w = csv.DictWriter(file, my_dict.keys())
        if file.tell() == 0:
            w.writeheader()
        w.writerow(my_dict)

def run(seed, n_interviews_per_spot, n_spec_per_applicant, 
                      denominator_variance_specialty_choice):
    np.random.seed(seed)
    match = Match(n_interviews_per_spot, n_spec_per_applicant, 
                      denominator_variance_specialty_choice)
    results_dict = match.generate()
    return results_dict

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='residency_match.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("n_interviews_per_spot", help="the number of interviews for each residency spot", type=int)
    parser.add_argument("n_spec_per_applicant", help="the number of specialties to which applicants apply", type=int)
    parser.add_argument("denominator_variance_specialty_choice", help="a value which determines variability in applicants' specialty choice. smaller values mean more variance.")
    parser.add_argument("n_runs", help="the number of repetitions in this set of simulations", type=int)
    parser.add_argument("output_file", help="the file to append the results of the run")           
    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)
    arguments = parser.parse_args()
    n_interviews_per_spot = int(arguments.n_interviews_per_spot)
    n_spec_per_applicant = int(arguments.n_spec_per_applicant)
    denominator_variance_specialty_choice = float(arguments.denominator_variance_specialty_choice)
    output_file = arguments.output_file
    N_runs = arguments.n_runs
    seeds_list = list(range(0, N_runs))
    list_of_results_dicts = parmap.map(run, seeds_list, n_interviews_per_spot=n_interviews_per_spot, 
                                       n_spec_per_applicant=n_spec_per_applicant,
                                       denominator_variance_specialty_choice=denominator_variance_specialty_choice,
                                       pm_pbar=True, pm_chunksize=3) 
    for results_dict in list_of_results_dicts:
        append_to_csv(output_file, results_dict)
    
