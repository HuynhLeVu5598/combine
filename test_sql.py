from time import sleep
import threading
import multiprocessing

import PySimpleGUI as sg

def func(queue:multiprocessing.Queue, link: str):
    for i in range(10):
        queue.put(f'Message #{i}')
        sleep(1)

def thread(window, url):
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=func, args=(queue, url), daemon=True)
    process.start()
    while process.is_alive():
        if not queue.empty():
            line = queue.get()
            window.write_event_value("Message", line)
    while not queue.empty():
        line = queue.get()
        window.write_event_value("Message", line)
    window.write_event_value("Message", 'Process has stopped')

def make_window():
    layout = [[sg.Multiline(key='-Multiline-', size=(40, 10), reroute_stdout=True)],
              [[sg.Button('Start', key='-Start-')]]]

    window = sg.Window('Forum', layout, finalize=True)

    sg.cprint_set_output_destination(window, '-Multiline-')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        elif event == '-Start-':
            sg.cprint('Process has started')
            url = 'https://stackoverflow.com/questions/ask'
            threading.Thread(target=thread, args=(window, url), daemon=True).start()
        elif event == 'Message':
            message = values[event]
            print(message)

    window.close()

if __name__ == '__main__':
    make_window()