# Написать функцию, которая принимает
# путь к директории, путь к файлу и
# записывает в файл информацию обо всех
# файлах в директории (формат файла,
# размер, дата создания).
# Информация о файлах должна быть
# пронумерована, а каждый параметр должен
# быть помечен. Например, «1. Test;
# Расширение файла: py; Дата создания:
# 2019-12-12…» и т.д.

import os
import datetime

path = "\cpp_project"
dir_list = [os.path.join(path, x) for x in os.listdir(path)]

if dir_list:
    date_list = [[x, os.path.getctime(x)] for x in dir_list]
    
for n, item in enumerate(date_list):
	print(n, " ", item[0], "\t", datetime.datetime.fromtimestamp(item[1]).strftime("%B %d, %Y"))
    
