from datetime import datetime
from django.test import TestCase
from .models import Movie
import time
# Create your tests here.
class MovieTest(TestCase):
    def setUp(self):
        self.movie=Movie(movieTitle='test',movieDate=datetime.date(2022,6,13),movieDescription='test',movieRating='pg')
    def test_movieString(self):
        self.assertEqual(str(self.movie),'test')  
    def test_movieDescription(self):
        self.assertEqual(self.movie.movieDescription,'test')
    def test_movieRating(self):
        self.assertEqual(self.movie.movieRating,'pg')
        