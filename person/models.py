from django.db import models
from area_pop.models import State, Districts, City
import os

def get_upload_path(instance, filename, filetype):
    class_name = instance.__class__.__name__.lower()
    name = instance.name.replace(" ", "_") if instance.name else "unknown"
    
    ext = os.path.splitext(filename)[1]
    
    if filetype == "father":
        final_filename = f"{name}_father{ext}"
    elif filetype == "spouse":
        final_filename = f"{name}_spouse{ext}"
    else:
        final_filename = f"{name}{ext}"
    
    return os.path.join("adhikar", "person", class_name, name, final_filename)

def upload_person_photo(instance, filename):
    return get_upload_path(instance, filename, "person")

def upload_father_photo(instance, filename):
    return get_upload_path(instance, filename, "father")

def upload_spouse_photo(instance, filename):
    return get_upload_path(instance, filename, "spouse")


caste_cat = [
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OC', 'OC'),
    ]
Gender = (
    ('Male', 'Male'),
    ('Female', 'Female')
)
religion = (
    ('Hindu', 'Hindu'),
    ('Muslim', 'Muslim'),
    ('Sikh', 'Sikh'),
    ('Christian', 'Christian'),
    ('Buddhist','Buddhist')
)

class person(models.Model):
    name  = models.CharField(max_length=100,unique=True)
    dob = models.DateTimeField(null=True, blank=True)
    death_date = models.DateTimeField(null=True, blank=True)
    religion = models.CharField(max_length=100, choices=religion,null=True, blank=True)
    caste = models.CharField(max_length=100,null=True, blank=True)
    caste_category =models.CharField(max_length=10, choices=caste_cat,null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender, default='Male',null=True, blank=True)
    fathers_Name = models.CharField(max_length=100, default='',null=True, blank=True)    
    Spouse_Name = models.CharField(max_length=100, default='',null=True, blank=True)    
    Highest_Education = models.CharField(max_length=100, default='',null=True, blank=True)
    University = models.CharField(max_length=100, default='',null=True, blank=True)    
    presentaddress = models.TextField(max_length=600, default='',null=True, blank=True)
    premanentaddress = models.TextField(max_length=600, default='',null=True, blank=True)
    Email_address = models.EmailField(max_length=100, default='',null=True, blank=True)
    Mobile = models.CharField(max_length=20, default='',null=True, blank=True)
    children = models.CharField(max_length=100,null=True, blank=True)
    birth_state = models.ForeignKey(State, related_name="%(app_label)s_%(class)s_birth_state",on_delete=models.SET_NULL,null=True, blank=True)
    birth_district = models.ForeignKey(Districts,related_name="%(app_label)s_%(class)s_birth_district",  on_delete=models.SET_NULL,null=True, blank=True)
    birth_city =models.ForeignKey(City, related_name="%(app_label)s_%(class)s_birth_city",on_delete=models.SET_NULL,null=True, blank=True)
    extra_info = models.TextField(null=True, blank=True)
    person_photo = models.ImageField(upload_to=upload_person_photo, null=True, blank=True)
    fathers_image = models.ImageField(upload_to=upload_father_photo, null=True, blank=True)
    spouse_image = models.ImageField(upload_to=upload_spouse_photo, null=True, blank=True)

    class Meta:
        abstract = True  # No database table for this model
    
   
class ruling_period(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
