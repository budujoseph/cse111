
# Computing volume of a tire


import math

from datetime import datetime

width = float(input('Enter the width of the tire in mm: '))
ratio = float(input('Enter the ratio of the tire: '))
diameter = float(input('Enter the diameter of the wheel in inches: '))


formular1 = (math.pi*width**2)*ratio
formular2 = (width * ratio) + 2540*diameter

tire_volume = (formular1 * formular2) / 10000000000


current_date = datetime.now()

with open ('volume.txt', 'at') as volume_file:
    print(f'{current_date: %Y-%m-%d}, {width}, {ratio}, {diameter}, {tire_volume:.2f}' , file = volume_file)
    

