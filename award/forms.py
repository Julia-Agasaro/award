from django import forms
# fill in custom user info then save it
from django.contrib.auth.models import User
from .models import *


class UpdateProfileForm(forms.ModelForm):
    class Meta:
       model=Profile
       fields=['bio','profile_photo','email']
       exclude=['user']

class WebsitePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'landing_image',
                  'screenshot_1', 'screenshot_2','description', 'site_link', 'country')