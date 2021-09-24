import csv

with open ('height-weight-copy.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
file_data.pop(0)
newData = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    newData.append(float(n_num))