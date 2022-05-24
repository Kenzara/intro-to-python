#Boolean

print(2 > 3) 
print(2 == 3) 
print("b" > "ant") 
print("BAG" == "BAG") 
print(2 < 3) 

#conditional statement
age = 24
if (age > 18):
    print("adult")
print("enter age:") 

"""
      (Q1)  Write a program to find the eligibility of admission for a professional 
      course based on the following criteria:
        Eligibility Criteria : 
        Marks in Maths >=65 and Marks in Phy >=55 and Marks in Chem>=50 
        and Total in all three subject >=190 or Total in Maths and Physics >=140
        --------------------------Format-------------------------
        Input the marks obtained in Physics :65 Input the marks obtained in Chemistry :51 
        Input the marks obtained in Mathematics :72 
        Total marks of Maths, Physics and Chemistry : 188
         Total marks of Maths and Physics : 137 
         The candidate is not eligible.
        Expected Output :
        The candidate is not eligible for admission.
    """


#math >= 65
#chem >= 50
#phy  >= 55
#all_subjects >= 190
#total_maths_&_physic >= 140


physics = int(input('Input the marks obtained in Physics: '))
chem = int(input('Input the marks obtained in Chemistry: '))
maths = int(input('Input the marks obtained in Mathematics: '))

if ((maths + physics >= 140 or chem + maths + physics >= 190) and 
(maths >= 65 and chem >= 50 and physics >= 55)):
    message = "The candidate is eligible for admission."
else:
    message = "The candidate is not eligible for admission."

print(message)


""" (Q2) Write a program to calculate the root of a Quadratic Equation.
            Test Data : 1 5 7
            Expected Output :
            Root are imaginary;
            No solution.
    """

    """(Q3) Write a program to read temperature in centigrade and display a suitable message according to temperature state below : Go to the editor
        Temp < 0 then Freezing weather
        Temp 0-10 then Very Cold weather
        Temp 10-20 then Cold weather
        Temp 20-30 then Normal in Temp
        Temp 30-40 then Its Hot
        Temp >=40 then Its Very Hot
        Test Data :
        42
        Expected Output :
        Its very hot.
    """

    """Write a program to read the value 
    of an integer m and 
    display the value of n is 1
     when m is larger than 0, 
     0 when m is 0 and -1 
     when m is less than 0.
        Test Data : -5
        Expected Output :
        The value of n = -1
    """