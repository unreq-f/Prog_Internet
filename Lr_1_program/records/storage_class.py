from records.record_class import Record

class Storage:
    def __init__(self):
        self.storage_list = []

    def add_record(self, student_f: str,  missedh :int = 0, valid_reason_h: int = 0 ):
        record = Record(student_f, missedh, valid_reason_h)
        self.storage_list.append(record)

    def remove_record(self, index: int):
        if 0 <= index < len(self.storage_list):
            del self.storage_list[index]
        else:
            print("Помилка: Індекс поза діапазоном")


    def update_record(self, index: int, student_f: str, missedh: int = 0, valid_reason_h: int = 0):
        if 0 <= index < len(self.storage_list):
            self.storage_list[index] = Record(student_f, missedh, valid_reason_h)
        else:
            print("Помилка: Індекс поза діапазоном")

    def display_table(self):
        """Выводит ведомость посещаемости в табличном формате."""
        max_index_len = len(str(len(self.storage_list)))  # Длина номера записи
        max_name_len = max(len(record.student_f) for record in self.storage_list)
        max_missed_len = max(len(str(record.missedh)) for record in self.storage_list)
        max_valid_len = max(len(str(record.valid_reason_h)) for record in self.storage_list)
        max_count_len = max(len(str(record.count)) for record in self.storage_list)
        max_percent_len = max(len(f"{record.percentage:.2f}%") for record in self.storage_list)

        missed_hours_width = len(f'{'Всього':^{max_missed_len}} | {'Виправдано':^{max_valid_len}}')
        absences_width = len(f'{'У годинах':^{max_count_len}} | {'У %':^{max_percent_len}}')

        print("Відомість відвідування занять студентами:")

        header_1 = (
            f"| {'№':<{max_index_len}} | {'Прізвище':<{max_name_len}} | "
            f"{'Пропущено годин':^{missed_hours_width}} | {'Пропуски':^{absences_width}}  |"
        )
        header_2 = (
            f"|{'':<{max_index_len}} |{'':<{max(max_name_len, 9)}}  | "
            f"{'Всього':^{max_missed_len}} | {'Виправдано':^{max_valid_len}} | "
            f"{'У годинах':^{max_count_len}} | {'У %':^{max_percent_len}}  |"
        )

        print("-" * len(header_1))
        print(header_1)
        print(header_2)
        print("-" * len(header_1))

        # Данные
        for i, record in enumerate(self.storage_list, start=1):
            print(
                f"| {i:<{max_index_len}} | {record.student_f:<{max(8, max_name_len)}} | "
                f"{record.missedh:^{max(6, max_missed_len)}} | "
                f"{record.valid_reason_h:^{max(10, max_valid_len)}} | "
                f"{record.count:^{max(9, max_count_len)}} | "
                f"{record.percentage:^{max_percent_len}.2f}% |"
            )

        print("-" * len(header_1))


