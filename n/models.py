from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=32)


class State(models.Model):

    State_name = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.State_name)


class Districts(models.Model):

    State = models.ForeignKey(State, on_delete=models.CASCADE)
    District_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.District_name)


class City(models.Model):

    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    City_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.City_name)


class Ecandidates(models.Model):

    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    partyname = models.CharField(max_length=100, default='')
    Candidate = models.CharField(max_length=100, default='')
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    Residence = models.TextField(max_length=200, default='')
    Photo = models.ImageField(upload_to='photo/', default='')
    
    class Meta:
        abstract = True

    def __str__(self):
        return str(self.State)


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
        return str(self.State)


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
        return str(self.partyname)


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
        return str(self.partyname)


class LeadingSeats(models.Model):
    MGB = models.IntegerField()
    NDA = models.IntegerField()
    LJP = models.IntegerField()
    Others = models.IntegerField()


class States(models.Model):
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    capital = models.CharField(max_length=100, default='', unique=True)
    chief_minister = models.CharField(max_length=100, default='')
    chief_minister_Photo = models.ImageField(upload_to='photo/', null=True)
    Governor = models.CharField(max_length=100, default='')
    Governor_Photo = models.ImageField(upload_to='photo/', null=True)

    def __str__(self):
        return str(self.State)


class Parliament(models.Model):

    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    partyname = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=Gender, default='Male')
    fathersName = models.CharField(max_length=100, default='')
    SpouseName = models.CharField(max_length=100, default='')
    HighestEducation = models.CharField(max_length=100, default='')
    University = models.CharField(max_length=100,  default='')
    photo = models.ImageField(upload_to='photo/', null=True)
    address = models.TextField(max_length=600, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.State)


class Rajyasabha(Parliament):

    MPname = models.CharField(max_length=300, default='')

    def __str__(self):
        return str(self.State)


class LokSabha(Parliament):

    MPname = models.CharField(max_length=300, default='')
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    constituency_name = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.State)

class Legislative_Assembly(Parliament):

    MLA_name = models.CharField(max_length=300, default='')
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    constituency_name = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.State)

class Legislative_Council_Presence(models.Model):
    status = (
        ('Present', 'Present'),
        ('Absent', 'Absent')
    )
    presence = models.CharField(max_length=10, choices=status, default='Present')
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.State)

class Time_period(models.Model):
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    End_date = models.DateField()
    partyname = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=Gender, default='Male')
    fathersName = models.CharField(max_length=100, default='')
    SpouseName = models.CharField(max_length=100, default='')
    HighestEducation = models.CharField(max_length=100, default='')
    University = models.CharField(max_length=100,  default='')
    photo = models.ImageField(upload_to='photo/', null=True)
    address = models.TextField(max_length=600, default='')



    class Meta:
        abstract = True

    def __str__(self):
        return str(self.State)


class Assembly_time_period(Time_period):

    def __str__(self):
        return str(self.State)


class Panchayat_time_period(Time_period):

    def __str__(self):
        return str(self.State)


class Municipal_corporation_time_period(Time_period):

    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True)
    City = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, default='')
    corporation_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.State)


class Panchayat_and_corporation(models.Model):
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True,  default='')
    Districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True,  default='')
    partyname = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=Gender, default='Male')
    fathersName = models.CharField(max_length=100, default='')
    SpouseName = models.CharField(max_length=100, default='')
    HighestEducation = models.CharField(max_length=100, default='')
    University = models.CharField(max_length=100,  default='')
    photo = models.ImageField(upload_to='photo/', null=True)
    address = models.TextField(max_length=600, default='')


    class Meta:
        abstract = True

    def __str__(self):
        return str(self.State)


class Grama_panchayat(Panchayat_and_corporation):

    Mandal = models.CharField(max_length=100, default='')
    panchayat_name = models.CharField(max_length=100, default='')
    Sarpanch_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.State)


class Corporation(Panchayat_and_corporation):

    City = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, default='')
    Corporation_name = models.CharField(max_length=100, default='')
    partyname = models.CharField(max_length=100, default='')
    Mayor_name = models.CharField(max_length=100, default='')


    def __str__(self):
        return str(self.State)


class Panchayat_Ward_Number(Panchayat_and_corporation):

    Mandal = models.CharField(max_length=100, default='')
    panchayat_name = models.CharField(max_length=100, default='')
    Ward_Member_Name = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.State)


class Corporation_Ward_Number(Panchayat_and_corporation):

    City = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, default='')
    Ward_name = models.CharField(max_length=100, default='')
    partyname = models.CharField(max_length=100, default='')
    Corporator_name = models.CharField(max_length=100, default='')


    def __str__(self):
        return str(self.State)
