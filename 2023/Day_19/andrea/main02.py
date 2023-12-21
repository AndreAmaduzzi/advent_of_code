"""
19th December, 2023
"""

import re


def is_accepted(part, workflows):
    x, m, a, s  = part
    part_dict = {
        'x': x,
        'm': m,
        'a': a,
        's': s
    }
                
    current_wf_name = 'in'
    while current_wf_name not in ['A', 'R']:
        current_wf = workflows[current_wf_name]
        for rule in current_wf:
            condition, success_condition_wf = rule
            if eval(condition, part_dict) == True:
                current_wf_name = success_condition_wf
                break
    
    return current_wf_name == 'A'


def main():

    with open('input.txt', 'r') as f:
        file = f.read()
   
    wf_file, parts_file = file.split('\n\n')   

    # Parts parsing    
    parts = set()
    regex = re.compile('{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')
    for line in parts_file.split('\n'):
        match = re.fullmatch(regex, line)
        parts.add(tuple(map(int, match.groups())))

    # Workflow parsing 
    workflows = dict()
    rule_regex = re.compile('([a-zA-Z]+[<>]\d+):([a-zA-Z]+)')
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
            rules.append((match[0], match[1]))
            # print(match[0], match[1], match[2], match[3])
        rules.append(('True', default))
        workflows[name] = rules

    # P: (parts) set of parts; each part is a 4-size tuple representing 'x','m','a','s' values
    # WF: (workflows) dict of workflows; key=[workflow's name] value=[list of workfllow rules];
    #     each rule is a 2-size tuple (condition, success_condition_workflow); the last rule
    #     has 'True' as condition

    total_sum = 0
    for part in parts:
        if is_accepted(part, workflows):
            total_sum += sum(part)
    # Part 1
    print('Soluzione:')
    print(total_sum)



if __name__ == "__main__":
    main()
