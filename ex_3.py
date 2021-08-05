#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open('text_3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя зарплата = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Сотрудники с окладом менее 20тыс {[e[0] for e in employees_dict.items() if e [1] < 20000]}')