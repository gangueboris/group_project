with open("Day_5\Doc&images\example.txt",'r') as file:
    content = file.read()

content = content.split("\n")

seeds = [int(val) for val in content[0].split(':')[1].split()]
seed_soil = [[] for i in range(5-3)] # 19-3
soil_fertilizer = [[] for i in range(10-7)] #  54-21
fertilizer_water = [[] for i in range(16-12)] # 82-56
water_light = [[] for i in range(20-18)] # 122-84
light_temperature = [[] for i in range(25-22)] # 134-125
temperature_humidity = [[] for i in range(29-27)] # 173-136
humidity_location = [[] for i in range(33-31)] # 197-175

print(seeds)
for i, line in enumerate(content[3:5]): # 3:19
    seed_soil[i] = [int(val) for val in line.split()] 
for i, line in enumerate(content[7:10]): # 21:54
    soil_fertilizer[i] = [int(val) for val in line.split()] 
for i, line in enumerate(content[12:16]): # 56:82
    fertilizer_water[i] = [int(val) for val in line.split()]
for i, line in enumerate(content[18:20]): # 84:122
    water_light[i] = [int(val) for val in line.split()]
for i, line in enumerate(content[22:25]): # 125:134
    light_temperature[i] = [int(val) for val in line.split()]
for i, line in enumerate(content[27:29]): # 136:173
    temperature_humidity[i] = [int(val) for val in line.split()]
for i, line in enumerate(content[31:33]): # 175:197
    humidity_location[i] = [int(val) for val in line.split()]
#print(seed_soil,soil_fertilizer,fertilizer_water,water_light,light_temperature,temperature_humidity,humidity_location)
#print(soil_fertilizer)
locations = []
for seed in seeds:
    for line in seed_soil:
        if line[1] + line[2] > seed and seed >= line[1] :
            soil = line[0]
            soil+=  seed - line[1]
        else:
            soil = seed
               
    for line in soil_fertilizer:
        if soil - line[1] < line[2] and soil - line[1] > 0:
            fertilizer = line[0]
            fertilizer+=  soil - line[1]
        else:
            fertilizer = soil
    
    for line in fertilizer_water:
        if fertilizer - line[1] < line[2] and fertilizer - line[1] > 0:
            water = line[0]
            water+=  fertilizer - line[1]
        else:
            water = fertilizer
    
    for line in water_light:
        if water - line[1] < line[2] and water - line[1] > 0:
            light = line[0]
            light +=  water - line[1]
        else:
            light = water
    
    for line in light_temperature:
        if light - line[1] < line[2] and light - line[1] > 0:
            temperature = line[0]
            temperature +=  light - line[1]
        else:
            temperature = light
    
    for line in temperature_humidity:
        if temperature - line[1] < line[2] and temperature - line[1] > 0:
            humidity = line[0]
            humidity +=  temperature - line[1]
        else:
            humidity = temperature

    for line in humidity_location:
        if humidity - line[1] < line[2] and humidity - line[1] > 0:
            location = line[0]
            location+=  humidity - line[1]
        else:
            location = humidity
    print(seed,soil,fertilizer,water,light,temperature,humidity,location)
    locations.append(location)          
#print(locations,min(locations))

