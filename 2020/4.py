# Day 4
#%% part 1

with open('4.txt') as passport_file:
    passports = passport_file.read()
pass_port_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passports = 0
for p_info in passports.split('\n\n'):
    valid_passports += all(key in p_info for key in pass_port_keys)
print(valid_passports)

#%% part 2


def create_dict(passport_info):
    for info in passport_info.split():
        yield info.split(':')


with open('4.txt') as passport_file:
    passports = passport_file.read()
passport_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
valid_passports = 0
for p_info in passports.split('\n\n'):
    p_info_dict = {key: value for key, value in create_dict(p_info)}
    # Guard clauses for input validation
    try:
        if not (set(p_info_dict.keys()) | {'cid'}) == set(passport_keys):
            continue
        elif not 1920 <= int(p_info_dict['byr']) <= 2002:
            continue
        elif not 2010 <= int(p_info_dict['iyr']) <= 2020:
            continue
        elif not 2020 <= int(p_info_dict['eyr']) <= 2030:
            continue
        elif not ((('cm' in p_info_dict['hgt']) and (150 <= int(p_info_dict['hgt'][:-2]) <= 193))
                  or ('in' in p_info_dict['hgt'] and (59 <= int(p_info_dict['hgt'][:-2]) <= 76))):
            continue
        elif re.fullmatch('#(?:[0-9a-f]{6})', p_info_dict['hcl']) is None:
            continue
        elif p_info_dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        elif not (p_info_dict['pid'].isnumeric() and len(p_info_dict['pid']) == 9):
            continue
    except Exception as e:
        print(p_info_dict, e)
    valid_passports += 1

print(valid_passports)
