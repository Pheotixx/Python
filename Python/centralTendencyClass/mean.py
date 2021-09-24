import csv

with open ('height-weight-copy.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
file_data.pop(0)
new_Data=[]

for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_Data.append(float(n_num))

#to get the mean
n = len(new_Data)
total = 0

for x in new_Data:
    total += x

mean = total/n

print("The average is " + str(mean))