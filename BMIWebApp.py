import streamlit as slt
from helper import *

slt.title("BMI Web App")
weight_format = slt.radio("Select Your Weight Format", ("Kilograms", "Pounds"))
weight = slt.number_input(f"Enter your weight (in {weight_format})", value = 50)

height_format = slt.radio("Select Your Height Format:", ("Centimeters", "Meters", "Inches"))
height = slt.number_input(f"{height_format}")

calculate = slt.button("Calculate BMI")
if calculate:
    bmi = calculate_bmi(weight, height, height_format, weight_format)
    slt.text("Your BMI is " + str(bmi))

    if bmi < 18.5:
        slt.error("Underweight")
    elif 18.5 <= bmi < 24.9:
        slt.success("Healthy")
    elif 24.9 <= bmi < 30:
        slt.warning("Overweight")
    else:
        slt.error("Obesese")