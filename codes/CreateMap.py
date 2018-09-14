###
#   File name : CreateMap.py
#   Author    : Hyunjin Kim
#   Date      : Sep 14, 2018
#   Email     : firadazer@gmail.com
#   Purpose   : Make a random map with specified parameters
#
#   Instruction
#               1. import CreateMap
#               2. Run the function "MakeCircosPlot1.start(dataPath="./data/data1.xlsx", outputPath="./results/cirplot1.png"))" - specify the inputs
#               3. The results will be generated in the outputPath
###

def start(map_width=10, map_height=10, map_name="Map", output_path="./results/"):
    print("CreateMap.py")
    make_random_map(map_width, map_height, map_name, output_path)


### a function to make a random map
def make_random_map(map_width, map_height, map_name, output_path):
    print("makeRandomMap()")
    import random
    random.seed(1234)

    ### make an empty map
    world_map = [0] * map_height
    for i in range(map_height):
        world_map[i] = [0] * map_width

    ### randomly make horizontal and vertical roads on the map
    for i in range(map_width):
        ### add horizontal roads
        indices = random.sample(range(map_height), random.randint(0, map_height))
        for j in range(len(indices)):
            world_map[indices[j]][i] = world_map[indices[j]][i] + 1

        ### add vertical roads
        indices = random.sample(range(map_height), random.randint(0, map_height))
        for j in range(len(indices)):
            world_map[indices[j]][i] = world_map[indices[j]][i] + 2

        print_map_console(world_map)


### a function to print a given map in a readable format
### 0 - nothing
### 1 - horizontal road
### 2 - vertical road
### 3 - cross road
def print_map_console(world_map):
    print("printMapConsole()")

    ### convert the given map
    converted_map = world_map
    for i in range(len(converted_map)):
        for j in range(len(converted_map[0])):
            if converted_map[i][j] == 0:
                converted_map[i][j] = " "
            elif converted_map[i][j] == 1:
                converted_map[i][j] = "-"
            elif converted_map[i][j] == 2:
                converted_map[i][j] = "|"
            elif converted_map[i][j] == 3:
                converted_map[i][j] == "+"
            else:
                print("Unknown number in the map")
                SystemExit(0)

    ### print the given map
    for i in range(len(converted_map)):
        print(*converted_map[i], sep="")


start()
