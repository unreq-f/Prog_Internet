import logging

logging.basicConfig(filename='user_action.log',
                    filemode='w',
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",  # Формат сообщений
                    encoding="utf-8" )

def log_action(action: str):
    logging.info(action)

def log_error(error_message):
    """Логирование ошибки пользователя."""
    logging.error(error_message)


def log_warning(warning_message):
    """Логирование предупреждений (не критических ошибок)."""
    logging.warning(warning_message)