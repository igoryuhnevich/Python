# Импорт модуля App_4.py 1-ый способ   предпочтительней
""" import App_4

App_4.sayhi()
print('Version',App_4.__version__) """

# Второй способ     может быть конфликт имен
from App_4 import sayhi, __version__

sayhi()
print('Version',__version__)
