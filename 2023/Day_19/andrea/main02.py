"""
19th December, 2023
"""

import re


def calculate_ranges_product(ranges):
    product = 1
    for start, end in ranges.values():
        product *= end - start + 1
    return product



def get_accepted_comb_number(ranges, wf_name, workflows):
    # BASE CASE (1)
    if wf_name == 'R':
        return 0
    # BASE CASE (2)
    if wf_name == 'A': 
        return calculate_ranges_product(ranges)

    rules, default = workflows[wf_name] # rules: list of rules; default: default workflow name

    total = 0
    is_condition_impossible = False
    for var, symb, num, target in rules:
        start, end = ranges[var]
        # Calculate the range for the true and false condition
        if symb == "<":
            rule_true_range = (start, num-1)
            rule_false_range = (num, end)
        else: # symb == GREATER:
            rule_true_range = (num + 1, end)
            rule_false_range = (start, num)
        
        if rule_true_range[0] <= rule_true_range[1]:
            ranges_copy = dict(ranges)
            ranges_copy[var] = rule_true_range
            total += get_accepted_comb_number(ranges_copy, target, workflows)

        if rule_false_range[0] <= rule_false_range[1]:
            ranges = dict(ranges)
            ranges[var] = rule_false_range
        else:
            # Impossible Condition 
            is_condition_impossible = True
            break

    if not is_condition_impossible:
        total += get_accepted_comb_number(ranges, default, workflows)
    
    return total


def main():

    with open('input.txt', 'r') as f:
        file = f.read()
   
    wf_file, _ = file.split('\n\n')   

    # Workflow parsing 
    workflows = dict()
    rule_regex = re.compile('([a-zA-Z]+)([<>])(\d+):([a-zA-Z]+)')
    for line in wf_file.split('\n'):
        # Name
        index_of_curly= line.index('{')
        name = line[:index_of_curly]
        # Default rule
        rest_line = line[index_of_curly + 1:len(line)-1]
        default = rest_line.split(',')[-1]
        # Rules
        rules = []
        matches = re.findall(rule_regex, rest_line)
        for match in matches:
            rules.append((match[0], match[1], int(match[2]), match[3]))

        workflows[name] = (rules, default)


    rages_dict_0 = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }

    sol = get_accepted_comb_number(rages_dict_0, 'in', workflows)

    print('Soluzione:')
    print(sol)



if __name__ == "__main__":
    main()
