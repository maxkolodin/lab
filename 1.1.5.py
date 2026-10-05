oname = input("Название заказа: ")
cname = input("Имя заказчика: ")
item1 = input("Название первой позиции: ")
item1k = int(input("Количество первой позиции: "))
item1p = float(input("Цена первой позиции: "))
item2 = input("Название второй позиции: ")
item2k = int(input("Количество второй позиции: "))
item2p = float(input("Цена второй позиции: "))
delivery = float(input("Стоимость доставки: "))
paid = float(input("Внесённая сумма: "))
item1_total = item1k * item1p
item2_total = item2k * item2p
goods_total = item1_total + item2_total
total = goods_total + delivery
total_units = item1k + item2k
change = paid - total
print()
print("Заказ:", oname)
print("Заказчик:", cname)
print(f"Название:{item1} , Количество:{item1k} , Цена:{item1p:.2f} , Стоимость:{item1_total:.2f}")
print(f"Название:{item2} , Количество:{item2k} , Цена:{item2p:.2f} , Стоимость:{item2_total:.2f}")
print(f"Стоимость товаров без доставки: {goods_total:.2f}")
print(f"Стоимость доставки: {delivery:.2f}")
print(f"Общая сумма с доставкой: {total:.2f}")
print(f"Общее количество единиц: {total_units}")
print(f"Сдача: {change:.2f}")
