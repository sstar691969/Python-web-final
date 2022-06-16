from django.conf import settings
from math import prod
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, Customer, Showing, Ticket
from django.urls import reverse_lazy
from .forms import CustomerForm, MovieForm, ShowingForm, TicketForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
  return render(request, 'bluemouseapp/index.html')

def loginmessage(request):
    return render(request, 'bluemouseapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'bluemouseapp/logoutmessage.html')

@login_required
def newMovie(request):
  form=MovieForm

  if request.method=='POST':
    form=MovieForm(request.POST)
    if form.is_valid():
      post=form.save(commit=True)
      post.save()
      form=MovieForm()
  else:
    form=MovieForm()
  return render(request, 'bluemouseapp/newmovie.html', {'form': form})

@login_required
def newCustomer(request):
  form=CustomerForm

  if request.method=='POST':
    form=CustomerForm(request.POST)
    if form.is_valid():
      post=form.save(commit=True)
      post.save()
      form=CustomerForm()
  else:
    form=CustomerForm()
  return render(request, 'bluemouseapp/newcustomer.html', {'form': form})

@login_required
def newShowing(request):
  form=ShowingForm

  if request.method=='POST':
    form=ShowingForm(request.POST)
    if form.is_valid():
      post=form.save(commit=True)
      post.save()
      form=ShowingForm()
  else:
    form=ShowingForm()
  return render(request, 'bluemouseapp/newshowing.html', {'form': form})

@login_required
def buyTicket(request):
  form=TicketForm

  if request.method=='POST':
    form=TicketForm(request.POST)
    if form.is_valid():
      post=form.save(commit=True)
      post.save()
      form=TicketForm()
  else:
    form=TicketForm()
  return render(request, 'bluemouseapp/buyticket.html', {'form': form})