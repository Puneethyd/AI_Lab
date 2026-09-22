height = 1.80
weight = 75

bmi = weight / (height**2)
print(f"Your BMI is {bmi:.2f}")


if bmi < 18.5:
    print("You fall into the Underweight category.")
elif bmi <= 22.9:
    print("You fall into the Normal weight category.")
elif bmi <= 27.4:
    print("You fall into the Overweight category.")
else:
    print("You fall into the Obese category.")
