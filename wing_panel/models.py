# from django.db import models

# # Create your models here.


# class Programmes_Registration_Model(models.Model):
#     Programme_Code = models.CharField(max_length=10, unique=True)
#     Programme_Name = models.CharField(unique=True,primary_key=True)
#     Programme_Description = models.TextField()
#     Programme_Date = models.DateField()
#     Programme_Time = models.TimeField()
#     Venue = models.CharField(max_length=200)
#     Organizer_Wing = models.ForeignKey(on_delete=models.CASCADE, ) #add the wing name from wing model
#     Programme_Img = models.ImageField(upload_to='programme/', null=True, blank=True)
#     created_by = models.ForeignKey(on_delete=models.CASCADE)# who created it 

#     def __str__(self):
#         return f"{self.Programme_Code} - {self.Programme_Name}  {self.Organizer_Wing}"


# # result model for storing the results 

# # class Result_Collection_Model(models.Model):
# #     programme_name = models.ForeignKey(Programmes_Registration_Model, on_delete=models.CASCADE)
# #     results_summary = models.TextField(max_length=450)

# #     first_holder = models.CharField(max_length=100)
# #     first_grade = models.CharField(max_length=10)
# #     first_img = models.ImageField(upload_to='result_photo/', null=True, blank=True )

# #     second_holder = models.CharField(max_length=100)
# #     second_grade = models.CharField(max_length=10)
# #     second_img = models.ImageField(upload_to='result_photo/', null=True, blank=True)

# #     third_holder = models.CharField(max_length=100)
# #     third_grade = models.CharField(max_length=10)
# #     third_img = models.ImageField(upload_to='result_photo/', null=True, blank=True)

# #     Programme_Month = models.CharField(max_length=20)
# #     event_img = models.ImageField(upload_to='events/', null=True, blank=True)
# #     wing_Name = models.CharField(max_length=250)

# #     def __str__(self):
# #         return f"Result of {self.programme_name} By: {self.wing_Name}"
