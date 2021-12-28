from django.urls import path

from . import views

app_name = 'resultparser'

urlpatterns = [
    path('',views.index,name='index'),
    path('record',views.record,name='record'),
    path('search',views.search,name='search'),
    path('reasult',views.result,name='result'),
]
