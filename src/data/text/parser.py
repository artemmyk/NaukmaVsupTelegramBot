def replace_reserved_characters(dict_of_strings):
    for string in dict_of_strings:
        dict_of_strings[string] = dict_of_strings[string].replace(".", "\\.") \
            .replace(",", "\\,").replace(";", "\\;").replace("(", "\\(").replace(")", "\\)") \
            .replace("!", "\\!").replace("?", "\\?").replace("-", "\\-").replace("<@", "(").replace("@>", ")")
    return dict_of_strings
