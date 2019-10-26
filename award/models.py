from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    profile_photo = models.ImageField(upload_to='images/', blank=True)
    user_name = models.CharField(max_length=50, null=True)
    bio = models.TextField(blank=True)
    website = models.CharField(max_length=150, null=True)
    GENDER_CHOICES = (
        ('Male', ("Male")),
        ('Female', ("Female")),
        ('Other', ("Other")),
    )
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, blank=True)
    age = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    address = models.IntegerField(null=True)

    def save_profile(self, current_user):
        self.user = current_user
        self.save()

    def __str__(self):
       return self.bio

# class Post(models.Model):
#     uploader = models.ForeignKey(User, null=True, related_name='posts')
#     name = models.CharField(max_length=200, null=True)
#     country = models.CharField(max_length=50, null=True)
#     landing_image = models.ImageField(upload_to='site-images/', null=True)
#     screenshot_1 = models.ImageField(upload_to='site-images/', null=True)
#     screenshot_2 = models.ImageField(upload_to='site-images/', null=True)
#     screenshot_3 = models.ImageField(upload_to='site-images/', null=True)
#     screenshot_4 = models.ImageField(upload_to='site-images/', null=True)
#     screenshot_5 = models.ImageField(upload_to='site-images/', null=True)
#     screenshot_6 = models.ImageField(upload_to='site-images/', null=True)

#     description = models.TextField(blank=True)
#     site_link = models.CharField(max_length=200, null=True)
#     post_date = models.DateTimeField(auto_now_add=True)

#     @classmethod
#     def all_posts(cls):
#         all_posts = cls.objects.all()
#         return all_posts