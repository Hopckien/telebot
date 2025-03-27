import threading
import time

# import maina
from .dealapi import *

# import schedule


CNTER = 0



def run_on_time(interval=1):
    """Формирование фоновых потоков"""
    cease_continuous_run = threading.Event()
    class ZakazDeal(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    dealapi_thread = ZakazDeal()
    dealapi_thread.start()
    return cease_continuous_run


# ВОТ ДОСЮДА КОПИРУЕМ


# run_on_time()

# Do some other things...
# print('Z работаю')
