import re
from random import shuffle, randrange
isu = 466930

eye = isu % 6
nose = isu % 4
mouth = isu % 8


def gen_tex(): #генерирует текст
    alpha = '0123456789qwertyuiopasdfghjklzxcvbnm{}[]/\|.,<>?!'
    s = ''
    for i in alpha:
        s += i * randrange(5)
    s = list(s)
    shuffle(s)
    return ''.join(s)



def you_look_lonely(text, pattern): #программа поиска смайлов в тексте
    result = re.findall(pattern, text)
    return len(result)


smile_pattern = '=-{P'
if '|' in smile_pattern:
    smile_pattern = smile_pattern[:smile_pattern.index('|')] + '\\' + smile_pattern[smile_pattern.index('|'):]

elif '[' in smile_pattern:
    smile_pattern = smile_pattern[:smile_pattern.index('[')] + '\\' + smile_pattern[smile_pattern.index('['):]

elif '(' in smile_pattern:
    smile_pattern = smile_pattern[:smile_pattern.index('(')] + '\\' + smile_pattern[smile_pattern.index('('):]

elif ')' in smile_pattern:
    smile_pattern = smile_pattern[:smile_pattern.index(')')] + '\\' + smile_pattern[smile_pattern.index(')'):]

print(smile_pattern)
for i in range(5):
    t = gen_tex()
    for j in range(5):
        wrng = randrange(len(t) - len(smile_pattern) - 1)
        t = t[:wrng] + smile_pattern + t[wrng:]
        print(t, you_look_lonely(t, smile_pattern))

#конец первого задания

testic1 = ('Уважаемые студенты!'
           'В эту субботу в 15:00 планируется доп. занятие на 2 часа.'
           'То есть в 17:00:50 оно уже точно кончится. ')
testic2 = ('всем привет, я был в школе в 12:08 '
           'потом ходил кушать в 16:41 '
           'потом пробежал кросс за 01:22:33 как же я хорош')
testic3 = ('проснулся утром и начал смотреть NBA начиная с 06:15:00 заканчивая 08:44:43')
testic4 = ('часто смотрел фильмы начиная с 00:03:40 секунды, а потом отматывал на 05:00:47')
testic5 = ('меня всегда спрашивают, почему я ходил за цветами в 23:20, ведь можно сходить в 12:00:54')

time_pattern = r"\b([01]\d|2[0-3]):([0-5]\d)(?::([0-5]\d))?\b"
for i in [testic1, testic2, testic3, testic4, testic5]:
    sovpadeniya = re.findall(time_pattern, i)
    print(re.sub(time_pattern, '(TBD)', i))

# конец второй части
testos1 = ('<meta name="daily_volume" content="В суточным объемом торгов'
    '₽2,835,029,974,960.63 RUB."/> <meta name="daily_price" content="Мы обновляем'
    'нашу цену BTC к RUB в режиме реального времени."/> <meta name="daily_price'
    'content=" Цена Bitcoin в реальном времени сегодня составляет ₽5,797,806.88'
    'RUB."/><meta name="daily_price" content="Ethereum стоит на данный момент'
    '₽229,590,78 RUB."/>')
testos2 = ('<meta name="daily_volume" что то очень важное./> <meta name="daily_volume" сегодня цена за биткойн будет сказана в следующем сообщении./><meta name="daily_price'
    'content=" Цена Bitcoin в реальном времени сегодня составляет ₽5,797,806.88'
    'RUB."/> <meta name="daily_price" content="Ethereum стоит на данный момент'
    '₽229,590,78 RUB."/>')
testos3 = ('<meta name="daily_price" content="Ethereum стоит на данный момент'
    '₽229 RUB."/> <meta facebook apple amazom many many, yaght, boss> < сегодня концерт Drake в Купчино> ,meta data'
           ' сегодня люди не покупают биткоин, скидок не было <meta name="daily_price'
    'content=" Цена Bitcoin в реальном времени сегодня составляет ₽5,797,806.88'
    'RUB."/>')
testos4 = ('<meta name="daily_volume" content= сегодня прошли выборы в венесуэлле, победил Мадуро, сообщают источники близкие к президенту>> <<<'
           'британские ученые заявили, что если часто улыбаться, то на вас будут странно смотреть>>'
           '<<meta name warnings= сегодня после прогроммы время будут показывать сериал сопрано, бегом смотреть'
           '<meta name="daily_price'
            'content=" Цена Bitcoin в реальном времени сегодня составляет ₽5,806.88'
            'RUB."/>')
testos5 = ('<meta name="daily_price'
    'content=" Цена Bitcoin в реальном времени сегодня составляет ₽8,787,806.98'
    'RUB."/> это уже пятый тест- сообщают источники/..> << казино вылкан закрыли за невыплату налогов.>>'
           '<< ежедневный просмотр инстаграм риллсов улучшает жизнь обитателей общаги сообщает WALL STREET JOURNAL со ссылкой на источники в Б6>.'
           '<< 2226- столько раз в этом месяце студенты из Бангладеш варили паприку'
           '<<ЗАКОЛЕБАЛИ ТАРАКАНЫ- именно с такими словами житель вязьмы обедал в комнате')
pattern_zad_3 = r'<meta name="daily_pricecontent=" Цена Bitcoin в реальном времени сегодня составляет ₽[\d,.]+RUB."/>'
for i in [testos1, testos2, testos3, testos4, testos5]:
    otvet = re.findall(pattern_zad_3, i)[0]
    print(re.findall(r'[\d,.]+', otvet)[0])












