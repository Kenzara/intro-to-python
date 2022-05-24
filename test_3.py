import math
temp = int(input("Enter the temperature: ")) 
    
if(temp <= 0):
    print("freezing weather")

elif(temp > 0 and temp <=10):
    print("very cold weather")
elif(temp > 10 and temp <=20):
    print("cold weather")
elif(temp > 20 and temp <=30):
    print("normal weather")
elif(temp > 30 and temp <=40):
    print("it's hot")
else:
    print("out of bound")