print("welcom to python pizza deliveries!")
size = input("what size pizza you want? s , l , m : ")
add_pepperoni = input("do you want pepperoni?? y , n : ")
extra_cheese = input("do you want extra cheese ?? y , n : ")
bill = 0 
if size == "s" :
    bill = 15
  

elif size == " m " :
    bill = 20 
    
else :
    bill = 25 
    
if extra_cheese == "y" :
    bill += 1 
if add_pepperoni == "y" and size == "s" :
    bill += 2
else :
    bill += 3
print(f"your bill is {bill}")


