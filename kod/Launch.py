import subprocess
import time

def launch():
    # Путь к исполняемому файлу LDPlayer
    package_name = "com.igg.android.hub"
    # package_name = "com.igg.android.lordsmobile"
    launch = r'"C:\\LDPlayer\\LDPlayer9\\dnplayer.exe" index=0'

    try:
        # Запуск LDPlayer в фоновом режиме
        subprocess.Popen(launch, shell=False)

        # Ожидание запуска LDPlayer перед использованием ADB
        time.sleep(10)
        print("LDPlayer запущен успешно!")
        time.sleep(10)

        # Команда для запуска IGG Hub через ADB
        adb = f'adb shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1'
        
        # Запуск ADB команды
        subprocess.run(adb, check=False, shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("IGG Hub запущен успешно через ADB!")
        time.sleep(10)
        
    except subprocess.CalledProcessError as e:
        print(f"Ошибка: {e}")