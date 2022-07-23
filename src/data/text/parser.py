def replace_reserved_characters(dict_of_strings):
    for element in dict_of_strings:
        if type(dict_of_strings[element]) is dict:
            for string in dict_of_strings[element]:
                dict_of_strings[element][string] = replace(dict_of_strings[element][string])
        else:
            dict_of_strings[element] = replace(dict_of_strings[element])

    return dict_of_strings


def replace(string):
    if string.startswith("https"):
        return string
    return string.replace("[сайт приймальної комісії НаУКМА]<@https://vstup.ukma.edu.ua/golovna/pryjmalna-komisiya/@>",
                          "[сайт]<@https://vstup.ukma.edu.ua/@> приймальної комісії НаУКМА") \
        .replace("https://vstup.ukma.edu.ua/wp-content/uploads/2022/05/motyvaciyniy_lyst_2022.pdf",
                 "https://vstup.ukma.edu.ua/bachelor/motyvaciyniy-lyst-2022") \
        .replace("МТНК(магістерський тест навчальної компетентності) та фаховий іспит",
                 "МТНК(магістерський тест навчальної компетентності) та фаховий іспит (детальніше [тут]<@https://vstup.ukma.edu.ua/master-degree/mkt-mtnk@>)") \
        .replace("на сайті НаУКМА", "на сайті Могилянки") \
        .replace(".", "\\.") \
        .replace(",", "\\,").replace(";", "\\;").replace("(", "\\(").replace(")", "\\)") \
        .replace("!", "\\!").replace("?", "\\?").replace("-", "\\-").replace("<@", "(").replace("@>", ")") \

