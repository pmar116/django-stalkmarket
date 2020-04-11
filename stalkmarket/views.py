from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Stalk, Trade

class stalkmarketView(generic.ListView):
    model = Stalk
    context_object_name='stalk_list'
    ordering=['-pub_date']
    template_name='stalkmarket/stalkmarket.html'

class tradingView(generic.ListView):
    model = Trade
    context_object_name='trade_list'
    ordering=['-pub_date']
    template_name='stalkmarket/trade.html'

class poststalk(generic.CreateView):
    model=Stalk
    fields=['price', 'user','DodoCode']

class posttrade(generic.CreateView):
    model=Trade
    fields=['item', 'user', 'DodoCode']
