import csv
import json

#loading row_list to a .csv file
row_list = [["id", "name", "description", "commas_used", "created_at", "updated_at"],
             [1, "Test", "Test Entry", ",,,", "2020-01-01", "2020-01-01"],
             [2, "Test1", "Test 1 Entry", ",,,,,,", "2020-01-01", "2020-10-05"],
             [3, "Test2", "Test 2 Entry", ",", "2020-03-04", "2020-03-05"]]
with open('load-csv.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

#loading jsonArray to a .json file
jsonArray = [
    {
        "id": "1",
        "name": "Test",
        "description": "Test Entry",
        "commas_used": ",,,",
        "created_at": "2020-01-01",
        "updated_at": "2020-01-01"
    },
    {
        "id": "2",
        "name": "Test1",
        "description": "Test 1 Entry",
        "commas_used": ",,,,,,",
        "created_at": "2020-01-01",
        "updated_at": "2020-10-05"
    },
    {
        "id": "3",
        "name": "Test2",
        "description": "Test 2 Entry",
        "commas_used": ",",
        "created_at": "2020-03-04",
        "updated_at": "2020-03-05"
    }
]
with open('load-json.json', 'w', encoding='utf-8') as jsonFile:
    json.dump(jsonArray, jsonFile, indent=4)


