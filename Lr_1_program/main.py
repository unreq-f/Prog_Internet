from menu import show_menu   # Импортируем функцию show_menu
from logger.loger import log_action
from email_send_module import send_log_email

if __name__ == "__main__":
    log_action("Начало работы программы")
    show_menu()
    log_action("Завершение работы программы")
    send_log_email()

# Это точка входа в програму