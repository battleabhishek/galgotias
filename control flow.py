#control flow,function,file io for ml
#control flow
# if else statement
x = 10
if x > 5:
    print("x is greater than 5")    
else:
    print("x is less than or equal to 5")
# if elif else statement
y = 20
if y > 30:
    print("y is greater than 30")
elif y > 10:
    print("y is greater than 10 but less than or equal to 30")
else:
    print("y is less than or equal to 10")

#data filtering for ml
#valuenless then 0(invalid data)
#value b/w 0 and 1(normalized data)
#value greater than 1(outliers)
data = [0.5, 0.8, -0.2, 1.5, 0.3]
filtered_data = []
for value in data:
    if value < 0:
        print(f"Invalid data: {value}")
    elif 0 <= value <= 1:
        filtered_data.append(value)
    else:
        print(f"Outlier: {value}")
print("Filtered data:", filtered_data)

#print the no. of invalid data,normalized data and outliers
data = [-1, 0.5, 2, 0.8, -0.5, 1.5, 0.2]
invalid_data = 0
normalized_data = 0
outliers = 0
for i in data:
    if i < 0:
        invalid_data += 1
    elif i >= 0 and i <= 1:
        normalized_data += 1
    else:
        outliers += 1
print("Invalid data: ", invalid_data)
print("Normalized data: ", normalized_data)
print("Outliers: ", outliers)