# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("text_2.txt", 'r', encoding="utf-8") as f_obj:
    useful = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов'
              for line, count in enumerate(f_obj, 1)]
    print(*useful, f"Всего строк - {len(useful)}.", sep="\n")









