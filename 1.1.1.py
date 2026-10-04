surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст (полных лет): "))
subject = input("Любимый предмет: ")
hours = float(input("Часов подготовки в неделю: "))

fullname = name + " " + surname
age_4 = age + 4
hoursw = hours * 4
avg_day = hours / 7

print()
print("Карточка студента")
print("Фамилия:", surname)
print("Имя:", name)
print("Группа:", group)
print("Город:", city)
print("Возраст:", age)
print("Любимый предмет:", subject)
print("Часов подготовки в неделю:", f"{hours:.2f}")
print("Полное имя:", fullname)
print("Возраст через 4 года:", age_4)
print("Подготовка за 4 недели:", f"{hoursw:.2f}")
print("Среднее в день:", f"{avg_day:.2f}")