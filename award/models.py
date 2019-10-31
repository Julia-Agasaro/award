from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    prof_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
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
        self.prof_user = current_user
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
       return self.bio

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=50, null=True)
    landing_image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField(blank=True)
    site_link = models.CharField(max_length=200, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    user_project_id = models.IntegerField(default=0)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        all_posts = cls.objects.all()
        return all_posts

    @classmethod
    def search_project_by_name(cls,search_term):
        project = cls.objects.filter(name__icontains=search_term)
        return project

    @classmethod
    def get_single_project(cls, project):
        project = cls.objects.get(id=project)
        return project

    class Meta:
        ordering = ['-id']