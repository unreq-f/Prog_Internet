from records.storage_class import Storage
from logger.loger import log_action, log_error, log_warning

def show_menu(storage=None):

    # Создаем объект хранилища, если его нет (при первом вызове)
    if storage is None:
        storage = Storage()

    print("\nМеню:")
    print("1. Добавить запись")
    print("2. Удалить запись")
    print("3. Изменить запись")
    print("4. Показать ведомость")
    print("5. Выйти")

    choice = input("Выберите действие: ").strip()

    if choice == "1":
        try:
            student_f = input("Введите ФИО студента: ").strip()
            if not student_f:
                raise ValueError("Колонка ФИО не может быть пустой.")

            missedh = int(input("Введите количество пропущенных часов: ").strip())
            if missedh < 0:
                raise ValueError("Количество часов не может быть отрицательным.")

            valid_reason_h = int(input("Введите количество оправданных часов: ").strip())
            if valid_reason_h < 0 or valid_reason_h > missedh:
                raise ValueError("Оправданные часы не могут быть отрицательными или больше пропущенных.")

            storage.add_record(student_f, missedh, valid_reason_h)
            print("✅ Запись добавлена.")
            log_action(f"Добавлена запись: {student_f}, пропущено {missedh}, оправдано {valid_reason_h}")

        except ValueError as e:
            print(f"❌ Ошибка: {e}")
            log_error(f"Ошибка при добавлении записи: {e}")

        show_menu(storage)  # Рекурсивный вызов

    elif choice == "2":
        if not storage.storage_list:
            print("⚠️ Ведомость пуста, удалять нечего.")
            log_warning("Попытка удалить запись, но ведомость пуста.")
        else:
            storage.display_table()
            try:
                index = int(input("Введите номер записи для удаления: ").strip()) - 1
                removed_record = storage.storage_list[index]
                storage.remove_record(index)
                print("✅ Запись удалена.")
                log_action(f"Удалена запись под номером {index}: {removed_record.student_f}, пропущено {removed_record.missedh}, оправдано {removed_record.valid_reason_h}")
            except IndexError:
                print("❌ Ошибка: Введите корректный номер записи.")
                log_error("Ошибка некорректный индекс")

        show_menu(storage)  # Рекурсивный вызов


    elif choice == "3":

        if not storage.storage_list:

            print("⚠️ Ведомость пуста, изменять нечего.")
            log_warning("Попытка изменить запись, но ведомость пуста.")


        else:

            storage.display_table()

            try:

                index = int(input("Введите номер записи для изменения: ").strip()) - 1

                if index < 0 or index >= len(storage.storage_list):
                    raise IndexError("Записи с таким номером не существует.")


                student_f = input("Введите новые данные ФИО студента: ").strip()

                if not student_f:
                    raise ValueError("Колонка ФИО не может быть пустой.")

                missedh = int(input("Введите новое количество пропущенных часов: ").strip())

                if missedh < 0:
                    raise ValueError("Количество часов не может быть отрицательным.")

                valid_reason_h = int(input("Введите новое количество оправданных часов: ").strip())

                if valid_reason_h < 0 or valid_reason_h > missedh:
                    raise ValueError("Оправданные часы не могут быть отрицательными или больше пропущенных.")

                old_record = storage.storage_list[index]
                storage.update_record(index, student_f, missedh, valid_reason_h)
                print("✅ Запись обновлена.")
                log_action(f"Изменена запись под номером {index} : {old_record.student_f} -> {student_f}, {old_record.missedh} -> {missedh}, {old_record.valid_reason_h} -> {valid_reason_h}")


            except ValueError as e:
                print(f"❌ Ошибка: {e}")
                log_error(f"Ошибка при изменении записи: {e}")

            except IndexError as e:
                print(f"❌ Ошибка: {e}")
                log_error(f"Ошибка при изменении записи: {e}")

        show_menu(storage)  # Рекурсивный вызов

    elif choice == "4":
        if not storage.storage_list:
            print("⚠️ Ведомость пуста.")
            log_warning("Попытка отобразить ведомость, но она пуста.")
        else:
            storage.display_table()
            log_action("Отображена ведомость")

        show_menu(storage)  # Рекурсивный вызов

    elif choice == "5":
        print("👋 Завершение работы.")
        log_action("Завершение работы программы")
    else:
        print("❌ Некорректный ввод, попробуйте снова.")
        log_warning(f"Введена несуществующая опция: {choice}")
        show_menu(storage)  # Рекурсивный вызов

