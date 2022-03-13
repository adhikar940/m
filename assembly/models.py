from django.db import models
from n.models import *
from party.models import Party1
class Assembly_Constituency1(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    Assembly_Constituency_Name = models.CharField(max_length=100)
    class Meta:
        unique_together = ['Assembly_Constituency_Name']
        ordering = ['Assembly_Constituency_Name']
    def __str__(self):
        return '%s' %(self.Assembly_Constituency_Name)

class Legislative_Assembly1(Parliament):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True,
                              default='')
    District = models.ForeignKey(Districts, on_delete=models.CASCADE,
                                 null=True, default='')
    MLA_name = models.CharField(max_length=300, default='')
    Party = models.ForeignKey(Party1,  on_delete=models.SET_NULL, null=True)
    constituency_name = models.ForeignKey(Assembly_Constituency1, on_delete=models.CASCADE, null=True, default='')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')
    class Meta:
        unique_together = ['MLA_name']
        ordering = ['MLA_name']

    def __str__(self):
        return str(self.MLA_name)
class assemblypersonal1(personal):
    mla = models.ForeignKey(Legislative_Assembly1, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['mla']
    def __str__(self):
        return '%s' % (self.mla)
class assemblyterm(models.Model):
    mla = models.ForeignKey(Legislative_Assembly1, on_delete=models.SET_NULL, null=True,)
    year =  models.IntegerField(blank=True)
    month = models.IntegerField(choices=[(i, i) for i in range(1, 13)], blank=True)
    date = models.IntegerField(choices=[(i, i) for i in range(1, 32)], blank=True)
    class Meta:
        unique_together = ['mla','year','month','date']
    def __str__(self):
        return '%s' % (self.mla)
class excelupload(models.Model):
    excelfileupload = models.FileField(upload_to = '')
