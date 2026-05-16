#comment
#this is a comment
#multiline """"......"""(three ouble quotes)

#print function
salary=7000
print("my salary is",salary)
print("total salary is", salary)
print("my",salary,"is good")

#input function
name=input("enter your name")
print("my name is",name)
#data types
a=10
b=3.14  
c="hello"
print(type(a))
print(type(b))
print(type(c))

#two values with seprate comma
x,y=int(input("enter two numbers").split())
print("the sum is",x+y)

#if satement
age=int(input("enter your age"))
if age>=18:
    print("you are eligible to vote")   
else: 
    print("you are not eligible to vote")

#multi condtion
marks=int(input("enter your marks"))
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")
elif marks>=70:
    print("grade C")
else:
    print("grade D")

#for loop
for i in range(5):
    print(i)    
    
    