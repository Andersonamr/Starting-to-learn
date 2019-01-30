#BMI Calculator with Inputs

print("Hello, here you find out where's your body health quality, please provide the numbers in metric format.")

name = input("What's your name? ")
height = float(input("Whats your height? "))
weight = float(input("What's your weight? "))

height2 = height/100
bmi = weight/height2 ** 2

if bmi < 18.5:
    print("Hey", name, "your BMI is:", bmi)
    print("You're Underweight!")
elif bmi >= 18.6 and bmi < 24.9:
    print("Hey", name, "your BMI is:", bmi)
    print("You're Normal Weight!")
elif bmi >= 25 and bmi < 29.9:
    print("Hey", name, "your BMI is:", bmi)
    print("You're Overweight!")
elif bmi > 30:
    print("Hey", name, "your BMI is:", bmi)
    print("You're in obesity phase, be careful!")
