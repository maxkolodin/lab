subject1 = input("Название первого предмета: ")
count1 = int(input("Количество занятий по первому предмету за неделю: "))
dur1 = int(input("Продолжительность занятия по первому предмету (мин): "))

subject2 = input("Название второго предмета: ")
count2 = int(input("Количество занятий по второму предмету за неделю: "))
dur2 = int(input("Продолжительность занятия по второму предмету (мин): "))

hours_d = float(input("Доступное время на неделю (ч): "))

minutes1 = count1 * dur1
minutes2 = count2 * dur2
total_minutes = minutes1 + minutes2
total_hours = total_minutes / 60
free_hours = hours_d - total_hours
weeks_minutes_f = total_minutes * 4
weeks_hours_f = total_hours * 4

print()
print(f"{subject1}: {minutes1} мин")
print(f"{subject2}: {minutes2} мин")
print(f"Общая нагрузка: {total_minutes} мин = {total_hours:.2f} ч")
print(f"Остаток свободного времени: {free_hours:.2f} ч")
print(f"Нагрузка за 4 недели: {weeks_minutes_f} мин = {weeks_hours_f:.2f} ч")