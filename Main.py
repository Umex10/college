import pandas as pd
from ISLP import load_data

#Load the data
college = load_data("College")

print("-- Column Names --")
# makes it more readable for py devs
print(college.columns.tolist())
print()


#1. Exercise
print("----- 1. Exercise -----")
print()
#1. Take each column and update the delimeter

def replace_dot_with_underscore(column_name):
    return column_name.replace('.', '_')

#2. Make it inplace directly on the data_frame
college.rename(columns=replace_dot_with_underscore, inplace=True)

print("-- Columns after renaming --")
print(college.columns.tolist())
print()


#2. Exercise
print("----- 2. Exercise -----")
print()

#1. Use Accept: how many students were accepted? 
#2. Use Apps: How many apps were there?
#3. Mathematical formula: * 100
#4. Show the tp 5

relative_number = (college['Accept'] / college['Apps']) * 100
college['Acceptance_Rate'] = relative_number

print(college[['Apps', 'Accept', 'Acceptance_Rate']].head())
print()

#3. Exercise
print("----- 3. Exercise -----")
print()

#1. sort the table with function college.sort_values
#2. FIrst sort after the first column, then after the second column
college_sorted = college.sort_values(by=['Private', 'Apps'], ascending=[True, True])

print("-- Sorted by 'Private' and 'Apps' --")
print(college_sorted[['Private', 'Apps']].head())
print()

#4. Exercise 

print("----- 4. Exercise -----")
print()

# Empty list for the values n and y
new_column = []

for x in college['Top10perc']:
    # Is elite Uni?
    if x > 50:
        new_column.append('Yes')
    else:
        new_column.append('No')

# Add the column to the exisitng dataframe
college['Elite'] = new_column

# Output
print("-- Added 'Elite' variable --")
print(college[['Top10perc', 'Elite']].head())
print()

# Final output
print("-- Final columns preview --")
print(college[['Private', 'Apps', 'Accept', 'Acceptance_Rate', 'Top10perc', 'Elite']].head())

# 5. Exercise
print()
print("----- 5. Exercise -----")
print()

summary = college.describe()
print(summary.T.round(2))

# 6. Exercise
print()
print("----- 6. Exercise -----")
print()
variables_of_interest = ['Acceptance_Rate', 'Room_Board', 'Books', 'PhD', 'Grad_Rate'] # investigating the mean of those variables
private_means = college.groupby('Private', observed=False)[variables_of_interest].mean() # Grouping by Private Collages (NO or YES)
print(private_means.T.round(2))

# 7. Exercise
print()
print("----- 7. Exercise -----")
print()

group_by_private_elite = college.groupby(['Private','Elite'], observed=False)[variables_of_interest].mean() # Grouping by Private and Elite Collages (NO or YES)
print(group_by_private_elite.T.round(2))
print()
