import pandas as pd
import numpy as np

# %% part 1
rules = pd.read_csv('16.txt', nrows=20, sep=': |-| or ', engine='python',
                    names=['rule name', 'rule1 low', 'rule1 high', 'rule2 low', 'rule2 high'])
nearby_tickets = np.loadtxt('16.txt', delimiter=',', skiprows=25, dtype=int)
nearby_tickets_flat = nearby_tickets.flatten()
fulfill_rules = (((rules['rule1 low'].to_numpy()[:, np.newaxis] <= nearby_tickets_flat)
                  & (nearby_tickets_flat <= rules['rule1 high'].to_numpy()[:, np.newaxis]))
                 | ((rules['rule2 low'].to_numpy()[:, np.newaxis] <= nearby_tickets_flat)
                    & (nearby_tickets_flat <= rules['rule2 high'].to_numpy()[:, np.newaxis])))

valid_ticket_values = fulfill_rules.any(axis=0).reshape(nearby_tickets.shape)
nearby_tickets[~valid_ticket_values].sum()

#%% part 2
valid_tickets = nearby_tickets[valid_ticket_values.all(axis=1), :]
valid_tickets_bool = valid_ticket_values.copy()
valid_tickets_bool[~valid_ticket_values.all(axis=1), :] = False
fulfill_rules_valid = fulfill_rules[:, valid_tickets_bool.flatten()].reshape((-1, *valid_tickets.shape))
ordered_rules = pd.Series(index=rules['rule name'].index, data='', dtype=str)
while (ordered_rules == '').any():
    rules_valid_for_all_tickets = fulfill_rules_valid.all(axis=1)
    ticket_col_with_one_rule_match = rules_valid_for_all_tickets.sum(axis=0) == 1
    corresponding_rules = rules_valid_for_all_tickets[:, ticket_col_with_one_rule_match].flatten()
    ordered_rules[ticket_col_with_one_rule_match] = rules['rule name'][corresponding_rules].tolist()
    fulfill_rules_valid[corresponding_rules, :, :] = False
    fulfill_rules_valid[:, :, ticket_col_with_one_rule_match] = False


your_ticket = np.loadtxt('16.txt', skiprows=22, max_rows=1, delimiter=',', dtype=np.int64)
print(your_ticket[ordered_rules.str.startswith('departure').to_numpy()].prod())
