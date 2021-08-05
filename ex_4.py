#Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4.txt", 'w', encoding="utf-8") as new_file:
    with open("text_2.txt", encoding="utf-8") as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0]))for line in my_file])
