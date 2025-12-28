from django.db import models
from n.models import *
from party.models import Party1
class Legislative_councils1(Parliament):
    elected = (
        ('Members of Local Body', 'Members of Local Body'),
        ('Members of legislative body', 'Members of Legislative Body'),
        ('Governor', 'Governor'),
        ('Graduates of three years', 'Graduates of three years'),
        ('University teacher of three years', 'University teacher of three years')
    )
    state = models.ForeignKey(State, on_delete=models.CASCADE,
                              null=True, default='')
    elected = models.CharField(max_length=500, choices=elected, default='Governor')
    MLC_name = models.CharField(max_length=300, default='')
    Districts = models.CharField(max_length=100,default='')
    constituency_name = models.CharField(max_length=200, default='')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')
    party = models.ForeignKey(Party1,on_delete=models.CASCADE, null=True, default='')
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    class Meta:
        unique_together = ['MLC_name']

    def __str__(self):
        return str(self.MLC_name)
class councilpersonal1(personal):
    mlc = models.ForeignKey(Legislative_councils1, on_delete=models.SET_NULL, null=True)
    class Meta:
        unique_together = ['mlc']
    def __str__(self):
        return '%s' % (self.mlc)
class councilterm(models.Model):
    mlc = models.ForeignKey(Legislative_councils1, on_delete=models.SET_NULL, null=True)
    year =  models.IntegerField(blank=True)
    month = models.IntegerField(choices=[(i, i) for i in range(1, 13)], blank=True)
    date = models.IntegerField(choices=[(i, i) for i in range(1, 32)], blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True, default='')
    class Meta:
        unique_together = ['mlc','year','month','date']
    def __str__(self):
        return '%s' % (self.mlc)
