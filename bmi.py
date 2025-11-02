def calculate_bmi(height, weight):
    print("Height="+str(height))
    print("Weight="+str(weight))

    bmi = weight/(height**2)
    print("BMI =" + str(bmi))

    if bmi < 18.5:
        print("User is Under Weight")
    elif bmi >= 18.5 and bmi <=25.0 :
        print("User is Normal weight")
    elif bmi > 25.0 :
        print("User is Over Weight")

calculate_bmi(weight=80, height=1.7)