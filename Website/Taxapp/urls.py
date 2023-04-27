from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='indx'),
    path('<int:number>',views.newPrice,name='newP'),
    path("taxrate",views.taxrate,name="taxR")
]

