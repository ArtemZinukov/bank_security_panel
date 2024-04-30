from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.calculate_user_time import format_duration
from datacenter.calculate_user_time import get_duration
from datacenter.calculate_user_time import is_visit_long
from django.shortcuts import render
import django


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(get_duration(visit)),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
