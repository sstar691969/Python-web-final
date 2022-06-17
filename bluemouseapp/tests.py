from datetime import date, time
from django.test import TestCase
from .models import Movie, Showing, Customer, Ticket
from django.urls import reverse
from django.contrib.auth.models import User

class CustomerTest(TestCase):
    def setUp(self):
        self.customer=Customer(customerName='test', customerEmail='Test@dummy.com', customerPhone=1234567890)
    def test_string(self):
        self.title= Customer(customerName='test')
    def test_tablename(self):
        self.assertEqual(str(Customer._meta.db_table), 'customer')

class TicketTest(TestCase):
    def setUp(self):
        self.ticket=Ticket(ticketPurchaseDate=date(2022, 6, 13), ticketPurchaseTime=time(10, 00), ticketPurchasePrice=12.34)
    def test_string(self):
        self.title= Ticket(ticketPurchaseDate='test')
    def test_tablename(self):
        self.assertEqual(str(Ticket._meta.db_table), 'ticket')

class ShowingTest(TestCase):
    def setUp(self):
        self.showing=Showing(showingDate=date(2022,6,13), showingTime=time(10,00))
    def test_string(self):
        self.title= Showing(showingDate='test')
    def test_tablename(self):
        self.assertEqual(str(Showing._meta.db_table), 'showing')

class MovieTest(TestCase):
    def setUp(self):
        self.movie=Movie(movieTitle='test',movieDescription='test', movieRating='pg')
    def test_movieString(self):
        self.assertEqual(str(self.movie),'test')  
    def test_movieDescription(self):
        self.assertEqual(self.movie.movieDescription,'test')
    def test_movieRating(self):
        self.assertEqual(self.movie.movieRating,'pg')
    def test_string(self):
        self.title= Movie(movieTitle='test')
    def test_tablename(self):
        self.assertEqual(str(Movie._meta.db_table), 'movie')

class New_Movie_Authentication_Test(TestCase):
    def setup(self):
        self.test_user=User.objects.create_user(username='Testuser1', password='P@assw0rd1')
        self.movie=Movie.objects.create(movieTitle='test',movieDescription='test', movieRating='pg')
        self.customer=Customer.objects.create(movieID='test',showingDate=date(2022,6,13), showingTime=time(10,00))
        self.ticket=Ticket.objects.create(ticketPurchaseDate=date(2022,6,13), ticketPurchaseTime=time(10,00), ticketPurchasePrice=12.34, showingId='test', customerid='test')
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmovie'))
        self.assertRedirects(response, '/accounts/login/?next=/bluemouseapp/newmovie/')