"""
    Dear bug-maker:

    This settings are here to models use.
    This don't work on templates or views.
    This configuration is easily modificable
    and can support a large variety of uses
    or transformations on another data types.

    You can feel free to explore the options,
    but keep this out of the line of bugs-fire.
    You need this to register students and teachers.

    With love,
    -Martina
"""

""""Settings"""

# days to teachers work
days_of_week = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
    ]

# min and max hour to teachers work
min_hour = 9
max_hour = 19

# levels to students choice
levels = [
        ('Begginer', 'Begginer'),
        ('Pre-Intermediate', 'Pre-Intermediate'),
        ('Intermediate', 'Intermediate'),
        ('Upper-Intermediate', 'Upper-Intermediate'),
        ('Advanced', 'Advanced'),
    ]

# modalities to students choice
modalities =  [
        ('Individual', 'Individual'),
        ('Grupal', 'Grupal'),
    ]

# Journey calculator
def journey():
    # List the journey from min_hour to max_hour
    HS_OF_DAY = [(f'{x}', f'{x}.00') for x in range(min_hour,max_hour+1)]
    return HS_OF_DAY
