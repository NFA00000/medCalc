def calculation():
    # Ввод данных
    try:
        dose = float(input("Введите дозу препарата в мкг/кг/ч "))
        weight = float(input("Введите массу тела пациента "))
        time = float(input("Введите время длительности инфузии "))
        medic = float(input("Введите концентрацию маточного раствора в мкг "))
    except Exception:
        calculation()
    # volume = float(input("Введите объем шприца "))
    # rate = float(input("Введите скорость введения готового раствора в мл/ч "))
    # Вычисление
    variable = dose * weight * time / 1000
    result = variable/medic
    # constant = 60
    # first_part = dose * weight * volume * constant
    # second_part = rate * medication
    # result = first_part / second_part
    # Результат
    print("Итоговый объем препарата", round(result, 2), "мл")
while True:
    flag = input("Новый рассчет? ")

    if flag == "да" or "Да":
        calculation()
    else:
        break