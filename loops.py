#for

welcome_message = "Welcome to the loops.py"

for i in [0,5,1]:
   # print("Welcome message")
    print(i)
# infinite number
    # count = 0
    # while count <= 7:
    #     # Loop Body
    #     print (count)
    #     count += 1

# clothes loop
    
    colors = ["red", "green", "blue", "white", "brown", "cream"]
    color_i_want = "blue"

                            #for loop

    # for color in colors:

    #     if color == color_i_want:
    #         print("I have found the color i want")
    #         break
    #     print(color)


              # while loop        
length = len(colors)
count = 0

while count < length:
    print (colors[count])

    if colors[count] == color_i_want:
        print("I have found the color i want")
        break
    count += 1


        #Age entrance in a club
ages = [12, 15, 18, 20, 25, 30, 32, 38]

for age in ages:
    if age <21:
        continue
    print (age)
  #Nested loops
    groups = [["Paul", "skinny"], ["Annette", "George"]]
    for group in groups:
        for name in group:
            print(name)



            