import os
import time


def write_text_to_file(filename, ctime=None):
    with open(filename, 'a') as file:
        file.write(f'{ctime}: Hello, Docker!\n')


while True:
    time.sleep(1)
    current_time = time.strftime('%H:%M:%S', time.localtime())
    write_text_to_file('deneme.txt', ctime=time.ctime())

