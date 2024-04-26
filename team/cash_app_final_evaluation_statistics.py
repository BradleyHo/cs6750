'''
    ____                       _                              __           __        __      
   / __ \___  ___  ____       (_)___ _____  ___  _____       / /___ ______/ /_____  / /______
  / / / / _ \/ _ \/_  /______/ / __ `/ __ \/ _ \/ ___/  __  / / __ `/ ___/ //_/ _ \/ __/ ___/
 / /_/ /  __/  __/ / //_____/ / /_/ / / / /  __/ /     / /_/ / /_/ / /__/ ,< /  __/ /_(__  ) 
/_____/\___/\___/ /___/    /_/\__, /_/ /_/\___/_/      \____/\__,_/\___/_/|_|\___/\__/____/  
                             /____/                                                          
 ___________________________________________________
|   Georgia Institute of Technology                 |
|   CS 6750: Human-Computer Interaction             |
|___________________________________________________|
|   Team: Deez-igner Jackets                        |
|   Repository: https://github.com/BradleyHo/cs6750 | 
|___________________________________________________|
|   Sharon Cha                                      |
|   Bradley Ho                                      |
|   Ugonna Nwankwo                                  |
|   Minh Thu (Theresa) Phan                         |
|   Lili Yu                                         |
|___________________________________________________|                                                 
'''

from scipy.stats import chisquare
import pandas as pd

# How would you rate the intuitiveness of this design?
observed_frequencies = [0,3,4,19,1]
total_responses = sum(observed_frequencies)
expected_frequencies = [total_responses/5]*5

chi2, p_val = chisquare(observed_frequencies, f_exp=expected_frequencies)
print(f'Chi-Square statistic = {chi2}\np-value = {p_val}')
if p_val < 0.05:
   print("We reject the null hypothesis that the observed and expected frequencies are the same.")
else:
   print("We do not reject the null hypothesis that the observed and expected frequencies are the same.")

# How would you rate the efficiency of this design?
observed_frequencies = [0,4,6,14,3]
total_responses = sum(observed_frequencies)
expected_frequencies = [total_responses/5]*5

chi2, p_val = chisquare(observed_frequencies, f_exp=expected_frequencies)
print(f'Chi-Square statistic = {chi2}\np-value = {p_val}')
if p_val < 0.05:
   print("We reject the null hypothesis that the observed and expected frequencies are the same.")
else:
   print("We do not reject the null hypothesis that the observed and expected frequencies are the same.")

# How would you rate the usability of this design?
observed_frequencies = [0,0,4,18,5]
total_responses = sum(observed_frequencies)
expected_frequencies = [total_responses/5]*5

chi2, p_val = chisquare(observed_frequencies, f_exp=expected_frequencies)
print(f'Chi-Square statistic = {chi2}\np-value = {p_val}')
if p_val < 0.05:
   print("We reject the null hypothesis that the observed and expected frequencies are the same.")
else:
   print("We do not reject the null hypothesis that the observed and expected frequencies are the same.")

# How well do you agree?
observed_frequencies = [0,0,2,20,5]
total_responses = sum(observed_frequencies)
expected_frequencies = [total_responses/5]*5

chi2, p_val = chisquare(observed_frequencies, f_exp=expected_frequencies)
print(f'Chi-Square statistic = {chi2}\np-value = {p_val}')
if p_val < 0.05:
   print("We reject the null hypothesis that the observed and expected frequencies are the same.")
else:
   print("We do not reject the null hypothesis that the observed and expected frequencies are the same.")
