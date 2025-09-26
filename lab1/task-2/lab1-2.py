# Импортируем модуль для работы с регулярными выражениями
import re


# Читаем файл log.txt
data = open('log.txt').read()

# Находим IPv4 адреса
ipv4 = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", data)

# Находим временные метки в формате YYYY-MM-DD HH:MM:SS
time = re.findall(r"[0-9]{4}\-[0-9]{2}\-[0-9]{2}\ [0-9]{2}\:[0-9]{2}\:[0-9]{2}", data)

# Находим все слова в uppercase
uppercase_words = re.findall(r"\b[A-Z]{2,}", data)


with open('protected_log.txt', 'w', encoding="utf-8") as f:
    mails = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b", '[EMAIL PROTECTED]', data)
    f.write(mails)