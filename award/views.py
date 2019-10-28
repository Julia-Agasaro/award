from django.http  import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, PostSerializer

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

class PostList(APIView):
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers = PostSerializer(all_post, many=True)
        return Response(serializers.data)

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.objects.all()
   
    return render(request, 'home.html',{'posts':posts})

@login_required(login_url='/accounts/login/')
def editProfile(request):
    current_user=request.user
    prof = Profile.objects.filter(prof_user=current_user)
    print(prof)
    if prof:
        return redirect('profile')

    if request.method =='POST':
        form = UpdateProfileForm(request.POST,request.FILES)

        if form.is_valid():
              profile=form.save(commit=False)
              profile.prof_user=current_user
              profile.save()
        return redirect('profile')

    else:
        form=UpdateProfileForm()
    return render(request,'editProfile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def profile(request, username=None):

    current_user=request.user
    projects = Post.objects.filter(user = current_user)

    try:   
        prof = Profile.objects.get(prof_user=current_user)

    except ObjectDoesNotExist:
        return redirect('updateProfile')

  

    return render(request, 'profile.html',{"profile":prof,'projects':projects})
   


@login_required(login_url='/accounts/login/')
def post_website(request):
    current_user=request.user
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = WebsitePostForm(request.POST, request.FILES)
            # print(pf.is_valid())
            if form.is_valid():
                post=form.save(commit=False)
                post.user=current_user
                post.save()
                # return redirect(reverse('rate_website', args=(post.id,)))
        else:
            form = WebsitePostForm()

        context = {
            'form': form
        }
        return render(request, 'upload.html', context)
    return redirect('home')

@login_required(login_url='/accounts/login/')
def search(request):

    if 'project' in request.GET and request.GET ["project"]:
        search_term = request.GET.get("project")
        searched_projects = Post.search_project_by_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {"message":message, "projects":searched_projects})

    else:
        message = "No search results yet!"
        return render (request, 'search.html', {"message": message})

@login_required(login_url='/accounts/login/')
def project_review(request,project_id):
    try:
        single_project = Post.get_single_project(project_id)
        average_score = round(((single_project.design + single_project.usability + single_project.content)/3),2)
        if request.method == 'POST':
            vote_form = VoteForm(request.POST)
            if vote_form.is_valid():
                single_project.vote_submissions+=1
                if single_project.design == 0:
                    single_project.design = int(request.POST['design'])
                else:
                    single_project.design = (single_project.design + int(request.POST['design']))/2
                if single_project.usability == 0:
                    single_project.usability = int(request.POST['usability'])
                else:
                    single_project.usability = (single_project.usability + int(request.POST['usability']))/2
                if single_project.content == 0:
                    single_project.content = int(request.POST['content'])
                else:
                    single_project.content = (single_project.content + int(request.POST['usability']))/2

                single_project.save()
                return redirect('project_review',project_id)
        else:
            vote_form = VoteForm()

    except Exception as  e:
        raise Http404()
    return render(request,'project_review.html',{"vote_form":vote_form,"single_project":single_project,"average_score":average_score})