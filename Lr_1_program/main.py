from menu import show_menu
from logger.loger import log_action
from email_send_module import send_log_email

if __name__ == "__main__":
    log_action("Початок роботи програми")
    show_menu()
    log_action("Завершення роботи програми")
    send_log_email()

# Это точка входа в програму