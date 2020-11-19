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

    Statename = models.CharField(max_length=30, choices=choice_states, default='')
    partyname = models.CharField(max_length=100, default='')
    Candidate = models.CharField(max_length=100, default='')
    District_name = models.CharField(max_length=100, default='')
    Residence = models.TextField(max_length=200, default='')
    Photo = models.ImageField(upload_to='photo/', default='')
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.Statename


class BiharCandidate(Ecandidates):
    constituency_name = models.CharField(max_length=100, default='')
    

class BiharWinners(Ecandidates):
    constituency_name = models.CharField(max_length=100, default='', unique='True')
    total_contested = models.IntegerField()
    no_of_votes = models.IntegerField()


class BiharRunners(Ecandidates):
    constituency_name = models.CharField(max_length=100, default='', unique='True')
    total_contested = models.IntegerField()
    no_of_votes = models.IntegerField()


class DubbakaCandidate(Ecandidates):
    constituency_name = models.CharField(max_length=100, default='')
    

class DubbakaWinners(Ecandidates):
    constituency_name = models.CharField(max_length=100, default='', unique='True')
    total_contested = models.IntegerField()
    no_of_votes = models.IntegerField()


class DubbakaRunners(Ecandidates):
    constituency_name = models.CharField(max_length=100, default='', unique='True')
    total_contested = models.IntegerField()
    no_of_votes = models.IntegerField()

    def __str__(self):
        return self.Statename


class Bihar_Coalition_Party(models.Model):
    choice = (
        ('Regional', 'regional'),
        ('National', 'national'),
    )
    party_status = models.CharField(max_length=30, choices=choice)
    partyname = models.CharField(max_length=100)
    abbreviation = models.CharField(null=True, max_length=20)
    President = models.CharField(max_length=100, null=True)
    founder = models.CharField(max_length=100, null=True)
    chairperson = models.CharField(max_length=100, null=True)
    founded_date = models.DateField()
    headquarters = models.CharField(max_length=1000)
    seats_in_rajyasabha = models.IntegerField()
    seats_in_loksabha = models.IntegerField()
    party_symbol = models.ImageField(upload_to='photo/', null=True)
    founderPhoto = models.ImageField(upload_to='photo/', null=True)
    chairpersonPhoto = models.ImageField(upload_to='photo/', null=True)

    def __str__(self):
        return self.partyname


class Party(models.Model):
    choice = (
        ('Regional', 'regional'),
        ('National', 'national'),
    )
    party_status = models.CharField(max_length=30, choices=choice)
    partyname = models.CharField(max_length=100)
    abbreviation = models.CharField(null=True, max_length=20)
    President = models.CharField(max_length=100, null=True)
    founder = models.CharField(max_length=100, null=True)
    chairperson = models.CharField(max_length=100, null=True)
    founded_date = models.DateField()
    headquarters = models.CharField(max_length=1000)
    seats_in_rajyasabha = models.IntegerField()
    seats_in_loksabha = models.IntegerField()
    party_symbol = models.ImageField(upload_to='photo/', null=True)
    founderPhoto = models.ImageField(upload_to='photo/', null=True)
    chairpersonPhoto = models.ImageField(upload_to='photo/', null=True)

    def __str__(self):
        return self.partyname

class LeadingSeats(models.Model):
    MGB = models.IntegerField()
    NDA = models.IntegerField()
    LJP = models.IntegerField()
    Others = models.IntegerField()

class States(models.Model):
    State_name = models.CharField(max_length=100, default='', unique=True)
    capital = models.CharField(max_length=100, default='', unique=True)
    chief_minister = models.CharField(max_length=100, default='')
    chief_minister_Photo = models.ImageField(upload_to='photo/', null=True)
    Governor = models.CharField(max_length=100, default='')
    Governor_Photo = models.ImageField(upload_to='photo/', null=True)

    def __str__(self):
        return self.State_name

class Parliament(models.Model):

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
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    Statename = models.CharField(max_length=100, choices=choice_states, default='Andhra Pradesh')
    MPname = models.CharField(max_length=100, default='')
    partyname = models.CharField(max_length=100, default='')
    constituency_name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=Gender, default='Male')
    fathersName = models.CharField(max_length=100, default='')
    SpouseName = models.CharField(max_length=100, default='')
    HighestEducation = models.CharField(max_length=100, default='')
    University = models.CharField(max_length=100,  default='')
    photo = models.ImageField(upload_to='photo/', null=True)
    address = models.TextField(max_length=200, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return self.Statename

class Rajyasabha(Parliament):

    def __str__(self):
        return self.Statename

class LokSabha(Parliament):

    def __str__(self):
        return self.Statename

class Time_period(models.Model):

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

    State_name = models.CharField(max_length=100, choices=choice_states, default='Andhra Pradesh')
    start_date = models.DateField()
    End_date = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.Statename


class Assembly_time_period(Time_period):

    def __str__(self):
        return self.Statename

class Panchayat_time_period(Assembly_time_period):

    def __str__(self):
        return self.Statename

class Municipal_corporation_time_period(Assembly_time_period):

    District_name = models.CharField(max_length=100, default='')
    City_name = models.CharField(max_length=100, default='')
    corporation_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.Statename

