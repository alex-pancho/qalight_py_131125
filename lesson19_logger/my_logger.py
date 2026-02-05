import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

log_level = DEBUG

# Створення логера
logger = logging.getLogger(__name__)

# Налаштування рівня логування
logger.setLevel(log_level)

# Створення обробника для виводу в stdout
console_handler = logging.StreamHandler()

# Створення обробника для запису в файл
file_handler = logging.FileHandler('example.log', encoding="utf8")

# Налаштування рівня логування для обробника
console_handler.setLevel(log_level)
file_handler.setLevel(log_level)

# Створення форматера для обробника
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s = %(filename)s - %(funcName)s: - %(lineno)d // %(name)s'
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Додавання обробника до логера
logger.addHandler(console_handler)
logger.addHandler(file_handler)


if __name__ == "__main__":
    # Логування подій
    logger.debug('Це повідомлення рівня DEBUG')
    logger.info('Це повідомлення рівня INFO')
    logger.warning('Це повідомлення рівня WARNING')
    logger.error('Це повідомлення рівня ERROR')
    logger.critical('Це повідомлення рівня CRITICAL')
