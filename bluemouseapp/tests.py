from datetime import datetime
from django.test import TestCase
from .models import Movie, Showing, Customer, Ticket
import time
# Create your tests here.
class MovieTest(TestCase):
    def setUp(self):
        self.movie=Movie(movieTitle='test',movieDescription='test',movieRating='pg')
    def test_movieString(self):
        self.assertEqual(str(self.movie),'test')  
    def test_movieDescription(self):
        self.assertEqual(self.movie.movieDescription,'test')
    def test_movieRating(self):
        self.assertEqual(self.movie.movieRating,'pg')

class CustomerTest(TestCase):
    def test_string(self):
        self.title= Customer(customerName='test')
    def test_tablename(self):
        self.assertEqual(str(Customer._meta.db_table), 'test')


        