def bmi(weight, height):
    mass_index = weight/height**2
    if mass_index < 18:
        return "Underweight"
    elif mass_index >= 18 and mass_index < 25:
        return "Normal"
    elif mass_index >= 25 and mass_index < 30:
        return "Overweight"
    else:
        return "Obesity"
print(bmi(85, 1.9))
