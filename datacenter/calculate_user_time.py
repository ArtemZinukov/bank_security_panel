from django.utils.timezone import localtime


def get_duration(visit):
    if not visit.leaved_at:
        visit_time = localtime() - visit.entered_at
    else:
        entered = visit.entered_at
        leave = visit.leaved_at
        visit_time = leave - entered
    return visit_time.total_seconds()


def format_duration(duration):
    hour = duration // 3600
    minute = (duration % 3600) // 60
    second = (duration % 3600) % 60
    return f'{int(hour)}:{int(minute)}:{int(second)}'


def is_visit_long(visit_time):
    if not visit_time >= 3600:
        return 'Нет'
    return 'Да'
