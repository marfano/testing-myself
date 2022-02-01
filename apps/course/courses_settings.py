""""Settings"""

days_of_week = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
    ]

min_hour = 9
max_hour = 19

levels = [
        ('Begginer', 'Begginer'),
        ('Pre-Intermediate', 'Pre-Intermediate'),
        ('Intermediate', 'Intermediate'),
        ('Upper-Intermediate', 'Upper-Intermediate'),
        ('Advanced', 'Advanced'),
    ]

modalities =  [
        ('Individual', 'Individual'),
        ('Grupal', 'Grupal'),
    ]

group_capacity = 6
tolerance = 1


def journey():
    # List the journey from min_hour to max_hour
    HS_OF_DAY = [(f'{x}', f'{x}.00') for x in range(min_hour,max_hour+1)]
    return HS_OF_DAY
