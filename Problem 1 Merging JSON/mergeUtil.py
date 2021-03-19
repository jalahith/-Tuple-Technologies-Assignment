import os
import json
import sys
from os import listdir
from os.path import isfile, join

if len(sys.argv) < 5:
    print("########### JSON Merge Utility #####################")
    print("## Utility requires 4 arguments -> (Folder Path, Input File Base Name, Output File Base Name, Max File Size) ")
    print("#####################################################")
    exit(0)
print("########### JSON Merge Utility #####################")
print("## Folder Path           -> ", sys.argv[1])
print("## Input File Base Name  -> ", sys.argv[2])
print("## Output File Base Name -> ", sys.argv[3])
print("## Max File Size         -> ", sys.argv[4])
print("#####################################################")

outputFileDict = {}
#mypath = 'C:\\Users\jalahith\Desktop\Assignment Tuple\data'
folderPath = sys.argv[1]
inputFileBaseName = sys.argv[2]
outputFileBaseName = sys.argv[3]
maxFileSize = sys.argv[4]

listOfJSONFiles = [f for f in listdir(folderPath) if f.startswith(inputFileBaseName)]

for (index, fileName) in enumerate(listOfJSONFiles):
    print('reading file -> ',index, join(folderPath, fileName))
    f = open(join(folderPath, fileName), "r")
    fileDict = json.loads(f.read())
    f.close()
    if index == 0:
        # Here we just need to intitalize my output dictionary
        outputFileDict = fileDict
    else:
        # Here we need to check if my current file dictionary has a key that matches output dictionary
        # if key matches then merge the values in the existing key
        # else if key does not match then just add the new key and value to output
        for key in fileDict.keys():
            if key in outputFileDict.keys():
                outputFileDict[key].append(fileDict[key])
            else:
                outputFileDict[key] = fileDict[key]
        #print(fileDict)
        #print(outputFileDict)
        f = open(join(folderPath, outputFileBaseName + str(index)+".json") , "w")
        f.write(json.dumps(outputFileDict))
        f.close()
print("################# Execution Complete ################")
print("#####################################################")
