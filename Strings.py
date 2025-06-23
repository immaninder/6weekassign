# question 1
name=input("name of the student")
Class = int(input("class of the student"))
section=input("section of the student")
a=int(input(" marks in english"))
b=int(input("marks in maths "))
c=int(input("marks in hindi"))
d=int(input("marks in sst"))
e=int(input("marks in evs"))
total= a+b+c+d+e
percent=total/5
print(name)
print(Class)
print(section)
print(percent)

# question 2
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
sum=a+b+c
print(sum)

#question 3
a=int(input("a:"))
print("square of a is:", a**2)

#question 4

temp=input("temperature is celcius:")
temp=float(temp)
print(temp)
 temp=(temp*9/5)+32
print("temperature in fahrenhiet is:", temp)

#question 5
a=int(input("a:"))
b=int(input("b:"))
print("quotient",a//b )
print("remaninder",a%b)
