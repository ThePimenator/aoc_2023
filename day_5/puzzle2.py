
input = open('input.txt', 'r')
inputLines = input.readlines()

sum = 0 

seeds = [int(s) for s in inputLines[0].rstrip().split(" ")[1:]]
seeds_2 = []

i = 0
while i < len(seeds):
    seeds_2.append([seeds[i], seeds[i] + seeds[i+1]])
    i += 2
seeds = seeds_2

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

# return to be added back in the pool, progressed 
def computeRange(seed_range, progression):
    diff = progression[2] - progression[0]
    # Completely not in the progression range, nothing changes
    if seed_range[0] > progression[1]:
        return [seed_range], None

    # left point of range in progression range
    if seed_range[0] <= progression[1] and seed_range[0] >= progression[0]:
        # right point also in range EASY
        if seed_range[1] < progression[1]:
            return None, [seed_range[0] + diff, seed_range[1] + diff]
        # right point not in range SPLIT 
        else:
            return [[progression[1], seed_range[1]]], [seed_range[0] + diff, progression[1] + diff]
    # Left point to the left of the range 
    else: 
        # right point also to the left, nothing changed
        if seed_range[1] <= progression[0]:
            return [seed_range], None
        # right point of range in progression range, but not left SPLIT once 
        if seed_range[1] <= progression[1] and seed_range[1] > progression[1]:
            return [[seed_range[0], progression[0]]], [progression[0] + diff, seed_range[1] + diff]
        # right point to the right of progression range, SLIT TWICE (middle section progresses)
        else: 
            return [[seed_range[0], progression[0]],[progression[1], seed_range[1]]], [progression[0] + diff,  progression[1] + diff]

category = ""
for line in inputLines[1:]:
    if line.strip() == "":
        continue
    if not line.strip()[0].isdigit():
        category = line.strip()
    else: 
        destination_start = int(line.strip().split(" ")[0])
        source_start = int(line.strip().split(" ")[1])
        range_map = int(line.strip().split(" ")[2])

        match category:
            case "seed-to-soil map:":
                seed_to_soil.append([source_start, source_start + range_map, destination_start]);
            case "soil-to-fertilizer map:":
                soil_to_fertilizer.append([source_start, source_start + range_map, destination_start]);
            case "fertilizer-to-water map:":
                fertilizer_to_water.append([source_start, source_start + range_map, destination_start]);
            case "water-to-light map:":
                water_to_light.append([source_start, source_start + range_map, destination_start]);
            case "light-to-temperature map:":
                light_to_temperature.append([source_start, source_start + range_map, destination_start]);
            case "temperature-to-humidity map:":
                temperature_to_humidity.append([source_start, source_start + range_map, destination_start]);
            case "humidity-to-location map:":
                humidity_to_location.append([source_start, source_start + range_map, destination_start]);

steps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water,
         water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

# return to be added back in the pool, progressed 
for s in steps:
    next_seeds = []
    for i in range(len(seeds)):
        todo = [seeds[i]]
        todo_2 = []
        for j in s:
            for r in todo:
                todo_new, done = computeRange(r, j)
                if not todo_new is None:
                    for new in todo_new:
                        todo_2.append(new)
                if not done is None: 
                    next_seeds.append(done)
            todo = todo_2
            todo_2 = []
        for r in todo:
            next_seeds.append(r)
    seeds = next_seeds

for s in seeds:
    if s[0] < 100000000:
        print(s[0])

        



