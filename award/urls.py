from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^editProfile',views.editProfile,name = 'updateProfile'),
    url(r'^userdetails', views.profile, name='profile'),
    url(r'^api/profile/$', views.ProfileList.as_view(),name = 'profile_api'),
    url(r'^api/project/$', views.PostList.as_view(),name = 'project_api'),
    url(r'^new/post/$', views.post_website, name='post_website'),
    url(r'^search', views.search, name='search'),
    url(r'^project/review/',views.project_review,name='project_review'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)