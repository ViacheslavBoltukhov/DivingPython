'''
Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
WARNING и выше — в warnings_errors.log.
'''

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s -%(message)s')

debug_info = logging.FileHandler('debug_info.log')
debug_info.setLevel(logging.DEBUG)
debug_info.setFormatter(formatter)
logger.addHandler(debug_info)

warnings_errors = logging.FileHandler('warnings_errors.log')
warnings_errors.setLevel(logging.WARNING)
warnings_errors.setFormatter(formatter)
logger.addHandler(warnings_errors)

logger.debug('Level message DEBUG.')
logger.info('Level message INFO.')
logger.warning('Level message WARNING.')
logger.error('Level message ERROR.')
logger.critical('Level message CRITICAL.')
