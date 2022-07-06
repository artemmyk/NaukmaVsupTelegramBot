from data.info.coef import coef


def calculate_score(message, faculty, speciality):
    # parse message
    grades = parse_message(message)

    # if error in parsing return error
    if type(grades) != list:
        return grades

    # parse coeficients
    coeficients = parse_coeficients(faculty, speciality)

    # calculate grade
    grade = sum([grades[i] * coeficients[i] for i in range(3)])

    # delete decimal point if grade is whole number
    if grade - int(grade) == 0:
        grade = int(grade)

    return f"Ваш бал: {grade}"


def parse_message(message):
    # split message into words by spaces
    words = message.split()

    # check if enough words (has to be 3)
    # if more than 3 take only first 3
    if len(words) < 3:
        return "Введіть бали з трьох предметів"
    else:
        words = words[:3]

    # check if words are numbers
    # if numbers also check if in correct range
    grades = []
    for word in words:
        try:
            grade = float(word.replace(",", "."))
            if grade < 100 or grade > 200:
                return f"Введений бал {word} має бути в межах від 100 до 200"
            else:
                grades.append(grade)
        except ValueError:
            return f"Введене число {word} є невірним"

    return grades


def parse_coeficients(faculty, speciality):
    return [float(x) for x in coef[faculty][speciality].split()]
