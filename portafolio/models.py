from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image= models.ImageField(upload_to="portafolio/images")
    url= models.URLField(blank=True)

class Profiles(models.Model):
    name = models.CharField(max_length=50) # example : Julian
    title = models.CharField(max_length=50) # example : Django Developer 
    description = models.CharField(max_length=500) # example : I am someone who loves python--
    image= models.ImageField(upload_to="portafolio/images") # example : photo of you
    linkedin = models.CharField(max_length=50) #link
    github = models.CharField(max_length=50) #link

class Skills(models.Model): 
    name = models.CharField(max_length=50) # example : Docker
    image= models.ImageField(upload_to="portafolio/images") # example : icon of python
    



