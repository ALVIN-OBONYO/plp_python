#  WEEK 3 ASSIGNMENT

def calculate_discount(price, discount_percentage):
    return price * discount_percentage / 100

discount = calculate_discount(100, 10) 
print(discount)




#if else 

Mary = 20

if Mary > 18:
    print("Mary can vote")


grade = 75

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

    





weekday = "Monday" , "Tuesdy" , "Wednesday" , "Thursday" , "Friday"
Weekend = "Saturday" , "Sunday"

Weekday = "Sunday"


if Weekday:
    print("Wake up at 6:30")
else: 
    print("sleep in")
