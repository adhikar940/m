from django.db import models
from area_pop.models import State,Districts
from party.models import Party
from person.models import person
class Rajyasabhapresedential1(person):
    choice = (
        ('Legislature', 'Legislature'),
        ('President', 'President')
    )
    #state = models.ForeignKey(State, on_delete=models.CASCADE, null=True,default='')
    MP_name = models.CharField(max_length=300, default='')
    #Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    field = models.CharField(max_length=300, default='')
    elected = models.CharField(max_length=500, choices=choice, default='President')
    is_present = models.BooleanField(default=True,null=True, blank=True)
    #actvated = models.CharField(max_length=500, choices=choice2, default='no')
    class Meta:
        unique_together = ['MP_name']
        ordering = ['MP_name']

    def __str__(self):
        return str(self.MP_name)
class Rajyasabha1(person):
    choice = (
        ('Legislature', 'Legislature'),
        ('President', 'President')
    )
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True,
                              default='')
    MP_name = models.CharField(max_length=300, default='')
    Party = models.ForeignKey(Party,on_delete=models.SET_NULL, null=True)
    elected = models.CharField(max_length=500, choices=choice, default='Legislature')
    is_present = models.BooleanField(default=True,null=True, blank=True)
    #actvated = models.CharField(max_length=500, choices=choice2, default='no')
    class Meta:
        unique_together = ['MP_name']
        ordering = ['MP_name']

    def __str__(self):
        return str(self.MP_name)+'-'+str(self.state)
'''class rajyasabhapersonal1(personal):
    mp = models.ForeignKey(Rajyasabha1, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['mp']

    def __str__(self):
        return '%s' % (self.mp)'''

class Rajyasabhaterm(models.Model):
    Rajyasabha_MP_Name = models.ForeignKey(Rajyasabha1, on_delete=models.SET_NULL, null=True, default='')
    year =  models.IntegerField(blank=True)
    month = models.IntegerField(choices=[(i, i) for i in range(1, 13)], blank=True)
    date = models.IntegerField(choices=[(i, i) for i in range(1, 32)], blank=True)
    class Meta:
        unique_together = ['Rajyasabha_MP_Name','year','month','date']
    def __str__(self):
        return '%s' % (self.Rajyasabha_MP_Name)


#$#### SESSIONS
# Rajyasabha Individual Sessions
'''class Rajyasabha_Session1(models.Model):
    Rajyasabha_MP_Name = models.ForeignKey(Rajyasabha1, on_delete=models.SET_NULL, null=True, default='')
    Session_Title = models.ForeignKey(Sessions, on_delete=models.CASCADE, null=True, default='')
    date = models.DateField()
    session = models.TextField(default='')
    link =  models.CharField(max_length=1000, default='')

    def __str__(self):
        return str(self.Session_Title)
    class Meta:
        ordering = ['-date']
# Rajyasabha Complete Sessions
class Rajyasabha_Complete_Session1(models.Model):
    Session_Title = models.ForeignKey(Sessions,on_delete=models.CASCADE, null=True, default='')
    Description = models.CharField(max_length=100, default='')
    date = models.DateField()
    session = models.TextField(default='')
    video_link = models.CharField(max_length=1000, default='')

    def __str__(self):
        return str(self.Session_Title)+'-'+str(self.date)
    class Meta:
        ordering = ['-date']'''
