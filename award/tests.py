from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
class TestProfile(TestCase):
   def setUp(self):
       self.prof_user = User(username='Bideli')
       self.prof_user.save()
       self.profile_test = Profile( profile_photo=' media/sweet-food-chocolate-wallpaper-e45943b31955e9eb66381700fb22297d_hTxbvq4.jpg', bio='this is a test ', prof_user=self.prof_user)
   def test_instance(self):
       self.assertTrue(isinstance(self.profile_test, Profile))
   def test_save_profile(self):
       self.profile_test.save_profile()
       travel = Profile.objects.all()
   def tearDown(self):
       '''
       Test delete category behaivour
       '''
       Profile.objects.all().delete()
   def test_delete_profile(self):
       '''
       Test if category can be deleted from db.
       '''
       self.profile_test.save_profile()
       self.profile = Profile.objects.get(id = 1)
       self.assertFalse(len(Profile.objects.all()) == 0)

class PostTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_profile = Profile(id=1,prof_user=self.new_user,bio='yolo',contact_info='kezajo@gmail.com',profile_Id=1)
        self.new_profile.save_profile()
        self.new_project = Project(id=1,title='title',details='details',link='www.link.com',user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Post))

    def test_save_instance(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_project(self):
        self.new_project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

    def test_fetch_projects(self):
        self.new_project.save_project()
        projects = Project.fetch_all_images()
        self.assertTrue(len(projects)>0)

    def test_find_project(self):
        self.new_project.save_project()
        project = Project.get_single_project(self.new_project.id)
        self.assertTrue(project == self.new_project)