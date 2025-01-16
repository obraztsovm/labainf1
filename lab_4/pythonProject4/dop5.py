import json
import dop5_pb2  # Импортируем сгенерированный файл

# Ваш JSON
json_data = '''{
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
          }
        ]
      }
    ]
  }
}'''

# Загружаем JSON
data = json.loads(json_data)

# Создаем объект Schedule
schedule = dop5_pb2.Schedule()

# Перебираем дни и добавляем их в protobuf
for day_data in data['site']['date']:
    day = schedule.date.add()
    day.date_full = day_data['date_full']
    day.date_short = day_data['date_short']

    # Перебираем уроки в каждом дне
    for lesson_data in day_data['Sheet']:
        lesson = day.Sheet.add()
        lesson.time = lesson_data['time']
        lesson.weeks = lesson_data['weeks']
        lesson.group = lesson_data['group']
        lesson.place = lesson_data['place']
        lesson.name = lesson_data['name']
        lesson.format = lesson_data['format']

# Выводим сериализованный protobuf объект
print(schedule)

# Если нужно, сериализуем объект в строку
serialized_data = schedule.SerializeToString()

# Пример десериализации обратно
schedule_parsed = dop5_pb2.Schedule()
schedule_parsed.ParseFromString(serialized_data)

# Выводим десериализованные данные
print(schedule_parsed)
