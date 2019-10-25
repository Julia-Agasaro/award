from django.http  import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')