# import 
# modules.cuz
# from modules.cuz import ReadJson
import json
# read = ReadJson("story/stats.json").show()
# print(read)

Jpath = "story/stats.json"

with open(Jpath,'r') as jFile:
    # json.load(jsonpath)
    print(json.load(jFile))
    pass
    
# import os

# print(os.path.curdir)