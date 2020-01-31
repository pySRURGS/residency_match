import os 
import csv 
import pandas 
import numpy as np 
import scipy.stats as sc
from run_simulations import files
import pdb

def main():
    table = []
    for myfile in files:
        df_baseline = pandas.read_csv('10_2_0point2.csv')
        df = pandas.read_csv(myfile)
        columns = ['num_applicants', 'fraction_applicants_no_interviews', 'match_rate']
        for column in columns:
            p_value = sc.ttest_ind(df[column], df_baseline[column], equal_var=False).pvalue
            results = [myfile, column, df[column].mean(), df[column].median(), df[column].min(), 
                       df[column].max(), p_value]
            table.append(results)
            
    with open('stats.csv', 'w') as outputfile:
        writer = csv.writer(outputfile)
        for i in range(0,len(table)):
            writer.writerow(table[i])
            
if __name__ == '__main__':
    main()