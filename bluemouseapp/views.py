from django.shortcuts import render, get_object_or_404
from .models import Movie, Customer, Showing, Ticket
from django.urls import reverse_lazy
from .forms import MovieForm

# Create your views here.
def index(request):
  return render(request, 'bluemouseapp/index.html')

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