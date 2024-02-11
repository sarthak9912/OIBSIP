def calculatebmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classifybmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Invalid input! Weight and height must be greater than zero.")
        else:
            bmi = calculatebmi(weight, height)
            category = classifybmi(bmi)

            print(f"Your BMI is: {bmi:.2f}")
            print("Category:", category)

    except ValueError:
        print("Invalid input! Weight and height must be numeric values.")

if __name__ == "__main__":
    main()