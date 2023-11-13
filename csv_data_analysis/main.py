# with open("weather_data.csv") as csv_file:
#     csv_data=csv_file.readlines()
#     print(csv_data)
import csv
with open("weather_data.csv") as csv_file:
    csv_data=csv.reader(csv_file)
    temperature=[]
    for row in csv_data:
        if row[1]!="temp":
            temperature.append(int(row[1]))
    print(temperature)
