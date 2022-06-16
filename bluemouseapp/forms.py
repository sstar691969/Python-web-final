from django import forms
from django.core.exceptions import ValidationError
from .models import Movie, Showing, Ticket, Customer

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields='__all__'

    def clean(self):
        cleaned_data=super().clean()
        showingname = cleaned_data.get("showingId")

        if Ticket.objects.filter(showingId=showingname).count()>=205:
                raise ValidationError("We're sorry, there are no more available tickets for this showing")

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class ShowingForm(forms.ModelForm):
    class Meta:
        model=Showing
        fields='__all__'