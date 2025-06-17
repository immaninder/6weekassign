#Question1
l1=['Rangers','Mercedes','Dog','Cat','happiness','Forgive','Love','Bad','Strength','Lifestyle']
l2=[i for i in l1 if len(i)<4]
print(l2)


#Question2
l3=[i for i in range(20)]
l4=['odd' if i % 2 != 0 else 'even' for i in l3]
print(l4)

#Question3
l5=[i for i in range(1,1001)]
l6=[i for i in l5 if i%7==0]
print(l6)

#Question4
l5=['I am a student of Btech','I am Studying','I love to play Basketball','I am Happy']
spaces=0
for i in l5:
    spaces += i.count(' ')  
print("Total number of spaces in the list:", spaces)

#Question5
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
list_c=[i for i in list_a for j in list_b if i == j]
print("Common elements in both lists:",list_c)
