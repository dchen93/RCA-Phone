from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from rest_framework import viewsets

from location.models import Phone, Center
from location.serializers import PhoneSerializer, CenterSerializer

class DetailView(generic.DetailView):
	model = Phone
	template_name = 'location/detail.html'


class ResultsView(generic.DetailView):
	model = Phone
	template_name = 'location/results.html'


def update(request, phone_id):
	p = get_object_or_404(Phone, pk = phone_id)
	try:
		selected_center = p.center_set.get(pk=request.POST['center'])
	except (KeyError, Center.DoesNotExist):
		return render(request, 'location/detail.html', {
			'phone': p,
			'error_message': "You didn't select a center.",
			})
	else:
		selected_center.current_location = True
		selected_center.save()
		p.updated_time = timezone.now()
		p.save()
		for center in p.center_set.all():
			if center != selected_center:
				center.current_location = False
				center.save()
		return HttpResponseRedirect(reverse('location:results', args=(p.id,)))


class PhoneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows phones to be viewed or edited. To reach phone instances, /api/phones/{pk}
    """
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class CenterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows phones to be viewed or edited. To reach phone instances, /api/phones/{pk}
    """
    queryset = Center.objects.all()
    serializer_class = CenterSerializer