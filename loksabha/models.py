from django.db import models
from n.models import *
from party.models import Party1
class LokSabha1(Parliament):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True,
                              default='')
    MP_name = models.CharField(max_length=300, null=True)
    Party = models.ForeignKey(Party1,on_delete=models.CASCADE, null=True,default='')
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    constituency_name = models.CharField(max_length=200, default='')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')
    class Meta:
        unique_together = ['MP_name']
        ordering = ['MP_name']
    def __str__(self):
        return '%s: %s' % (self.state, self.MP_name)
class loksabhapersonal1(personal):
    mp = models.ForeignKey(LokSabha, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['mp']
    def __str__(self):
        return '%s' % (self.mp)
###############################################################################################################
#           SESSIONS MODELS- Loksabha
###############################################################################################################
# Loksabha Individual Sessions
class Loksabha_Session1(models.Model):
    Loksabha_MP_Name = models.ForeignKey(LokSabha1, on_delete=models.SET_NULL, null=True, default='')
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
        ordering = ['-date']
