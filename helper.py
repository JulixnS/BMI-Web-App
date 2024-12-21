import math 


def kg_to_lb(kg):
    return kg * 2.2
def lb_to_kg(lb):
    return lb / 2.2

def calculate_bmi(weight, height, height_format = "centimeters", weight_format = "kilograms"):
    print("Height", height, "Weight", weight, "height_format", height_format)

    if weight_format.lower() == "pounds":
        weight = lb_to_kg(weight)

    match height_format.lower():
        case "centimeters":
            print("KG - CM")
            return round(weight / math.pow(height, 2) * 10000, 2)
        case "meters":
            print("KG - M")
            return round(weight / math.pow(height, 2), 2)
        case "inches":
            return round(weight / math.pow(height * 2.4, 2) * 10000, 2)

if __name__ == "__main__":
    print(calculate_bmi(200, 70, "inches", "pounds"))
    print(kg_to_lb(1))