#cal mmean satndard deviation with csv file
import csv
import math

data = []

#read data from csv file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        if row:  # Check if the row is not empty
            data.append(float(row[0]))
            
#calculate mean
mean = sum(data) / len(data)

#calculate standard deviation
variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = math.sqrt(variance)

#write staticsics to csv file
with open('statistics.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Mean', 'Standard Deviation'])
    writer.writerow([mean, std_dev])
    writer.writerow(['matric', 'value'])
    writer.writerow(['Mean', mean])
    writer.writerow(['Standard Deviation', std_dev])

#print statistics
print("Statistics have been written to statistics.csv")


#print mean and standard deviation
print("Mean:", mean)
print("Standard Deviation:", std_dev)

