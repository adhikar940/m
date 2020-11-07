from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=32)


class Ecandidates(models.Model):
    choice_states = (
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya  Pradesh', 'Madhya  Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal')
    )

    Statename = models.CharField(max_length=30, choices=choice_states,default='')
    partyname = models.CharField(max_length=100,default='')
    Candidate = models.CharField(max_length=100,default='')
    
    District_name = models.CharField(max_length=100,default='')
    Residence = models.TextField(max_length=200, default='')
    Photo = models.ImageField(upload_to='photo/', default='')
    
    class Meta:
        abstract=True
    def __str__(self):
        return self.Statename

class BiharCandidate(Ecandidates):
    constituency_name = models.CharField(max_length=100,default='')
    


class BiharWinners(Ecandidates):
    constituency_name = models.CharField(max_length=100,default='',unique='True')
    total_contested = models.IntegerField()
    no_of_votes = models.IntegerField()


class BiharRunners(Ecandidates):
    constituency_name = models.CharField(max_length=100,default='',unique='True')
    total_contested = models.IntegerField()
    no_of_votes = models.IntegerField()

class DubbakaCandidate(Ecandidates):
    constituency_name = models.CharField(max_length=100,default='')
    


class DubbakaWinners(Ecandidates):
    constituency_name = models.CharField(max_length=100,default='',unique='True')
    total_contested = models.IntegerField()
    no_of_votes = models.IntegerField()


class DubbakaRunners(Ecandidates):
    constituency_name = models.CharField(max_length=100,default='',unique='True')
    total_contested = models.IntegerField()
    no_of_votes = models.IntegerField()

    def __str__(self):
        return self.Statename

class Bihar_Coalition_Party(models.Model):
    choice = (
        ('Regional', 'regional'),
        ('National', 'national'),
    )
    party_status= models.CharField(max_length=30, choices=choice)
    partyname = models.CharField(max_length = 100)
    abbreviation = models.CharField(null=True, max_length=20)
    President = models.CharField(max_length = 100,null=True)
    founder = models.CharField(max_length = 100,null=True)
    chairperson = models.CharField(max_length = 100, null=True)
    founded_date = models.DateField()
    headquarters = models.CharField(max_length = 1000)
    seats_in_rajyasabha = models.IntegerField()
    seats_in_loksabha = models.IntegerField()
    party_symbol = models.ImageField(upload_to='photo/', null=True)
    founderPhoto = models.ImageField(upload_to='photo/', null=True)
    chairpersonPhoto = models.ImageField(upload_to='photo/', null=True)

    def __str__(self):
        return self.partyname

class Bihar_Party(models.Model):
    choice = (
        ('Regional', 'regional'),
        ('National', 'national'),
    )
    party_status= models.CharField(max_length=30, choices=choice)
    partyname = models.CharField(max_length = 100)
    abbreviation = models.CharField(null=True, max_length=20)
    President = models.CharField(max_length = 100,null=True)
    founder = models.CharField(max_length = 100,null=True)
    chairperson = models.CharField(max_length = 100, null=True)
    founded_date = models.DateField()
    headquarters = models.CharField(max_length = 1000)
    seats_in_rajyasabha = models.IntegerField()
    seats_in_loksabha = models.IntegerField()
    party_symbol = models.ImageField(upload_to='photo/', null=True)
    founderPhoto = models.ImageField(upload_to='photo/', null=True)
    chairpersonPhoto = models.ImageField(upload_to='photo/', null=True)

    def __str__(self):
        return self.partyname


