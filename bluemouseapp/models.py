

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movieTitle=models.CharField(max_length=255)
    movieDate=models.DateField()
    movieTime=models.DateTimeField()
    movieDescription=models.TextField()
    movieRating=models.CharField(max_length=225)


    def __str__(self):
        return self.movieTitle


    class Meta:
        db_table='movie'


class Showing(models.Model):
    movieId=models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    showingTime=models.DateTimeField()
    showingDate=models.DateField()

    def __str__(self):
        return str(self.movieId)


    class Meta:
        db_table='showing'

#--The two class above should be correct but please update if incorrected--#


class Customer(models.Model):
    customereName=models.CharField(max_length=255)
    customerEmail=models.EmailField(max_length=255,unique=True)
    customerPhone=models.IntegerField()
    

    def __str__(self):
        return self.customereName


    class Meta:
        db_table='customer'



class Ticket(models.Model):
    ticketPurchaseDate=models.DateField()
    ticketPurchaseTime=models.DateTimeField()
    ticketPurchasePrice=models.DecimalField(max_digits=19, decimal_places=2)
    showingId=models.ForeignKey(Showing, on_delete=models.DO_NOTHING)
    customerId=models.ForeignKey(Customer, on_delete=models.DO_NOTHING)   


    def __str__(self):
        return self.ticketPurchaseDate


    class Meta:
        db_table='ticket'



    
    
#-- Models Customers and Tickets attributes are not complete 

        
    
# Create your models here.
