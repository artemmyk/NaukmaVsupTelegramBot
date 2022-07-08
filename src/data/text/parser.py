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
    return string.replace(".", "\\.") \
                .replace(",", "\\,").replace(";", "\\;").replace("(", "\\(").replace(")", "\\)") \
                .replace("!", "\\!").replace("?", "\\?").replace("-", "\\-").replace("<@", "(").replace("@>", ")") \
                .replace("на сайті НаУКМА", "на сайті Могилянки").replace("сайт приймальної комісії НаУКМА",
                                                                          "сайт приймальної комісії Могилянки")