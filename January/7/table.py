import csv

print("Enter path to csv file you want to create/ edit")
path = input()

with open(path, 'w') as csvfile:
    fieldnames = ['nr', 'squared']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for index in range(0, 10):
        writer.writerow({'nr': index, 'squared': index*index})