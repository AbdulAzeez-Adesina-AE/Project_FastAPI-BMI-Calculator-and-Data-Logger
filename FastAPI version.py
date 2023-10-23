import csv
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def calculate_bmi(height: float, weight: float) -> float:
    # Calculate BMI (BMI = weight(kg) / (height(m) ^ 2))
    return weight / (height ** 2)

def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

@app.post("/calculate_bmi")
async def calculate_bmi(
    Full_name: str = Form(...),
    Age: int = Form(...),
    Sex: str = Form(...),
    height: float = Form(...),
    weight: float = Form(...)
):
    bmi = calculate_bmi(height, weight)
    category = bmi_category(bmi)

    with open("BMI_Survey_Data.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Full Name", "Age", "Sex", "Height", "Weight", "BMI Index", "Category"])
        writer.writerow([Full_name, Age, Sex, height, weight, bmi, category])

    return {"Full Name": Full_name, "BMI": bmi, "Category": category}

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("bmi_form.html", {"request": request})
