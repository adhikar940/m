from django.db import models
from django.contrib.contenttypes.models import ContentType

"""
This app is for creating all kind of areas like state, district, city, etc
"""

class area(models.Model):
    formationdate = models.CharField(max_length=100, null=True, blank=True)
    areasqkm =  models.IntegerField(null=True, blank=True, default=None)
    densitysqkm =   models.IntegerField(null=True, blank=True, default=None)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  ## Name of the model
    object_id = models.PositiveIntegerField()    
    ## To avoid multiple area per entity
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['content_type', 'object_id'],
                name='unique_area_per_entity'
            )
        ]
    

class population(models.Model):
    YEAR_CHOICES = [
        (2011, '2011')
    ]
    totalpopulation=  models.IntegerField(null=True, blank=True, default=None)
    malepopulation= models.IntegerField(null=True, blank=True, default=None)
    femalepopulation=  models.IntegerField(null=True, blank=True, default=None)
    census_year = models.IntegerField(choices=YEAR_CHOICES, default=2011)
    DecadalGrowthRate = models.IntegerField(null=True, blank=True, default=None)
    LiteracyRate= models.IntegerField(null=True, blank=True, default=None)
    femtomaleSexRatio= models.CharField(max_length=100, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)    
    ## To make only one population record per entity and census_year
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['content_type', 'object_id', 'census_year'],
                name='unique_entity_census_year'
            )
        ]

class State(models.Model):
    status = (
        ('State', 'State'),
        ('UT', 'UT'),
    )
    Statename = models.CharField(max_length=50,unique=True)
    capital = models.CharField(max_length=50,blank=True,default='')
    Status = models.CharField(max_length=6, choices=status, default='State')
    abbreviation = models.CharField(max_length=5, blank=True, null=True)    
    oldname = models.CharField(max_length=50,unique=True, blank=True, null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['Statename'],
                name='unique_Statename'
            )
        ]

class Districts(models.Model):
    State = models.ForeignKey(State,related_name='District', on_delete=models.CASCADE)
    Districtname = models.CharField(max_length=50)
    headquarters = models.CharField(max_length=50, null=True, blank=True)
    Revenuedivisons =  models.CharField(max_length=100, null=True, blank=True)
    mandals =  models.CharField(max_length=100, null=True, blank=True)
    abbreviation = models.CharField(max_length=5, blank=True, null=True)    
    class Meta:
        unique_together = ('State', 'Districtname')

class Taluk(models.Model):
    District = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    Talukname = models.CharField(max_length=50,unique=True)

class City(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    Cityname = models.CharField(max_length=100,unique=True)
    abbreviation = models.CharField(max_length=5, blank=True, null=True)
    
