from django.urls import path
from . import views

urlpatterns = [
    path('', views.stalkmarketView.as_view(), name='stalkmarket'),
    path('trade/', views.tradingView.as_view(), name='trade'),
    path('post/stalk', views.poststalk.as_view(), name='post-stalk'),
    path('post/trade', views.posttrade.as_view(), name='post-trade')
]