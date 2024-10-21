poem = """\
    Программировать весело.
    Если работа скучна,
    Чтобы придать ей весёлый тон -
    используй Питон ! """

f = open('App1\my_file.txt','w',encoding='utf-8')  # открываем файл для записи (writing)
f.write( poem )
f.close()

f = open('App1\my_file.txt',encoding='utf-8') # если не указан режим, по умолчанию подразумевается режим чтения( r - reading)

while True:
    line = f.readline()
    if len(line) == 0: # нелевая длина обозначает конец файла (EOF)
        break
    print(line, end=" ")

f.close()
    