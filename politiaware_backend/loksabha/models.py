from django.db import models
from area_pop.models import State,Districts
from party.models import Party
from person.models import person

class LoksabhaConstituency(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    District = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    LoksabhaConstituencyName = models.CharField(max_length=100)
    isexist= models.BooleanField(default=True,null=True, blank=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['State','District','LoksabhaConstituencyName'],
                name='unique_loksabhaconstituency'
            )
        ]       

class LokSabhaMP(person):    
    Party = models.ForeignKey(Party,on_delete=models.CASCADE, null=True,default='')
    ispresent = models.BooleanField(default=True,null=True, blank=True)
    constituency = models.ForeignKey(LoksabhaConstituency, on_delete=models.SET_NULL, null=True)
    #actvated = models.CharField(max_length=500, choices=choice2, default='no')
    class Meta:
        unique_together = ['name']
    
'''class loksabhapersonal1(personal):
    mp = models.ForeignKey(LokSabha, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['mp']
    def __str__(self):
        return '%s' % (self.mp)'''
###############################################################################################################
#           SESSIONS MODELS- Loksabha
###############################################################################################################
# Loksabha Individual Sessions
'''class Loksabha_Session(models.Model):
    Loksabha_MP_Name = models.ForeignKey(LokSabha, on_delete=models.SET_NULL, null=True, default='')
    Session_Title = models.ForeignKey(Sessions,on_delete=models.CASCADE, null=True, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link = models.CharField(max_length=1000, default='')

    def __str__(self):
        k = str(self.Loksabha_MP_Name)+'-'+str(self.Session_Title)+'-'+str(self.date)
        return (k)
    class Meta:
        ordering = ['-date']
# Loksabha Complete Sessions
class Loksabha_Complete_Session1(models.Model):
    Loksabha_Session_Title = models.ForeignKey(Sessions,on_delete=models.CASCADE, null=True, default='')

    Description = models.CharField(max_length=100, default='')
    date = models.DateField()
    session = models.TextField(default='')
    video_link = models.CharField(max_length=1000, default='')

    def __str__(self):
        return str(self.Loksabha_Session_Title)+'-'+str(self.date)
    class Meta:
        ordering = ['-date']'''
