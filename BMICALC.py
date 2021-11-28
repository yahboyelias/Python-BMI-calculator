#BODYMASS INDEX CALC
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#BODY MATH CALCULATION
height_calcualtions = weight / height ** 2
Body_calc2 = round(float(height_calcualtions))

#BMI CONDITIONS
if Body_calc2 < 18.5:
    print("You are underweight" + ", your current BMI is " + str(Body_calc2))
    
elif Body_calc2 <= 25:
    print("You have a normal weight" +   ", your current BMI is " + str(Body_calc2))

elif Body_calc2 <= 30:
    print("You are slightly overweight" +  ", your current BMI is " + str(Body_calc2))

elif Body_calc2 <= 35:
    print("You are obese" +  ", your current BMI is " + str(Body_calc2))

elif Body_calc2 > 35:
    print("You are clinically obese" +  ", your current BMI is " + str(Body_calc2))
 
 
 
