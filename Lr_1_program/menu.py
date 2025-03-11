from records.storage_class import Storage
from logger.loger import log_action, log_error, log_warning

def show_menu(storage=None):

    # Создаем объект хранилища, если его нет (при первом вызове)
    if storage is None:
        storage = Storage()

    print("\nМеню:")
    print("1. Додати запис")
    print("2. Видалити запис")
    print("3. Змінити запис")
    print("4. Відобразити відомість")
    print("5. Вийти")

    choice = input("Виберіть дію: ").strip()

    if choice == "1":
        try:
            student_f = input("Введіть ПІБ студента ").strip()
            if not student_f:
                raise ValueError("Колонка ПІБ не може бути пустою.")

            missedh = int(input("Введіть кількість пропущених годин: ").strip())
            if missedh < 0:
                raise ValueError("Кількість годин не може бути від\'ємною.")

            valid_reason_h = int(input("Введіть кількість виправданих годин: ").strip())
            if valid_reason_h < 0 or valid_reason_h > missedh:
                raise ValueError("Випрадані години не можуть бути від\'ємними або більше пропущених.")

            storage.add_record(student_f, missedh, valid_reason_h)
            print("✅ Запис додано.")
            log_action(f"Додано запис: {student_f}, пропущено {missedh}, виправдано {valid_reason_h}")

        except ValueError as e:
            print(f"❌ Помилка: {e}")
            log_error(f"Помилка при додаванні запису: {e}")

        show_menu(storage)  # Рекурсивный вызов

    elif choice == "2":
        if not storage.storage_list:
            print("⚠️ Відомість пуста, видаляти нічого.")
            log_warning("Спроба видалити запис, але відомість пуста.")
        else:
            storage.display_table()
            try:
                index = int(input("Введіть номер запису для видалення: ").strip()) - 1
                removed_record = storage.storage_list[index]
                storage.remove_record(index)
                print("✅ Запис видалено")
                log_action(f"Видалено запис під номером {index}: {removed_record.student_f}, пропущено {removed_record.missedh}, виправдано {removed_record.valid_reason_h}")
            except IndexError:
                print("❌ Помилка: Введіть корректный номер запису.")
                log_error("Помилка некоректний індекс")

        show_menu(storage)  # Рекурсивный вызов


    elif choice == "3":

        if not storage.storage_list:

            print("⚠️ Ведомість пуста, змінювати нічого.")
            log_warning("Спроба змінити запис, але відомість пуста.")


        else:

            storage.display_table()

            try:

                index = int(input("Введіть номер запису для зміни: ").strip()) - 1

                if index < 0 or index >= len(storage.storage_list):
                    raise IndexError("Запису з таким номером не існує.")


                student_f = input("Введіть нові дані ПІБ студента: ").strip()

                if not student_f:
                    raise ValueError("Колонка ПІБ не може бути пустою.")

                missedh = int(input("Введіть нову кількість пропущених годин: ").strip())

                if missedh < 0:
                    raise ValueError("Кількість годин не може бути від\'ємною.")

                valid_reason_h = int(input("Введіть нову кількість виправданих годин: ").strip())

                if valid_reason_h < 0 or valid_reason_h > missedh:
                    raise ValueError("Виправдані години не можуть бути від\'ємними або більше пропущенних.")

                old_record = storage.storage_list[index]
                storage.update_record(index, student_f, missedh, valid_reason_h)
                print("✅ Запис оновлено.")
                log_action(f"Змінено запис під номером {index} : {old_record.student_f} -> {student_f}, {old_record.missedh} -> {missedh}, {old_record.valid_reason_h} -> {valid_reason_h}")


            except ValueError as e:
                print(f"❌ Помилка: {e}")
                log_error(f"Помилка при зміні запису: {e}")

            except IndexError as e:
                print(f"❌ Помилка: {e}")
                log_error(f"Помилка при зміні запису: {e}")

        show_menu(storage)  # Рекурсивный вызов

    elif choice == "4":
        if not storage.storage_list:
            print("⚠️ Відомість пуста.")
            log_warning("Спроба відобразити відомість, але вона пуста.")
        else:
            storage.display_table()
            log_action("Відображено відомість")

        show_menu(storage)  # Рекурсивный вызов

    elif choice == "5":
        print("👋 Завершення роботи")
    else:
        print("❌ Некорректний ввод, спопробуйте знову.")
        log_warning(f"Введена неіснуюча опція: {choice}")
        show_menu(storage)  # Рекурсивный вызов

