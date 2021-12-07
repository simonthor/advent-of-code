with open('19.txt') as rules_and_messages:
    rules = {}
    for line in rules_and_messages:
        if line == '\n':
            break
        line_sections = line.split(':')
        rules[int(line_sections[0])] = line_sections[1].strip()

    collapse_rules(0)

    for line in rules_and_messages:

