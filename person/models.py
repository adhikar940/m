from django.db import models
from area_pop.models import State, Districts, City
import os

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
)

class person(models.Model):
    name  = models.CharField(max_length=100,unique=True)
    dob = models.DateTimeField(null=True, blank=True)
    death_date = models.DateTimeField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    religion = models.CharField(max_length=100, choices=religion,null=True, blank=True)
    caste = models.CharField(max_length=100,null=True, blank=True)
    caste_category =models.CharField(max_length=10, choices=caste_cat,null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender, default='Male',null=True, blank=True)
    fathers_Name = models.CharField(max_length=100, default='',null=True, blank=True)
    fathers_image = models.TextField(null=True, blank=True)
    Spouse_Name = models.CharField(max_length=100, default='',null=True, blank=True)
    spouse_image = models.TextField(null=True, blank=True)
    Highest_Education = models.CharField(max_length=100, default='',null=True, blank=True)
    University = models.CharField(max_length=100, default='',null=True, blank=True)
    photo = models.ImageField(upload_to='person_photo/', null=True, blank=True)
    photo_path = models.TextField(null=True, blank=True)
    address = models.TextField(max_length=600, default='',null=True, blank=True)
    Email_address = models.EmailField(max_length=100, default='',null=True, blank=True)
    Mobile = models.CharField(max_length=20, default='',null=True, blank=True)
    children = models.CharField(max_length=100,null=True, blank=True)
    birth_state = models.ForeignKey(State, related_name="%(app_label)s_%(class)s_birth_state",on_delete=models.SET_NULL,null=True, blank=True)
    birth_district = models.ForeignKey(Districts,related_name="%(app_label)s_%(class)s_birth_district",  on_delete=models.SET_NULL,null=True, blank=True)
    birth_city =models.ForeignKey(City, related_name="%(app_label)s_%(class)s_birth_city",on_delete=models.SET_NULL,null=True, blank=True)
    extra_info = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True  # No database table for this model
    
    def save(self, *args, **kwargs):
        if self.photo:
            self.photo_path = os.path.join('person_photo/', self.photo.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the person.        
        This method returns the name of the person and name is visualized in admin panel
        """
        return self.name

class ruling_period(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
