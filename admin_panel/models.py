from django.db import models
# Create your models here.
from django.contrib.auth.models import User



# student related models 

class Student_info_Model(models.Model):
    user_Stn = models.OneToOneField(User, on_delete=models.CASCADE)  # link with login user
    Student_Name = models.CharField(max_length=250, unique=True)
    Student_Add_no = models.CharField(max_length=50, unique=True)
    Student_Email = models.EmailField(unique=True, primary_key=True)
    Student_Phone = models.CharField(max_length=15)

    Student_Position = models.CharField(max_length=100)
    Student_Goal = models.CharField(max_length=250, null=True, blank=True)

    Student_Dob = models.DateField(default="2010-08-10")
    Student_Father = models.CharField(max_length=250)
    Student_Address = models.CharField(max_length=250)
    Student_Img = models.ImageField(upload_to='student/')

    def __str__(self):
        return f"{self.Student_Add_no} - {self.Student_Name}"


class Outreach_Programmes(models.Model):
    stn_Name = models.ForeignKey(Student_info_Model, on_delete=models.CASCADE)
    Programme_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    Programme_Discription = models.TextField()

    Programme_organiser = models.CharField(max_length=200, null=True, blank=True)
    hosting_place = models.CharField(max_length=200, null=True, blank=True)

    Programme_date = models.DateField()
    Programme_img = models.ImageField(upload_to='outreach/')

    def __str__(self):
        return f"{self.Programme_name} - {self.stn_Name}"


class Wings_Model(models.Model):
    wing_id = models.CharField(max_length=50, primary_key=True, unique=True)
    wing_name = models.CharField(max_length=250, unique=True)
    wing_email = models.CharField(max_length=250, unique=True)
    
    wing_manager = models.OneToOneField(
        Student_info_Model,
        on_delete=models.CASCADE,
        related_name="wing_chairPerson"
        )
    wing_assistent = models.OneToOneField(
        Student_info_Model,
        on_delete=models.CASCADE,
        related_name="wing_helper"
        )

    def __str__(self):
        return f"{self.wing_id} {self.wing_name} {self.wing_manager}"
    