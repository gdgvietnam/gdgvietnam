from mezzanine_events.models import EventContainer


def all_events(request):
    event_container = EventContainer.objects.all()[0]
    return {
        'events': {'ongoing_events': event_container.ongoing_events(),
                   'future_events': event_container.future_events(),
                   'lastest_events': event_container.past_events()[:3], }}
