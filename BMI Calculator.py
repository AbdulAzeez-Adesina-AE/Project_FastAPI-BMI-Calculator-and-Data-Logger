import csv

def user_details():
    Full_name = input("What is Your Full name: ")
    Age = int(input("How old are you: "))
    Sex = input("Are you Male or Female: ")
    height = float(input("Type your height in Metres: "))
    weight = int(input("What is your weight in Kg: "))
    return Full_name, Age, Sex,height, weight

def BM_Index_calculator(height, weight):
    BM_Index = (weight) / (height**2)
    return BM_Index

def BM_Index_category(BM_Index_Value):
    if BM_Index_Value < 18.5:
        return "Underweight"
    elif 18.5 <= BM_Index_Value < 24.9:
        return "Normal weight"
    elif 25 <= BM_Index_Value < 29.9:
        return "Overweight"
    else:
        return "Obese"


while True:
    Full_name, Age, Sex, height, weight = user_details()
    BM_Index = BM_Index_calculator(height, weight)
    print(f"Your BMI value is {BM_Index} ")
    Category = BM_Index_category(BM_Index)
    print(f"Your BMI Category is {Category}. ")
    print('-'*38)

    with open("BMI_Survey_Data.csv", mode='a', newline='') as file:
    
        header = ["Full Name", "Age", "Sex", "Height", "Weight", "BMI Index", "Category"]
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(header)
        writer.writerow([Full_name, Age, Sex, height, weight, BM_Index, Category])
