from django.db import models

# Create your models here.


class Wings_Model(models.Model):
    wing_id = models.CharField(max_length=50, primary_key=True, unique=True)
    wing_name = models.CharField(max_length=250, unique=True)
    wing_chairPerson = models.CharField(max_length=250, unique=True)
    wing_helper = models.CharField(max_length=205, unique=True)
