import csv
import json

with open('parks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Year', 'Month', 'Name', 'Value'])

    with open('./parks.json') as f:
        data = json.load(f)
        for dictionary in data:
            writer.writerow([None, None, dictionary["name"], dictionary["region"]])
