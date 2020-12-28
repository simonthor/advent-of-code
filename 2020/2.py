# Day 2
import pandas as pd

#%% part 1

passwords = pd.read_csv('2.txt', sep=' |-|: ',
                        names=['min_counts', 'max_counts', 'character', 'password'],
                        engine='python')

#%%

valid_passwords = 0
for entry in passwords.itertuples():
    if entry.min_counts <= entry.password.count(entry.character) <= entry.max_counts:
        valid_passwords += 1
print(valid_passwords)

#%% part 2

passwords.rename(columns={'min_counts': 'first_index', 'max_counts': 'last_index'}, inplace=True)
valid_passwords = 0
for entry in passwords.itertuples():
    if (entry.password[entry.first_index-1] == entry.character) ^ (entry.password[entry.last_index-1] == entry.character):
        valid_passwords += 1
print(valid_passwords)
