#input in python
name=input("Enter your name: ")
print("Hello, "+name)

#coontrol flow in python
marks=int(input("Enter your marks: "))
valid=[]

for m in marks:
    if m>=90:
        valid.append("A")
    elif m>=80:
        valid.append("B")
    elif m>=70:
        valid.append("C")
    elif m>=60:
        valid.append("D")
    else:
        valid.append("F")
        
print(valid)

#catagrise students based on their marks
marks= 82 

if marks >=75:
     print("desigination")
elif marks >=60:
    print("first class")
elif marks >=40:
    print("pass")
else:
    print("fail")
    
#count pass student
marks = [35,50,60,20,80]
count=0
for m in marks:
    if m>=40:
        count+=1
print("Number of pass students: ",count)

#function
#pass fail
def pass_fail(marks):
    if marks>=40:
        return "pass"
    else:
        return "fail"
print (check_pass(55))

#normalisatin feaature
def normalize(feature):
    min_value=min(feature)
    max_value=max(feature)
    normalized_feature=[(x-min_value)/(max_value-min_value) for x in feature]
    return normalized_feature
print(noramlise(75,55,65))

#calculate mean
def calculate_mean(numbers):
    return sum(numbers)/len(numbers)
print(calculate_mean(45,55,65))

#attandance eligibility
def check_attendance(attendance_percentage):
    if attendance_percentage>=75:
        return "eligible"
    else:
        return "not eligible"
    
    
#file io
#reading a file
file = open(marks.text,"r")
content=file.read()
file.close()
print(content)

#write processed data to a file
file = open("processed_marks.txt","w")
file.write("data proceesed successfully")
file.close()

#read csv and print columb
import csv

with open("student_data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row[0]) #print first columb
        
#generate clean data set
import csv
with open("raw_data.csv","r") as infile, \
     open("clean_data.csv","w",newline="") as outfile:
    reader=csv.dictreader(infile)
    fieldnames=reader.fieldnames + ["result"]
    writer=csv.dictwriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        marks = int(row["marks"])
        result = 1 if marks >= 40 else 0
        row["result"]=result
        writer.writerow(row)

    
 

