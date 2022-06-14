from django.shortcuts import render
from django.conf import settings

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
  return render(request, 'bluemouseapp/index.html')



def loginmessage(request):
    return render(request, 'bluemouseapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'bluemouseapp/logoutmessage.html')