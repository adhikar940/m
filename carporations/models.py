from django.db import models
from n.models import *
from party.models import *
class municipalcarporation(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    City = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, default='')
    corporation_name = models.CharField(max_length=100, default='')
    formationdate =  models.CharField(max_length=100, default='')
    population = models.CharField(max_length=100, default='')
    lastelectionyear = models.CharField(max_length=100, default='')
    areainkm2 = models.CharField(max_length=100, default='')
    def __str__(self):
        return str(self.corporation_name)
class Mayor(Parliament):
    Mayor_Name = models.CharField(max_length=100, default='')
    party = models.ForeignKey(Party1, on_delete=models.SET_NULL, null=True)
    corporation = models.ForeignKey(municipalcarporation, on_delete=models.SET_NULL, null=True)
class mayorpersonal1(personal):
    mayor = models.ForeignKey(Mayor, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['mayor']
    def __str__(self):
        return '%s' % (self.mayor)
class deputymayor(Parliament):
    DeputyMayor_Name = models.CharField(max_length=100, default='')
    party = models.ForeignKey(Party1, on_delete=models.SET_NULL, null=True)
    corporation = models.ForeignKey(municipalcarporation, on_delete=models.SET_NULL, null=True)
class deputymayorpersonal1(personal):
    deputymayor = models.ForeignKey(deputymayor, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['deputymayor']
    def __str__(self):
        return '%s' % (self.deputymayor)
