# доп задание 1
import json
import xml.etree.ElementTree as ET


def json_to_xml(json_obj, root_tag="root"):
    """
    Преобразует Python объект (словарь или список) в XML строку.
    """

    def create_xml_element(tag, value):
        """Создает XML элемент для заданного тега и значения."""
        if isinstance(value, dict):
            # Если значение - словарь, создаем вложенные элементы
            element = ET.Element(tag)
            for key, val in value.items():
                element.append(create_xml_element(key, val))
            return element
        elif isinstance(value, list):
            # Если значение - список, создаем элемент для каждого элемента списка
            element = ET.Element(tag)
            for item in value:
                element.append(create_xml_element("item", item))
            return element
        else:
            # Для других типов данных (строки, числа) создаем текстовое значение
            element = ET.Element(tag)
            element.text = str(value)
            return element

    # Создаем корневой элемент
    root = ET.Element(root_tag)

    # Заполняем XML элементами на основе JSON
    for key, value in json_obj.items():
        root.append(create_xml_element(key, value))

    # Преобразуем дерево XML в строку
    tree = ET.ElementTree(root)
    xml_str = ET.tostring(root, encoding='unicode', method='xml')

    # Возвращаем XML строку с добавленным заголовком
    xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
    return xml_declaration + xml_str


def convert_json_to_xml(json_data):
    # Загружаем JSON
    json_obj = json.loads(json_data)

    # Конвертируем в XML
    return json_to_xml(json_obj)


# Пример JSON данных
json_data = '''
{
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
}
'''

# Конвертируем JSON в XML
xml_result = convert_json_to_xml(json_data)

# Выводим результат
print(xml_result)
# тут присутствует одна регулярка, когда первую строку xml файла добавляют
