from django.urls import path
from . import views


urlpatterns = [
   path('',views.index, name='index'),
   path('newmovie/', views.newMovie, name='newmovie'),
   path('newcustomer/', views.newCustomer, name='newcustomer'),
   path('newshowing/', views.newShowing, name='newshowing'),
   path('buyticket/', views.buyTicket, name='buyticket'),
   path('loginmessage/', views.loginmessage, name='loginmessage'),
   path('logoutmessage/', views.logoutmessage, name='logoutmessage')
]
