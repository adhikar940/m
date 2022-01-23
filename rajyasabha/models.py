from django.db import models
from n.models import *
'''class Rajyasabhapresedential1(Parliament):
    choice = (
        ('Legislature', 'Legislature'),
        ('President', 'President')
    )
    #state = models.ForeignKey(State, on_delete=models.CASCADE, null=True,default='')
    MP_name = models.CharField(max_length=300, default='')
    #Party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    field = models.CharField(max_length=300, default='')
    elected = models.CharField(max_length=500, choices=choice, default='President')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')
    class Meta:
        unique_together = ['MP_name']
        ordering = ['MP_name']

    def __str__(self):
        return str(self.MP_name)
class Rajyasabha1(Parliament):
    choice = (
        ('Legislature', 'Legislature'),
        ('President', 'President')
    )
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True,
                              default='')
    MP_name = models.CharField(max_length=300, default='')
    Party = models.ForeignKey(Party,on_delete=models.SET_NULL, null=True)
    elected = models.CharField(max_length=500, choices=choice, default='Legislature')
    presentorx = models.CharField(max_length=500, choices=choice1, default='present')
    actvated = models.CharField(max_length=500, choices=choice2, default='no')
    Termend =  models.DateField(default='0001-01-01')
    class Meta:
        unique_together = ['MP_name']
        ordering = ['MP_name']

    def __str__(self):
        return str(self.MP_name)+'-'+str(self.state)
class rajyasabhapersonal1(personal):
    mp = models.ForeignKey(Rajyasabha1, on_delete=models.SET_NULL, null=True,)
    class Meta:
        unique_together = ['mp']

    def __str__(self):
        return '%s' % (self.mp)
'''
