#!/usr/bin/env python3

import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin", 
        password="P@sswOrd1",  
        database="Human_friends"  
    )

    my_cursor = mydb.cursor()

    # --- Создание таблиц ---
    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS Животные (
            id INT AUTO_INCREMENT PRIMARY KEY,
            тип VARCHAR(255) NOT NULL
        )
    """)

    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pets (
            pet_id INT AUTO_INCREMENT PRIMARY KEY,
            животное_id INT,
            имя VARCHAR(255),
            вид VARCHAR(255),
            датаРождения DATE,
            FOREIGN KEY (животное_id) REFERENCES Животные(id)
        )
    """)

    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pack_animals (
            pack_animal_id INT AUTO_INCREMENT PRIMARY KEY,
            животное_id INT,
            имя VARCHAR(255),
            вид VARCHAR(255),
            датаРождения DATE,
            FOREIGN KEY (животное_id) REFERENCES Животные(id)
        )
    """)

    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS Собаки (
            собака_id INT AUTO_INCREMENT PRIMARY KEY,
            pet_id INT,
            порода VARCHAR(255),
            цвет VARCHAR(255),
            FOREIGN KEY (pet_id) REFERENCES Pets(id)
        )
    """)

    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS Кошки (
            кошка_id INT AUTO_INCREMENT PRIMARY KEY,
            pet_id INT,
            порода VARCHAR(255),
            цвет VARCHAR(255),
            FOREIGN KEY (pet_id) REFERENCES Pets(id)
        )
    """)

    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS Хомяки (
            хомяк_id INT AUTO_INCREMENT PRIMARY KEY,
            pet_id INT,
            порода VARCHAR(255),
            цвет VARCHAR(255),
            FOREIGN KEY (pet_id) REFERENCES Pets(id)
        )
    """)

    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS Лошади (
            лошадь_id INT AUTO_INCREMENT PRIMARY KEY,
            pack_animal_id INT,
            скорость INT,
            выносливость VARCHAR(255),
            FOREIGN KEY (pack_animal_id) REFERENCES Pack_animals(id)
        )
    """)

    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS Верблюды (
            верблюд_id INT AUTO_INCREMENT PRIMARY KEY,
            pack_animal_id INT,
            скорость INT,
            выносливость VARCHAR(255),
            FOREIGN KEY (pack_animal_id) REFERENCES Pack_animals(id)
        )
    """)

    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ослы (
            осел_id INT AUTO_INCREMENT PRIMARY KEY,
            pack_animal_id INT,
            скорость INT,
            выносливость VARCHAR(255),
            FOREIGN KEY (pack_animal_id) REFERENCES Pack_animals(id)
        )
    """)



    animals_data = [
      ('Домашние',),
      ('Дикие',),
      ('Сельскохозяйственные',),
      ('Экзотические',),
    ]
    my_cursor.executemany("INSERT INTO Животные (тип) VALUES (%s)", animals_data)
    
    # Получение id животных для связи
    my_cursor.execute("SELECT id FROM Животные")
    animal_ids = [row[0] for row in my_cursor.fetchall()]
    
    # Данные для таблицы Pets
    pets_data = [
        (animal_ids[0], 'Шарик', 'Собака', '2022-05-10'),
        (animal_ids[0], 'Мурка', 'Кошка', '2021-08-15'),
        (animal_ids[0], 'Крош', 'Хомяк', '2023-01-01'),
    ]
    
    my_cursor.executemany("INSERT INTO Pets (животное_id, имя, вид, датаРождения) VALUES (%s, %s, %s, %s)", pets_data)
    
    # Получаем id из таблицы Pets для связи со служебными животными
    my_cursor.execute("SELECT pet_id FROM Pets")
    pet_ids = [row[0] for row in my_cursor.fetchall()]
    
    # Данные для таблицы Собаки
    dogs_data = [
        (pet_ids[0], 'Немецкая овчарка', 'Черный'),
        (pet_ids[0], 'Лабрадор', 'Желтый'),
    ]
    
    my_cursor.executemany("INSERT INTO Собаки (pet_id, порода, цвет) VALUES (%s, %s, %s)", dogs_data)
    
    # Данные для таблицы Кошки
    cats_data = [
        (pet_ids[1], 'Сиамская', 'Кремовая'),
        (pet_ids[1], 'Бенгальская', 'Рыжая'),
    ]
    
    my_cursor.executemany("INSERT INTO Кошки (pet_id, порода, цвет) VALUES (%s, %s, %s)", cats_data)
    
    # Данные для таблицы Хомяки
    hamsters_data = [
        (pet_ids[2], 'Золотой', 'Золотистый'),
        (pet_ids[2], 'Серый', 'Серый'),
    ]
    
    my_cursor.executemany("INSERT INTO Хомяки (pet_id, порода, цвет) VALUES (%s, %s, %s)", hamsters_data)
    
    # Данные для таблицы Pack_animals
    pack_animals_data = [
        (animal_ids[2], 'Бурый', 'Лошадь', '2020-06-06'),
        (animal_ids[2], 'Мустанг', 'Лошадь', '2019-09-15'),
    ]
    
    my_cursor.executemany("INSERT INTO Pack_animals (животное_id, имя, вид, датаРождения) VALUES (%s, %s, %s, %s)", pack_animals_data)
    
    # Получаем id для связи с Лошадьми
    my_cursor.execute("SELECT pack_animal_id FROM Pack_animals")
    pack_animal_ids = [row[0] for row in my_cursor.fetchall()]
    
    # Данные для таблицы Лошади
    horses_data = [
        (pack_animal_ids[0], 60, 'Высокая'),
        (pack_animal_ids[1], 70, 'Средняя'),
    ]
    
    my_cursor.executemany("INSERT INTO Лошади (pack_animal_id, скорость, выносливость) VALUES (%s, %s, %s)", horses_data)
    
    # Данные для таблицы Верблюды
    
    camels_data = [
        (pack_animal_ids[0], 20, 'Высокая'),
    ]
    
    my_cursor.executemany("INSERT INTO Верблюды (pack_animal_id, скорость, выносливость) VALUES (%s, %s, %s)", camels_data)
    
    # Данные для таблицы Ослы
    donkeys_data = [
        (pack_animal_ids[1], 10, 'Средняя'),
    ]
    
    my_cursor.executemany("INSERT INTO Ослы (pack_animal_id, скорость, выносливость) VALUES (%s, %s, %s)", donkeys_data)
    
    
    
    my_cursor.execute("DELETE FROM Верблюды WHERE pack_animal_id IN (SELECT pack_animal_id FROM Pack_animals WHERE вид = 'Верблюд')")
    
    # --- Объединение лошадей и ослов ---
    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS ЛошадиОслы AS
        SELECT pa.животное_id, ж.тип, ж.имя, ж.вид, ж.датаРождения, pa.скорость, pa.выносливость
        FROM Pack_animals pa
        JOIN Животные ж ON pa.животное_id = ж.id
        WHERE ж.тип IN ('Лошадь', 'Осел')
    """)
    
    # --- Создание таблицы Animals_1_3 ---
    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS Animals_1_3 AS
        SELECT ж.*, TIMESTAMPDIFF(MONTH, p.датаРождения, CURDATE()) AS возраст_месяцев
        FROM Животные ж
        JOIN Pets p ON ж.id = p.животное_id
        WHERE TIMESTAMPDIFF(MONTH, p.датаРождения, CURDATE()) BETWEEN 12 AND 36
    """)
    
    # --- Объединение всех таблиц ---
    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS All_animals AS
        SELECT
            ж.id AS животное_id,
            ж.тип,
            p.имя,
            п.вид,
            п.датаРождения,
            c.порода AS порода_домашнего_животного,
            c.цвет AS цвет_домашнего_животного,
            pa.скорость,
            pa.выносливость
        FROM Животные ж
        LEFT JOIN Pets p ON ж.id = p.животное_id
        LEFT JOIN Собаки c ON p.pet_id = c.pet_id
        LEFT JOIN Pack_animals pa ON ж.id = pa.животное_id
    """)
    
    mydb.commit()

except mysql.connector.Error as err:
    print(f"Ошибка: {err}")

finally:
    if mydb.is_connected():
        my_cursor.close()
        mydb.close()
