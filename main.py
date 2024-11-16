from Model.data_parser import fill_drivers_info
from Model.driver_service import choose_driver


__URL = 'https://lonato.racemann.com/Race/id/b0c36ad5-acee-478f-a710-037b1bd6af55#race'

fill_drivers_info(race_url=__URL)
choose_driver()