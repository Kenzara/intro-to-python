maths = 65
phy = 55 
chem = 50

maths = int(input('input the marks obtained in maths: '))
phy= int(input('input the marks obtained in phy: ' ))
chem = int(input('input the marks obtained in chem: '))

if ((maths + phy >= 140 or maths + chem + phy >= 190)
and (maths >= 65 and phy >= 55 and chem >=50)):
    message = ' the candidate is eligble for admission.'
else:
    message = 'the candidate is not eligible for admission.'
print(message)


