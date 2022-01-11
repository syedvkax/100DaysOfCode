height = float(input("Please Enter your height in m: "))
weight = float(input("Please Enter your weight in kg: "))

# BMI Calculator
bmiCalculator = weight/height ** 2

if bmiCalculator < 18.5:
  print("Your BMI is ",bmiCalculator," You are underwight")
elif bmiCalculator <= 25.0:
  print("Your BMI is ",bmiCalculator," You have normal weight")
elif bmiCalculator <= 30.0:
  print("Your BMI is ",bmiCalculator," You are over weight")
elif bmiCalculator <= 35.0:
  print("Your BMI is ",bmiCalculator," You are obese")
elif bmiCalculator <= 35.0:
  print("Your BMI is ",bmiCalculator," You are clinically obese")
else:
  print("Invalid Input")