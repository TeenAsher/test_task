import os
import psutil
import time
import pydirectinput

GAME = 'WinxClub.exe'
FPS_STATISTICS = 'fraps.exe'


# Запуск игры (запуск по умолчанию от имени администратора)
def launch_game(launch_file):
    """Launching the game file"""
    launch_fps_statistics(FPS_STATISTICS)
    time.sleep(5)
    os.startfile(launch_file)


# Запуск программы для снятия статистики фпс
def launch_fps_statistics(launch_file):
    """Launching the fps statistics program"""
    os.startfile(launch_file)


# Команда запуска и остановки снятия статистики
def recording_fps():
    """Starting the fps recording"""
    pydirectinput.keyDown('f')
    pydirectinput.keyUp('f')


# Снятие скриншота
def take_screenshot():
    """Taking the screenshot (auto saving)"""
    pydirectinput.keyDown('g')
    pydirectinput.keyUp('g')


# Нажатие кнопки Enter
def tap_enter():
    """Tapping the Enter"""
    pydirectinput.press('enter')


# Нажатие кнопки Space
def tap_space():
    """Tapping the Enter"""
    pydirectinput.press('space')


# Нажатие кнопки "вниз"
def tap_down():
    pydirectinput.press('down')


# Выход из программы
def exit_program(file):
    """Exiting the running file"""
    PROCNAME = file
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()


def main(game, statistics):
    """Main script"""
    launch_game(game)
    time.sleep(30)
    tap_enter()
    time.sleep(3)
    tap_enter()
    time.sleep(1)
    tap_down()
    time.sleep(1)
    take_screenshot()
    time.sleep(1)
    recording_fps()
    time.sleep(3)
    tap_enter()
    time.sleep(3)
    tap_space()
    time.sleep(10)
    recording_fps()
    time.sleep(1)
    take_screenshot()
    time.sleep(3)
    exit_program(statistics)
    time.sleep(5)
    exit_program(game)


main(GAME, FPS_STATISTICS)
