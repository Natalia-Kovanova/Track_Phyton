disk_mb = 1.44               # объём дискеты в Мб
pages = 100                  # страниц в книге
lines_per_page = 50          # строк на странице
chars_per_line = 25          # символов в строке
bytes_per_char = 4           # байт на символ

# объём дискеты в байты
disk_bytes = disk_mb * 1024 ** 2

# сколько символов в книге
chars_in_book = pages * lines_per_page * chars_per_line

# объём одной книги в байтах
book_bytes = chars_in_book * bytes_per_char

# сколько книг поместится на дискету (целое число)
books_count = int(disk_bytes // book_bytes)

print("Количество книг, помещающихся на дискету:",books_count)
