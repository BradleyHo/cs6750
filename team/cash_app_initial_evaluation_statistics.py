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

# This Python program performs the Kruskal-Wallis H test and the Mann-Whitney U test for the initial evaluation quantitative analyses
# The U test is not necessary. We wanted to perform it to ensure that the results are conclusive between the almost-evenly voted prototypes out of the three
# If you are using your own spreadsheet, print debug statements for a few columns or ensure the titles match exactly (case and spacing sensitive)

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Load the data from the spreadsheet
file_path = 'cash_app_init_eval.xlsx'  # Update this path if your XLSX is in a different directory
data = pd.read_excel(file_path)

# Define the column names for the intuitive/useful and satisfied ratings
questions_intuitive_useful = [
    'Prototype 1: Payer/Payee Selection Before Payment Amount \n\nHow intuitive and useful do you find the design for prototype #1?',
    'Prototype 2: Labeled Icons, Filter Options, Transaction History, Recurring Payments \n\nHow intuitive and useful do you find the design for prototype #2? ',
    'Prototype 3: Multiple Name Fields, User Payment Verification Measures  \n\nHow intuitive and useful do you find the design for prototype #3?'
]

questions_satisfied = [
    'Prototype 1: Payer/Payee Selection Before Payment Amount \n\nHow satisfied are you with prototype #1?',
    'Prototype 2: Labeled Icons, Filter Options, Transaction History, Recurring Payments \n\nHow satisfied are you with prototype #2?',
    'Prototype 3: Multiple Name Fields, User Payment Verification Measures \n\nHow satisfied are you with prototype #3?'
]

# Perform Kruskal-Wallis H test
print("Kruskal-Wallis H test for 'Intuitive and Useful':")
print(stats.kruskal(*(data[col].dropna() for col in questions_intuitive_useful)))

print("\nKruskal-Wallis H test for 'Satisfied':")
print(stats.kruskal(*(data[col].dropna() for col in questions_satisfied)))

# Mann-Whitney U test for the first two prototypes
print("\nMann-Whitney U test between prototypes 1 and 2 for 'Intuitive and Useful':")
print(stats.mannwhitneyu(data[questions_intuitive_useful[0]].dropna(), data[questions_intuitive_useful[1]].dropna()))

print("\nMann-Whitney U test between prototypes 1 and 2 for 'Satisfied':")
print(stats.mannwhitneyu(data[questions_satisfied[0]].dropna(), data[questions_satisfied[1]].dropna()))

# Collecting data for plots
intuitive_useful_data = [data[col].dropna() for col in questions_intuitive_useful]
satisfied_data = [data[col].dropna() for col in questions_satisfied]

# Plotting 'Intuitive and Useful' ratings
plt.figure(figsize=(10, 6))
plt.boxplot(intuitive_useful_data, labels=['Prototype 1', 'Prototype 2', 'Prototype 3'])
plt.title('Intuitive and Useful Ratings Across Prototypes')
plt.ylabel('Rating')
plt.xlabel('Prototypes')
plt.grid(axis='y')
plt.show()

# Plotting 'Satisfied' ratings
plt.figure(figsize=(10, 6))
plt.boxplot(satisfied_data, labels=['Prototype 1', 'Prototype 2', 'Prototype 3'])
plt.title('Satisfaction Ratings Across Prototypes')
plt.ylabel('Rating')
plt.xlabel('Prototypes')
plt.grid(axis='y')
plt.show()

'''
 _______________________________________________________________________________
|   Console output:                                                             |
|_______________________________________________________________________________|
|   Kruskal-Wallis H test for 'Intuitive and Useful':                           |
|   KruskalResult(statistic=3.47113821138211, pvalue=0.17629983848939748)       |
|                                                                               |
|   Kruskal-Wallis H test for 'Satisfied':                                      |
|   KruskalResult(statistic=4.985474537037027, pvalue=0.0826833300578063)       |
|                                                                               |
|   Mann-Whitney U test between prototypes 1 and 2 for 'Intuitive and Useful':  |
|   MannwhitneyuResult(statistic=52.0, pvalue=0.23294847145459052)              |
|                                                                               |
|   Mann-Whitney U test between prototypes 1 and 2 for 'Satisfied':             |
|   MannwhitneyuResult(statistic=64.0, pvalue=0.6476003153872727)               |
|_______________________________________________________________________________|
'''
