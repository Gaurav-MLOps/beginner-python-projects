weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pound? (k or lb): ").lower()

if unit == "k":
    weight = weight * 2.205
    unit = "Lb"
    print(f"Your weight is: {round(weight, 1)} {unit}")

elif unit == "lb":
    weight = weight / 2.205
    unit = "Kg"
    print(f"Your weight is: {round(weight, 1)} {unit}")

else:
    print(f"{unit} is not valid!")