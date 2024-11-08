def hamming74(x: str) -> (str, str):
    r1 = int(x[0])
    r2 = int(x[1])
    r3 = int(x[3])
    i1 = int(x[2])
    i2 = int(x[4])
    i3 = int(x[5])
    i4 = int(x[6])
    s1 = str((r1 + i1 + i2 + i4) % 2)
    s2 = str((r2  + i1 + i3 + i4) % 2)
    s3 = str((r3 + i2 + i3 + i4) % 2)
    kost = (s1 + s2 + s3)[::-1]
    otv = int(kost, 2)
    if otv == 1:
        return f'{(not r1) * 1}{r2}{i1}{r3}{i2}{i3}{i3}{i4}', 'ошибка r1'
    if otv == 2:
        return f'{r1}{(not r2) * 1}{i1}{r3}{i2}{i3}{i3}{i4}', 'ошибка r2'
    if otv == 3:
        return f'{r1}{r2}{(not i1) * 1}{r3}{i2}{i3}{i3}{i4}', 'ошибка i1'
    if otv == 4:
        return f'{r1}{r2}{i1}{(not r3) * 1}{i2}{i3}{i3}{i4}', 'ошибка r3'
    if otv == 5:
        return f'{r1}{r2}{i1}{r3}{(not i2) * 1}{i3}{i3}{i4}', 'ошибка i2'
    if otv == 6:
        return f'{r1}{r2}{i1}{r3}{i2}{(not i3) * 1}{i3}{i4}', 'ошибка i3'
    if otv == 7:
        return f'{r1}{r2}{i1}{r3}{i2}{i3}{i3}{(not i4) * 1}', 'ошибка i4'



print(hamming74('0010011'))
print(hamming74('1101101'))
print(hamming74('0111000'))
print(hamming74('0011011'))

