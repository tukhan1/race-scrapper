import Model.data_parser
import time

def choose_driver():
    print("""------------------------------------------------------------
Скопировать имя гонщика (как в списке выше) и вставить ниже:""")
    selected_driver = input()
    for racer in Model.data_parser.racers:
        if racer.name == selected_driver:
            print("Success")
            calculate_position_after_pitstop(
                # СЮДА ВСТАВИТЬ ВРЕМЯ ПИТСТОПА                           |
                # СЮДА ВСТАВИТЬ ВРЕМЯ ПИТСТОПА                           |
                # СЮДА ВСТАВИТЬ ВРЕМЯ ПИТСТОПА                           |
                # СЮДА ВСТАВИТЬ ВРЕМЯ ПИТСТОПА                           |
                # СЮДА ВСТАВИТЬ ВРЕМЯ ПИТСТОПА                           |
                # СЮДА ВСТАВИТЬ ВРЕМЯ ПИТСТОПА                           |
                racer, drivers=Model.data_parser.racers, pit_stop_time=32.0)
            return
    print("Error: ГОНЩИК НЕ НАЙДЕН ПРОБУЙ ЕЩЕ")
    choose_driver()
    return


def calculate_position_after_pitstop(target_driver, drivers, pit_stop_time):
    
    current_index = drivers.index(target_driver)
    
    counter = current_index
    pit_duration = pit_stop_time
    while counter < (len(drivers) - 1):
        previus_driver_interval = float(drivers[counter + 1].interval.replace("+", ""))
        print(previus_driver_interval)
        if previus_driver_interval < pit_duration:
            pit_duration -= previus_driver_interval
            counter += 1
            print("pit duration: ", pit_duration)
        else:
            interval_to_prev = previus_driver_interval - pit_duration
            interval_to_next = previus_driver_interval - interval_to_prev
            print("Интервал до машины спереди: ", round(interval_to_next, 2))
            print("Интервал до машины сзади: ", round(interval_to_prev, 2)) 
            break