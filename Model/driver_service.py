import Model.data_parser


def choose_driver():
    print("""------------------------------------------------------------
Скопировать имя гонщика (как в списке выше) и вставить ниже:""")
    selected_driver = input()
    for racer in Model.data_parser.racers:
        if racer.name == selected_driver:
            print("Success")
            interval_to_prev, interval_to_next = calculate_intervals_after_pitstop(
                racer, drivers=Model.data_parser.racers, pit_stop_time=32.0)
            calculate_pit_stop_decision(interval_to_next, interval_to_prev)
            return
    print("Error: ГОНЩИК НЕ НАЙДЕН ПРОБУЙ ЕЩЕ")
    choose_driver()
    return

def calculate_intervals_after_pitstop(target_driver, drivers, pit_stop_time):
    current_index = drivers.index(target_driver)
    counter = current_index
    remaining_pit_time = pit_stop_time
    
    while counter < len(drivers) - 1:
        next_driver_interval = float(drivers[counter + 1].interval.lstrip("+"))
        
        if next_driver_interval < remaining_pit_time:
            remaining_pit_time -= next_driver_interval
            counter += 1
        else:
            interval_to_prev = next_driver_interval - remaining_pit_time
            interval_to_next = next_driver_interval - interval_to_prev
            return interval_to_prev, interval_to_next
        
def calculate_pit_stop_decision(interval_to_next, interval_to_prev):
    if interval_to_next > 5 and interval_to_prev > 3:
        print("\033[32mPIT STOP AVALIBLE\033[0m")
        print("Интервал до машины спереди: ", round(interval_to_next, 2))
        print("Интервал до машины сзади: ", round(interval_to_prev, 2)) 
    else:
        print("\033[31mDO NOT STOP\033[0m")
        print("Интервал до машины спереди: ", round(interval_to_next, 2))
        print("Интервал до машины сзади: ", round(interval_to_prev, 2)) 