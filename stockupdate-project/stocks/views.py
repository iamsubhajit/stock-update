from django.shortcuts import render, get_object_or_404
from .models import Stock

# Create your views here.
def homepage(request):
    stocks = Stock.objects
    return render(request, 'stocks/home.html', {'stocks':stocks})

def stockdetail(request, stock_id):
    stock_detail = get_object_or_404(Stock, pk=stock_id)
    return render(request, 'stocks/stockdetail.html', {'stock':stock_detail})
