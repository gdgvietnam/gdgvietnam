from mezzanine_events.models import EventContainer,Event
def all_events(request):
	event_container = EventContainer.objects.all()[0]
	return {'events': event_container.future_events}
