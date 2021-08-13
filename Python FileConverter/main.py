import json
import csv
import yaml
yamlArray = []

def convert_csv_to_json():
    #Intializing the array of JSON
    jsonArray = []

    #opening the .csv file to read
    with open('load-csv.csv','r', encoding='utf-8') as csvFile:
        #loading csv file data using csv pakage dictionary reader
        csvReader = csv.DictReader(csvFile)

        #converting each row from the .csv file into python dictionary
        for row in csvReader:
            #appending/adding the python dictionary into the json array
            jsonArray.append(row)

        #Converting Python Dictionary to Json Object and writing to a file
        with open('csvToJson.json', 'w', encoding='utf-8') as json_file:
            json.dump(jsonArray, json_file, indent=4)

    print('\nPlease look at csvToJson.json file for csv to json conversion\n')

def convert_to_csv(fileType):
    if(fileType == "json"):
        # opening .json file and loading the data from the file into a variable
        with open('load-json.json', 'r') as jsonFile:
            jsondata = json.load(jsonFile)
            write_to_csv(jsondata, 'jsonToCsv.csv')
            print('\nPlease look at jsonToCsv.csv file for json to csv conversion\n')

    if(fileType == "yaml"):
        with open('load-yaml.yaml', 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)  # yaml_data is type of list
            write_to_csv(yaml_data, 'yamlToCsv.csv')
            print('\nPlease look at yamlToCsv.csv file for yaml to csv conversion\n')

def write_to_csv(dataType, fileName):
    #opening a new .csv file to write the Json data
    with open(fileName, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        count = 0 #to keep track of the fieldNames rows
        for data in dataType:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count = 1
            csv_writer.writerow(data.values())

def convert_yaml_to_json():
    with open('load-yaml.yaml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file) #yaml_data is type of list

        with open('yamlToJson.json', 'w', encoding='utf-8') as jsonFile:
            json.dump(yaml_data, jsonFile, indent=2)

        print('\nPlease look at yamlToJson.json file for yaml to json conversion\n')

def convert_json_to_yaml():
    with open('load-json.json', 'r') as jsonFile:
        jsondata = json.load(jsonFile)

    with open('jsonToYaml.yaml', 'w')as yaml_file:
        yaml.dump(jsondata, yaml_file)

    print('\nPlease look at jsonToYaml.yaml file for json to yaml conversion\n')

def convert_csv_to_yaml():
    csv_inFile = open('load-csv.csv', "r")
    yaml_outFile = open('csvToYaml.yaml',"w")
    csv_reader = csv.reader(csv_inFile)#csv_reader is an object
    next(csv_reader)
    for index,row in enumerate(csv_reader):
        print(row)
        convert(row)

    yaml.dump(yamlArray, yaml_outFile);
    csv_inFile.close()
    yaml_outFile.close()
    print('\nPlease look at csvToYaml.yaml file for csv to yaml conversion\n')

def convert(row):
    yamlItem = {
        "id": row[0],
        "name": row[1],
        "description": row[2],
        "commas_used": row[3],
        "created_at": row[4],
        "updated_at": row[5],
    }
    yamlArray.append(yamlItem)#yamlArray is list of dicts




load_file = input("Please enter a file format you want to load:")
write_to_file = input("Please enter a file format you want to write to:")

if (load_file == "csv" and write_to_file == "json"):
    convert_csv_to_json()
elif(load_file == "json" and write_to_file == "csv"):
    convert_to_csv("json")
elif(load_file=="yaml" and write_to_file=="json"):
    convert_yaml_to_json()
elif(load_file=="yaml" and write_to_file=="csv"):
    convert_to_csv("yaml")
elif(load_file=="json" and write_to_file=="yaml"):
    convert_json_to_yaml()
elif(load_file=="csv" and write_to_file=="yaml"):
    convert_csv_to_yaml()
else:
    print("Invalid input or output file types. Please try again!")