import json
import xml.etree.ElementTree as ET


# Грамматические правила
def json_to_xml(json_obj, root_tag="root"):
    """
    Преобразует Python объект (словарь или список) в XML строку.
    """

    # Правила для преобразования JSON объекта в XML
    def json_object_to_xml(tag, obj):
        """Преобразует JSON объект в XML элементы"""
        element = ET.Element(tag)
        for key, value in obj.items():
            # Применяем правило преобразования для каждого ключа и значения
            element.append(json_value_to_xml(key, value))
        return element

    def json_array_to_xml(tag, arr):
        """Преобразует JSON массив в XML элементы"""
        element = ET.Element(tag)
        for item in arr:
            element.append(json_value_to_xml("item", item))
        return element

    def json_value_to_xml(tag, value):
        """Преобразует JSON значение в XML элемент"""
        if isinstance(value, dict):
            return json_object_to_xml(tag, value)  # Применяем правило для объекта
        elif isinstance(value, list):
            return json_array_to_xml(tag, value)  # Применяем правило для массива
        else:
            # Применяем правило для примитивного значения
            element = ET.Element(tag)
            element.text = str(value)
            return element

    # Создаем корневой элемент XML
    root = ET.Element(root_tag)

    # Применяем правило для главного объекта
    for key, value in json_obj.items():
        root.append(json_value_to_xml(key, value))

    # Преобразуем дерево XML в строку
    tree = ET.ElementTree(root)
    xml_str = ET.tostring(root, encoding='unicode', method='xml')

    # Возвращаем XML строку с заголовком
    return f'<?xml version="1.0" encoding="UTF-8"?>\n{xml_str}'


def convert_json_to_xml(json_data):
    """Основная функция для конвертации JSON в XML"""
    # Загружаем JSON
    json_obj = json.loads(json_data)

    # Преобразуем в XML
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
