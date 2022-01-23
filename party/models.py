from django.db import models
from n.models import *
class Party1(models.Model):
    choice = (
        ('Regional', 'regional'),
        ('National', 'national'),
    )
    party_status = models.CharField(max_length=30, choices=choice)
    partyname = models.CharField(max_length=100)
    abbreviation = models.CharField(null=True, max_length=20, unique=True)
    President = models.CharField(max_length=100, null=True)
    founder = models.CharField(max_length=100, null=True)
    chairperson = models.CharField(max_length=100, null=True)
    founded_date = models.DateField()
    headquarters = models.CharField(max_length=1000)
    seats_in_rajyasabha = models.IntegerField()
    seats_in_loksabha = models.IntegerField()
    party_symbol = models.ImageField(upload_to='Party/party_symbol/%Y-%m-%d/%H-%M-%S', null=True)
    founderPhoto = models.ImageField(upload_to='Party/founderPhoto/%Y-%m-%d/%H-%M-%S', null=True)
    chairpersonPhoto = models.ImageField(upload_to='Party/chairpersonPhoto/%Y-%m-%d/%H-%M-%S', null=True)
    actvated = models.CharField(max_length=20, choices=choice2, default='no')
    #stateactivated = models.CharField(max_length=10000, default='no')
    #districtactivated = models.CharField(max_length=10000, default='no')
    def __str__(self):
        return str(self.abbreviation)
class statepartyactivate1(models.Model):
    party = models.ForeignKey(Party1, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    email = models.CharField(max_length=64)
    class Meta:
        ordering = ['state']
        unique_together = ('party', 'state')
    def __str__(self):
        return str(self.party)+str(self.state)
class districtpartyactivate1(models.Model):
    party = models.ForeignKey(Party1, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE,default='')
    district =  models.ForeignKey(Districts, on_delete=models.CASCADE)
    email = models.CharField(max_length=64)
    class Meta:
        ordering = ['state']
        unique_together = ('party', 'district')
    def __str__(self):
        return str(self.party)+str(self.district)
