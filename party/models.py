from django.db import models

class candidate_inparty_period(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


class Party(models.Model):
    choice = (
        ('Regional', 'regional'),
        ('National', 'national'),
    )
    PARTY_COLOR_CHOICES = [
        ('#FF9933', 'BJP - Orange'),
        ('#00A2E8', 'INC - Blue'),
        ('#000000', 'CPI(M) - Black'),
        ('#FF0000', 'CPI - Red'),
        ('#008000', 'BSP - Green'),
        ('#FFD700', 'TMC - Yellow'),
        ('#FF4500', 'Shiv Sena - Saffron'),
        ('#A52A2A', 'DMK - Brown'),
        ('#000080', 'AIADMK - Navy Blue'),
        ('#800080', 'AAP - Purple'),
        ('#FFFFFF', 'None/Independent - White'),
    ]
    party_color = models.CharField(
        max_length=7,
        choices=PARTY_COLOR_CHOICES,
        default='#FFFFFF',
        help_text="Select party color"
    )
    partystatus = models.CharField(max_length=30, choices=choice)
    partyname = models.CharField(max_length=100)
    abbreviation = models.CharField(null=True, max_length=20, unique=True)
    President = models.CharField(max_length=100, null=True)
    founder = models.CharField(max_length=100, null=True)
    chairperson = models.CharField(max_length=100, null=True)
    foundeddate = models.DateField()
    headquarters = models.CharField(max_length=1000, null=True)
    partysymbol = models.ImageField(upload_to='Party/party_symbol/%Y-%m-%d/%H-%M-%S', null=True)
    founderPhoto = models.ImageField(upload_to='Party/founderPhoto/%Y-%m-%d/%H-%M-%S', null=True)
    chairpersonPhoto = models.ImageField(upload_to='Party/chairpersonPhoto/%Y-%m-%d/%H-%M-%S', null=True)
    PresidentPhoto = models.ImageField(upload_to='Party/PresidentPhoto/%Y-%m-%d/%H-%M-%S', null=True)
    #actvated = models.CharField(max_length=20, choices=choice2, default='no')
    #stateactivated = models.CharField(max_length=10000, default='no')
    #districtactivated = models.CharField(max_length=10000, default='no')
    def __str__(self):
        return str(self.abbreviation)
'''class statepartyactivate1(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    email = models.CharField(max_length=64)
    class Meta:
        ordering = ['state']
        unique_together = ('party', 'state')
    def __str__(self):
        return str(self.party)+str(self.state)
class districtpartyactivate1(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE,default='')
    district =  models.ForeignKey(Districts, on_delete=models.CASCADE)
    email = models.CharField(max_length=64)
    class Meta:
        ordering = ['state']
        unique_together = ('party', 'district')
    def __str__(self):
        return str(self.party)+str(self.district)'''
