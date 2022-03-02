from django.shortcuts import render

from .forms import OrderForm


def home(request):
    form = OrderForm()
    return render(request, 'landing/index.html', {'form': form})


def detail(request):
    return render(request, 'landing/portfolio-details2.html')
