"""
5th December, 2023
"""


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    state_read = 0

    for line in lines:
        aux_list = []
        if state_read == 0:
            if line != 'seed-to-soil map:\n':
                for word in line.split():
                    if word.isdecimal():
                      seeds.append(int(word))
            else:
                state_read = 1
        elif state_read == 1:
            if line != 'soil-to-fertilizer map:\n':
                for word in line.split():
                    aux_list.append(int(word))
                seed_to_soil.append(aux_list)
            else:
                state_read = 2
        elif state_read == 2:
            if line != 'fertilizer-to-water map:\n':
                for word in line.split():
                    aux_list.append(int(word))
                soil_to_fertilizer.append(aux_list)
            else:
                state_read = 3
        elif state_read == 3:
            if line != 'water-to-light map:\n':
                for word in line.split():
                    aux_list.append(int(word))
                fertilizer_to_water.append(aux_list)
            else:
                state_read = 4
        elif state_read == 4:
            if line != 'light-to-temperature map:\n':
                for word in line.split():
                    aux_list.append(int(word))
                water_to_light.append(aux_list)
            else:
                state_read = 5
        elif state_read == 5:
            if line != 'temperature-to-humidity map:\n':
                for word in line.split():
                    aux_list.append(int(word))
                light_to_temperature.append(aux_list)
            else:
                state_read = 6
        elif state_read == 6:
            if line != 'humidity-to-location map:\n':
                for word in line.split():
                    aux_list.append(int(word))
                temperature_to_humidity.append(aux_list)
            else:
                state_read = 7
        elif state_read == 7:
            for word in line.split():
                aux_list.append(int(word))
            humidity_to_location.append(aux_list)

    seed_to_soil.pop()
    soil_to_fertilizer.pop()
    fertilizer_to_water.pop()
    water_to_light.pop()
    light_to_temperature.pop()
    temperature_to_humidity.pop()

    # print(seeds)
    # print(seed_to_soil)
    # print(soil_to_fertilizer)
    # print(fertilizer_to_water)
    # print(water_to_light)
    # print(light_to_temperature)
    # print(temperature_to_humidity)
    # print(humidity_to_location)

    for i in range(len(seeds)):
        ''' seed to soil'''
        for x in seed_to_soil:
            if seeds[i] >= x[1] and seeds[i] < x[1] + x[2]:
                seeds[i] = seeds[i] - x[1] + x[0]
                break
        # print(seeds[i])
        ''' soil to fertilizer '''
        for x in soil_to_fertilizer:
            if seeds[i] >= x[1] and seeds[i] < x[1] + x[2]:
                seeds[i] = seeds[i] - x[1] + x[0]
                break
        # print(seeds[i])
        ''' fertilizer to water'''
        for x in fertilizer_to_water:
            if seeds[i] >= x[1] and seeds[i] < x[1] + x[2]:
                seeds[i] = seeds[i] - x[1] + x[0]
                break
        # print(seeds[i])
        ''' water to light '''
        for x in water_to_light:
            if seeds[i] >= x[1] and seeds[i] < x[1] + x[2]:
                seeds[i] = seeds[i] - x[1] + x[0]
                break
        # print(seeds[i])
        ''' light to temperature '''
        for x in light_to_temperature:
            if seeds[i] >= x[1] and seeds[i] < x[1] + x[2]:
                seeds[i] = seeds[i] - x[1] + x[0]
                break
        # print(seeds[i])
        ''' temperature to humidity '''
        for x in temperature_to_humidity:
            if seeds[i] >= x[1] and seeds[i] < x[1] + x[2]:
                seeds[i] = seeds[i] - x[1] + x[0]
                break
        # print(seeds[i])
        ''' humidity to location '''
        for x in humidity_to_location:
            if seeds[i] >= x[1] and seeds[i] < x[1] + x[2]:
                seeds[i] = seeds[i] - x[1] + x[0]
                break 

    min_location = seeds[0]
    for i in seeds:
        if i < min_location:
            min_location = i

    # print() 
    # print(seeds)
    print('Soluzione:')
    print(min_location)


if __name__ == "__main__":
    main()