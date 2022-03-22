from django.shortcuts import render

from crm.forms import OrderForm
from crm.models import Order
from telebot.send_message import sendTelegram


def home(request):
    form = OrderForm()
    return render(request, 'landing/index.html', {'form': form})


def portfolio_details(request):
    return render(request, './portfolio-details.html')


def portfolio_details2(request):
    return render(request, './portfolio-details2.html')


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    choice = request.POST['choice']
    dictionary = {
        'name': name,
        'phone': phone,
        'choice': choice,
    }
    element = Order(order_name=name, order_phone=phone, order_choice=choice)
    element.save()
    sendTelegram(tg_name=name, tg_phone=phone, tg_choice=choice)
    return render(request, './thanks_page.html', dictionary)
