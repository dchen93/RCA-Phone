from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def home(request):
	return HttpResponseRedirect(reverse('location:results', args=(1,))) # for RCA Phone (pk=1)