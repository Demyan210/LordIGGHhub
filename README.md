Скачиваем LDPlayer. Создаём эмулятор с разрешением как на скриншоте ниже.

![image](https://github.com/user-attachments/assets/46758f54-43a7-4f19-a975-6140a063e997)

Запускаем командную строку и переходим в раздел с файлом emul.py
Используем команду: pyinstaller --onefile --noconsole --add-data "day;day" --add-data "res;res" --add-data "kod;kod" emul.py
В этом разделе создастся папка dist, в ней будет рабочая программа.
