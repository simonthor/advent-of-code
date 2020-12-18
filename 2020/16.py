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
fulfill_rules_valid = fulfill_rules[:, valid_tickets_bool.flatten()]

ordered_rules = rules['rule name'].copy()
while fulfill_rules_valid.size > 0:
    fulfill_rules_valid = fulfill_rules_valid.reshape((rules.shape[0], *valid_tickets.shape))
    # TODO: Code not working. Other indices must be removed and sum might have to be over axis=0 instead
    only_one_rule_match = fulfill_rules_valid.all(axis=1).sum(axis=1) == 1
    ordered_rules[only_one_rule_match] = rules.loc[only_one_rule_match, 'rule name']
    fulfill_rules_valid = np.delete(fulfill_rules_valid, only_one_rule_match, 0)
    fulfill_rules_valid = np.delete(fulfill_rules_valid, only_one_rule_match, 2)

print(ordered_rules)
