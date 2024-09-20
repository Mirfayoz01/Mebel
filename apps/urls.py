from django.urls import path
from apps.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('contact', ContactView.as_view(), name='contact'),
    path('biz_haqimizda', info, name='biz_haqimizda'),
    path('karidor', KaridorListView.as_view(), name='karidor'),
    path('ofis', OfisListView.as_view(), name='ofis'),
    path('oshxona', OshxonaListView.as_view(), name='oshxona'),
    path('shkaf', ShkafListView.as_view(), name='shkaf'),
    path('bolalar', BolalarListView.as_view(), name='bolalar'),
    path('kattalar', KattalarListView.as_view(), name='kattalar'),
    path('tv', TvListView.as_view(), name='tv'),
    path('product', product, name='product')
]