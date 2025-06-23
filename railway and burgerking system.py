# #railway ticket booking system
print("Welcome to CodeRail Railway Booking System ")
name=input("\nEnter your name: ")
age=int(input("Enter your age: "))
final_price = 0
classes={1: "First Class", 2: "Second Class", 3: "Third Class"}
print("\nclasses available:")
print("1. First Class - Rs. 1500")
print("2. Second Class - Rs. 1000") 
print("3. Third Class - Rs. 500") 
c=input("Choose a travel class(1/2/3): ")
if c == '1':
     final_price = 1500
elif c == '2':
     final_price = 1000
elif c == '3':
     final_price = 500
else:
     print("Invalid choice. Please restart the program and choose a valid class.")
     exit()
if age<5:     final_price = 0
elif age>60:
     final_price = final_price * 0.8
else:
     final_price = final_price

meal=input("Do you want to add a meal? (yes/no): ")
if meal == 'yes':
     final_price += 200 
elif meal == 'no': 
     final_price = final_price
else:
     print("Invalid choice for meal. Please restart the program and choose 'yes' or 'no'.")
     exit()
print("Ticket Summary: ")
print("Name: ",name)
print("Age: ",age)    
print("Travel Class: ",classes[int(c)])
print("Meal Included: ",meal)
print("Final Price: ", final_price)
print("Enjoy your journey")


#Burger King System
print("Welcome to Burger King System")        
print("\nMenu:") 
print("1. whopper Burger - Rs. 150")
print("2. Crispy Veg - Rs. 100")  
print("3. Chicken Wings - Rs. 120")
c = input("Choose an item (1/2/3): ")                               
if c == '1':
    price = 150
elif c == '2':
    price = 100
elif c == '3':
    price = 120
else:
    print("Invalid choice.")            
    exit()
q = int(input("Enter the quantity: "))      
total_price = price * q
coupon = input("Do you have a coupon? (yes/no): ")
if coupon == 'yes':
    coupon_code = input("Enter the coupon code: ")
    if coupon_code == 'KING50':
        total_price *= 0.5 
    elif coupon_code == 'BK20':
        total_price *= 0.8
        print("Applying Coupon")
else:
        print("No Coupon applied. No discount applied.")
print("Order Summary:")
print("Item: ", c)      
print("Quantity: ", q)
print("Total Price: Rs.", total_price)  
print("Thank you for choosing Burger King! Enjoy your meal!")
