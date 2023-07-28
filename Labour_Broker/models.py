from django.db import models
from django.contrib.auth.models import User
type_choices = [
    
    ('', 'Select worker type'),
    ('Agriculture', 'Agriculture'),
    ('Construction', 'Construction'),
    ('Houseworks','Houseworks'),
    ('Textile','textile'),
    ('Machinary','machinary'),
]
class Labour_data(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=100, choices=type_choices,null=True,blank=True)
    other_type=models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100)
    no_of_w = models.IntegerField()
    salary = models.IntegerField()
    location = models.CharField(max_length=100)
    contact=models.IntegerField(default=0000)
    other_details=models.TextField(null=True,blank=True)
    
class Labour_type(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  
    reg_type=models.CharField(max_length=30)
    