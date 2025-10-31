from django.shortcuts import render
from .models import DIP_work

# Create your views here.

def home(request):
    dip_work = DIP_work.objects.all()
    context = {'works': dip_work}
    return render(request, 'DIP/dip_home.html', context)

def image_transformation(request):
    return render(request, 'DIP/image_transformation.html')