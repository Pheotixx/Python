from collections import Counter
import csv

with open ('height-weight-copy.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
file_data.pop(0)
newData = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    newData.append(float(n_num))

data = Counter(newData)
modeData_for_range = {
                        "50-60" : 0,
                        "60-70" : 0,
                        "70-80" :0
                     }

for height,occurence in data.items():
    if 50<float(height)<60:
        modeData_for_range["50-60"] += occurence
    elif 60<float(height)<70:
        modeData_for_range["60-70"] += occurence
    elif 70<float(height)<80:
        modeData_for_range["70-80"] += occurence

modeRange,mode_occurence = 0,0

for range,occurence in modeData_for_range.items():
    if occurence>mode_occurence:
        modeRange,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((modeRange[0] + modeRange[1])/2)

print(mode)