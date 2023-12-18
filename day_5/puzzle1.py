
input = open('input.txt', 'r')
inputLines = input.readlines()

sum = 0 

seeds = [int(s) for s in inputLines[0].rstrip().split(" ")[1:]]

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

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

for s in steps:
    for i in range(len(seeds)):
        for j in s:
                seeds[i] = j[2] + seeds[i] - j[0]
                break

print(min(seeds))
        



