# with open("weather_data.csv") as csv_file:
#     csv_data=csv_file.readlines()
#     print(csv_data)
# import csv
# with open("weather_data.csv") as csv_file:
#     csv_data=csv.reader(csv_file)
#     temperature=[]
#     for row in csv_data:
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#     print(temperature)
import pandas

csv_data = pandas.read_csv("weather_data.csv")

# csv_dict = csv_data.to_dict()
# print(csv_dict)

temp_list=csv_data["temp"].to_list()
print(temp_list)
