def add_time(start_time, duration_time, starting_day=''):
    start_format = start_time.split()
    start = start_format[0].split(':')
    duration = duration_time.split(':')
    start_hour, duration_hour = int(start[0]), int(duration[0])
    starting_minutes, duration_minutes = int(start[1]), int(duration[1])
    twelve_hour_format = ''
    if start_format[1] == 'AM':
        twelve_hour_format = 'PM'
    else:
        twelve_hour_format = 'AM'
    hours_sum = start_hour + duration_hour
    minutes_sum = starting_minutes + duration_minutes
    if minutes_sum >= 60:
        total_hour = (hours_sum % 12) + 1
    else:
        if hours_sum % 12 == 0:
            total_hour = 12
        else:
            total_hour = (hours_sum % 12)
    total_minutes = minutes_sum % 60
    if total_minutes < 10:
        total_minutes = '0' + str(total_minutes)
    day = 24 - start_hour
    hour = 12 - start_hour
    if (starting_minutes + duration_minutes) >= 60:
        dh = duration_hour + 1
    else:
        dh = duration_hour
    if start_format[1] == 'AM':
        if day <= dh <= (day + 24):
            n = 1
        elif dh >= day:
            n = int(duration_hour / 24) + 1
        else:
            n = int(duration_hour / 24)
    elif start_format[1] == 'PM':
        if dh >= hour:
            n = int(duration_hour / 24) + 1
        else:
            n = int(duration_hour / 24)
    founded_day = starting_day.capitalize()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    week = [(x, y) for x, y in enumerate(days) if founded_day in y]
    indices = week[0][0]
    new_day = days[(indices + n) % 7]
    new_format = ''
    minutes = 60 - starting_minutes
    if int(duration_hour / 12) % 2 == 0:
        if start_hour == 11:
            if hour >= (duration_hour % 12) and duration_minutes < minutes:
                new_format = start_format[1]
            else:
                new_format = twelve_hour_format
        elif hour >= (duration_hour % 12) and total_hour != 12:
            new_format = start_format[1]
        else:
            new_format = twelve_hour_format
    else:
        if start_hour == 11:
            if minutes <= duration_minutes:
                new_format = start_format[1]
            else:
                new_format = twelve_hour_format
        elif hour <= (duration_hour % 24):
            new_format = start_format[1]
        else:
            new_format = twelve_hour_format
    new_time = ''
    if n == 1:
        if starting_day != '':
            new_time = f'{total_hour}:{total_minutes} {new_format}, {new_day} (next day)'
        else:
            new_time = f'{total_hour}:{total_minutes} {new_format} (next day)'
    elif n < 1:
        if starting_day != '':
            new_time = f'{total_hour}:{total_minutes} {new_format}, {new_day}'
        else:
            new_time = f'{total_hour}:{total_minutes} {new_format}'
    elif n > 1:
        if starting_day != '':
            new_time = f'{total_hour}:{total_minutes} {new_format}, {new_day} ({n} days later)'
        else:
            new_time = f'{total_hour}:{total_minutes} {new_format} ({n} days later)'
    return new_time