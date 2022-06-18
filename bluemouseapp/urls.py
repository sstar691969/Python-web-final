from django.urls import path
from . import views


urlpatterns = [
   path('',views.index, name='index'),
   path('movies/', views.movies, name='movies'),
   path('moviedetail/<int:id>', views.moviedetail, name='moviedetail'),
   path('showings/', views.showings, name='showings'),
   path('showingdetail/<int:id>', views.showingdetail, name='showingdetail'),
   path('customers/', views.customers, name='customers'),
   path('customerdetail/<int:id>', views.customerdetail, name='customerdetail'),
   path('newmovie/', views.newMovie, name='newmovie'),
   path('newcustomer/', views.newCustomer, name='newcustomer'),
   path('newshowing/', views.newShowing, name='newshowing'),
   path('buyticket/', views.buyTicket, name='buyticket'),
   path('loginmessage/', views.loginmessage, name='loginmessage'),
   path('logoutmessage/', views.logoutmessage, name='logoutmessage')
]
