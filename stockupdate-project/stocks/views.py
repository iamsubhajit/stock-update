from django.shortcuts import render, get_object_or_404
#from .models import 

# Create your views here.
def homepage(request):
    return render(request, 'stocks/home.html')
