from django.shortcuts import render
from .models import Viz


def index(request):
    info = Viz.objects.order_by('-id')
    return render(request, 'vizitka/index.html', {'info':info})
