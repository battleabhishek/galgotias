#min max scaling with input
def min_max_scale(data):
    min_val = min(data)
    max_val = max(data)
    scaled_data = [(x - min_val) / (max_val - min_val) for x in data]
    return scaled_data

    for value in data:
        scaled_value = (value - min_val) / (max_val - min_val)
        scaled_data.append(scaled_value) 
    
    return
       
#main program
data= list(map(float, input("Enter numbers separated by space: ").split()))
scaled_data = min_max_scale(data)
print("Min-Max Scaled Data:", scaled_data)
print("original data:", data)
print("sacaled data:", scaled_data)


