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

def start(mapWidth=500, mapHeight=500, mapName="", outputPath="./results/cirplot1.png"):
    print("CreateMap.py")
    makeCPlot(dataPath, outputPath)

def makeCPlot(dataPath, outputPath):
    print("makeCPlot()")

    import pandas as pd

    xls = pd.ExcelFile(dataPath)
    df = xls.parse(0)

    print(df.shape)
    print(df.head())
    print(df.iloc[0][0])
    print(df.iloc[0][1])
    print(df.iloc[1][0])

start()