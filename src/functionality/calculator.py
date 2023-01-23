import re

from src.data.calculation.coef import coef


async def calculate_score(message, faculty, speciality):
    # parse message
    grades = await parse_message(message)

    # if error in parsing return error
    if type(grades) != list:
        return grades

    # parse coeficients
    coeficients = await parse_coeficients(faculty, speciality)

    # calculate grade
    grade = sum([grades[i] * coeficients[i] for i in range(3)])

    # delete decimal point if grade is whole number
    if grade - int(grade) == 0:
        grade = int(grade)
    else:
        grade = round(grade, 3)

    return f"Ваш бал: {grade}"


async def parse_message(message):
    # look for all numbers in a message using regular expression
    grades = re.findall("[0-9]+\.?[0-9]+", message.replace(",", "."))
    # check if there are enough grades
    if len(grades) < 3:
        return "Введіть бали з трьох предметів"
    else:
        grades = grades[:3]

    # loop through every grade and try to cast it to float type
    for i in range(3):
        try:
            grade = float(grades[i])
            # check if in correct range
            if grade < 100 or grade > 200:
                return f"Введений бал {grades[i]} має бути в межах від 100 до 200"
            else:
                grades[i] = grade
        except ValueError:
            return f"Введене число {grades[i]} є невірним"

    return grades


async def parse_coeficients(faculty, speciality):
    return [float(x) for x in coef[faculty][speciality].split()]
