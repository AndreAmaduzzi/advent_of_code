import re

def main():
    print('hello world')
    
    with open('input.txt') as f:
        lines = f.readlines()
    
    maps =  {}
    # maps: "seed-to-soil": [[50 98 2], [52 50 48]]
    for line in lines:
        if "seeds" in line:
            splits = line.split(' ')
            seeds = splits[1:]
            seeds[-1] = seeds[-1][:-1]
        if "map" in line:
            map_id = line.split(' ')[0] # seed-to-soil
            map_id_list = []
        #if line.matches("[0-9]+"):
        if "\n" in line:
            if line.replace(" ", "")[:-1].isdigit():
                numbers = line.split(' ')
                current_nums = []
                for number in numbers:
                    current_nums.append(int(number))
                map_id_list.append(current_nums)
                maps[map_id] = map_id_list
        else:
            if line.replace(" ", "").isdigit():
                numbers = line.split(' ')
                current_nums = []
                for number in numbers:
                    current_nums.append(int(number))
                map_id_list.append(current_nums)
                maps[map_id] = map_id_list
    
    locations = []
    for seed in seeds:
        current_source = int(seed)
        for key, vals in maps.items():
            # look for seed inside range
            for list_num in vals:
                if current_source>=list_num[1] and current_source<=list_num[1]+list_num[2]-1:
                    # found seed, looking for mapping
                    #offset = list_num[1] - list_num[0]
                    current_source = list_num[0]+current_source-list_num[1]
                    break
        locations.append(current_source)
    
    print('locations:', locations)
    print('min:', min(locations))
        
                        
    
    
if __name__ == "__main__":
    main()