import math

#a = 1
#b = 5
#c = 7
print(" a quadratic equation is given ")
a = int(input('enter the value of a: '))
b = int(input('enter the value of b: '))
c = int(input('enter the value of c: '))

 
if (math.pow(b,2) < 4 * a * c):
     print("root is imaginary")
else:
     root1 = (-(b) + math.sqrt(math.pow(b,2) - 4 * a * c))/(2 * a)
     root2 = (-(b) - math.sqrt(math.pow(b,2) - 4 * a * c))/(2 * a)

     print(root1,root2)

