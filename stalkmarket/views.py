from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import Q
from .models import Stalk, Trade
import datetime
from . import helper

class stalkmarketView(generic.ListView):
    template_name='stalkmarket/stalkmarket.html'
    context_object_name = 'stalk_list'

    def get_queryset(self):
        recent = Stalk.objects.filter(Q(morning=helper.ismorning()) & Q(pub_date=datetime.date.today()))
        return recent
    

class tradingView(generic.ListView):
    context_object_name='trade_list'
    template_name='stalkmarket/trade.html'

    def get_queryset(self):
        recent = Trade.objects.order_by('-pub_time')[:20]
        return recent

class poststalk(generic.CreateView):
    model=Stalk
    fields=['price', 'user','DodoCode']

class posttrade(generic.CreateView):
    model=Trade
    fields=['item', 'user', 'DodoCode']
