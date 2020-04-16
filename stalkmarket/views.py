from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import Q
from .models import Stalk, Trade
import datetime
from . import helper

class stalkmarketView(generic.ListView):
    template_name='stalkmarket/stalkmarket.html'

    def get(self, request, *args, **kwargs):
        recent = Stalk.objects.filter(Q(morning=helper.ismorning()) & Q(pub_date=datetime.date.today()))
        context = {
            'stalk_list' : recent
        }
        return render(request, 'stalkmarket/stalkmarket.html', context)
    

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
