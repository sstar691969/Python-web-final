from django import forms
from .models import Movie, Ticket, Customer

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields='__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class ShowingForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'