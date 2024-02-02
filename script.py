import csv

names = []
ages = []
bmis = []
insurance_costs = []

with open('insurance.csv', newline='') as csvfile:
  csv_reader = csv.DictReader(csvfile)
  for row in csv_reader:
    names.append(row[0])
    ages.append(row[1])
    bmis.append(row[2])
    insurance_costs.append(row[3])

for record in medical_records_clean:
    record[0] = record[0].upper()