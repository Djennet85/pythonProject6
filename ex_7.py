#Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

from json import dump
with open("text_7.txt", "r", encoding="utf-8") as read_file:
    with open("text_77.json", "w", encoding="utf-8") as write_file:
        dictionary = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in read_file}
        average_profit_list = []
        for n in dictionary.values():
            if n > 0:
                average_profit_list.append(n)
        dump([dictionary, {"average_profit": sum(average_profit_list) / len(average_profit_list)}],
             write_file, indent=4)
