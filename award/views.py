from django.http  import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Profile
from .serializer import ProfileSerializer

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html')


@login_required(login_url='/accounts/login/')
def profile(request, username=None):
   '''
   Method that fetches a users profile page
   '''
   current_user=request.user
   profile= Profile.objects.get(user=current_user)
   # images = Image.objects.filter(profile = profile_id)
   # title = User.objects.get(pk = profile_id).username
#    profile = Profile.objects.filter(user = current_user).all()
   print(f'profile {profile.bio}')
   return render(request, 'profile.html',{"profile":profile})
   
@login_required(login_url='/accounts/login/')
def editProfile(request):
    current_user=request.user
    if request.method =='POST':
        form = UpdateProfileForm(request.POST,request.FILES)

        if form.is_valid():
              profile=form.save(commit=False)
              profile.user=current_user
              profile.save()
        return redirect('profile')

    else:
        form=UpdateProfileForm()
    return render(request,'editProfile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def post_website(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = WebsitePostForm(request.POST, request.FILES)
            # print(pf.is_valid())
            if form.is_valid():
                form.save()
                post = Post.objects.last()
                post.save_post(user)
                # return redirect(reverse('rate_website', args=(post.id,)))
        else:
            form = WebsitePostForm()

        context = {
            'form': form
        }
        return render(request, 'upload.html', context)
    return redirect('home')