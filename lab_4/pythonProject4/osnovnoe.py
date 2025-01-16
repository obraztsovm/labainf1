# Простой код для разбора JSON и преобразования в XML
# основное задание
# Разбираем число
def __parse_number(string):
    number = ""

    number_chars = "0123456789.Ee-+"
    for char in string:
        if char in number_chars:
            number += char
        else:
            break

    if number.isnumeric():
        return int(number), string[len(number):].strip()
    else:
        try:
            return float(number), string[len(number):].strip()
        except ValueError:
            return None

# Разбираем строки в двойных кавычках
def __parse_string(string):
    if not string.startswith('"'):
        return None

    second_quote = string.find('"', 1)
    if second_quote == -1:
        return None

    return string[1:second_quote], string[second_quote + 1:].strip()

# Разбираем булевы значения
def __parse_bool(string):
    if string.startswith("true"):
        return True, string[4:].strip()
    if string.startswith("false"):
        return False, string[5:].strip()

# Разбираем null
def __parse_null(string):
    if string.startswith("null"):
        return None, string[4:].strip()

# Проверка на наличие двоеточия
def __parse_colon(string):
    if string.startswith(":"):
        return ":", string[1:].strip()

# Проверка на наличие запятой
def __parse_comma(string):
    if string.startswith(","):
        return ",", string[1:].strip()

# Разбираем пару ключ-значение
def __parse_keyvalue(string):
    parsed_string = __parse_string(string)
    if parsed_string is None:
        return None
    parsed_colon = __parse_colon(parsed_string[1])
    if parsed_colon is None:
        return None
    parsed_value = __parse_value(parsed_colon[1])
    if parsed_value is None:
        return None
    return (parsed_string[0], parsed_value[0]), parsed_value[1].strip()

# Разбираем список значений, разделенных запятыми
def __parse_comma_separated_values(string):
    res = []
    while True:
        parsed_value = __parse_value(string)
        if parsed_value is None:
            break
        res.append(parsed_value[0])
        string = parsed_value[1]

        parsed_comma = __parse_comma(string)
        if parsed_comma is None:
            break
        string = parsed_comma[1]

    if not res:
        return None

    return res, string.strip()

# Разбираем список пар ключ-значение
def __parse_comma_separated_keyvalues(string):
    res = {}
    while True:
        parsed_keyvalue = __parse_keyvalue(string)
        if parsed_keyvalue is None:
            break
        key, value = parsed_keyvalue[0]
        res[key] = value
        string = parsed_keyvalue[1]

        parsed_comma = __parse_comma(string)
        if parsed_comma is None:
            break
        string = parsed_comma[1]
    return res, string.strip()

# Разбираем массив (объект в квадратных скобках)
def __parse_array(string):
    if not string.startswith("["):
        return None
    parsed_sepvalues = __parse_comma_separated_values(string[1:].strip())
    if parsed_sepvalues is not None:
        arr, string = parsed_sepvalues
    else:
        arr, string = [], string[1:]
    if not string.startswith("]"):
        return None
    return arr, string[1:].strip()

# Разбираем объект (объект в фигурных скобках)
def __parse_object(string):
    if not string.startswith("{"):
        return None
    arr, string = __parse_comma_separated_keyvalues(string[1:].strip())
    if not string.startswith("}"):
        return None
    return arr, string[1:].strip()

# Общая функция для разбора значений (число, строка, булевое значение, null, массив, объект)
def __parse_value(string):
    parsers = [
        __parse_number,
        __parse_string,
        __parse_bool,
        __parse_null,
        __parse_array,
        __parse_object,
    ]
    for parser in parsers:
        result = parser(string)
        if result is not None:
            return result
    return None

# Преобразуем данные в формат XML
def dump2xml(dict_, tag_name="root"):
    xml = ""
    for key, value in dict_.items():
        underscores_key = key.replace(" ", "_")
        open_tag = "<" + underscores_key + ">"
        close_tag = "</" + underscores_key + ">"

        if isinstance(value, dict):
            xml += dump2xml(value, key)
        elif isinstance(value, list):
            xml += (
                open_tag
                + "".join([dump2xml({key + "_elem": elem}, "") for elem in value])
                + close_tag
            )
        else:
            xml += open_tag + str(value) + close_tag
    if tag_name == "":
        return xml
    return "<" + tag_name.replace(" ", "_") + ">" + xml + "</" + tag_name.replace(" ", "_") + ">"

# Парсим JSON строку
def parse_json(string):
    string = string.strip()
    parsed_value = __parse_value(string)

    if parsed_value is None:
        raise ValueError("not a valid JSON string")
    if parsed_value[1].strip():
        raise ValueError("not a valid JSON string")

    return parsed_value[0]



# Основной код

json_string = '''{
  "site": {
    "date": [
      {
        "date_full": "Понедельник",
        "date_short": "Пн",
        "Sheet": [
          {
            "time": "08:20-09:50",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/1",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          },
          {
            "time": "10:00-11:30",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/1",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          },
          {
            "time": "11:40-13:10",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/4",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          },
          {
            "time": "13:30-15:00",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/4",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          },
          {
            "time": "15:20-16:50",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/8",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          },
          {
            "time": "17:00-18:30",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/8",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          }
        ]
      },
      {
        "date_full": "Суббота",
        "date_short": "Сб",
        "Sheet": [
          {
            "time": "08:20-09:50",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/1",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          },
          {
            "time": "10:00-11:30",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/1",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          },
          {
            "time": "11:40-13:10",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/4",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          },
          {
            "time": "13:30-15:00",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/4",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          },
          {
            "time": "15:20-16:50",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/8",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          },
          {
            "time": "17:00-18:30",
            "weeks": "2, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17",
            "group": "АЯ-B1.1/8",
            "place": "3212 ауд. ул.Ломоносова, д.9, лит. Е",
            "name": "АНГЛИЙСКИЙ ЯЗЫК B1.1 (Прак)",
            "format": "Очно - дистанционный"
          }
        ]
      }
    ]
  }
}'''


# Парсим JSON строку
parsed_data = parse_json(json_string)

# Преобразуем в XML
xml_output = dump2xml(parsed_data)
print(xml_output)
# необходимо добавить заголовок

