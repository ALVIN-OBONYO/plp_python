name = input("Enter your name: ")

age = input("Enter your age: ")

location = input("Enter your location: ")

print(f"Hello {name}, you are {age} years old and live in {location}.")

#  I found this way easier than the one above

name = "Alvin O"
age = 20        
location = "Nairobi, Kenya"

print (f"Hello {name}, you are {age} years old and live in {location}")

# self made 



list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]

sum = 0
sum1 = 0

for elem in list1:
    if (elem % 2 == 0):
        sum = sum + elem
        continue
    if (elem % 3 == 0):
        sum1 = sum1 + elem

print(sum , end=" ")
