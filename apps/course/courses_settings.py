""""Settings"""

days_of_week = [
        ('Monday', 'Lunes'),
        ('Tuesday', 'Martes'),
        ('Wednesday', 'Miércoles'),
        ('Thursday', 'Jueves'),
        ('Friday', 'Viernes'),
    ]

min_hour = 9
max_hour = 19

levels = [
        ('begginer', 'Begginer'),
        ('pre_intermediate', 'Pre_Intermediate'),
        ('intermediate', 'Intermediate'),
        ('upper_intermediate', 'Upper-intermediate'),
        ('advanced', 'Advanced'),
    ]

modalities =  [
        ('individual', 'Individual'),
        ('grupal', 'Grupal'),
    ]

group_capacity = 6
tolerance = 1


def journey():
    # List the journey from min_hour to max_hour
    HS_OF_DAY = [(f'{x}', f'{x}.00') for x in range(min_hour,max_hour+1)]
    return HS_OF_DAY
