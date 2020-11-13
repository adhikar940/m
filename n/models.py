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

class Party(models.Model):
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

class LeadingSeats(models.Model):
    MGB = models.IntegerField()
    NDA = models.IntegerField()
    LJP = models.IntegerField()
    Others = models.IntegerField()


class Parliament(models.Model):
    choices = (
        ('Rajyasabha', 'rajyasabha'),
        ('Loksabha', 'Loksabha'),
    )

    categories = models.CharField(max_length=30, choices=choices, default='Loksabha')


class RajyaSabha(Parliament):
    statename=models.CharField(max_length=30,default='Odisha')

    def __str__(self):
        return self.statename

class StatesForRajyasabha(RajyaSabha):
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

    Statename = models.CharField(max_length=30, choices=choice_states, default='Andhra Pradesh')
    MPname = models.CharField(max_length=50)
    partyname = models.CharField(max_length=50)
    fathersName = models.CharField(max_length=50)
    SpouseName=models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    HighestEducation = models.CharField(max_length=50)
    University= models.CharField(max_length=100)


    class Meta:
        abstract=True
    def __str__(self):
        return self.Statename

class AndhraPradeshforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')




class ArunachalPradeshforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')


class AssamforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')


class BiharforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class ChhattishgarhforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')
class GoaforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')


class GujaratforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class HaryanaforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class HimachalPradeshforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')


class JammuandKashmirforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')


class JharkhandforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class KarnatakaforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class KeralaforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')


class MadhyaPradeshforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')


class MaharashtraforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class ManipurforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class MeghalayaforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class MizoramforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class NagalandforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class OdishaforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class PunjabforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class RajasthanforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class SikkimforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class TamilNaduforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class TelanganaforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')


class TripuraforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')


class UttarPradeshforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')


class UttarakhandforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')

class WestBengalforRajyasabha(StatesForRajyasabha):
    photo = models.ImageField(upload_to='photo/')


class LokSabha(Parliament):
    statename = models.CharField(max_length=30,default='Odisha')

    def __str__(self):
        return self.statename


class Statesforloksabha(LokSabha):
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

    Statename = models.CharField(max_length=30, choices=choice_states, default='Andhra Pradesh')
    MPname = models.CharField(max_length=50)
    partyname = models.CharField(max_length=50)
    fathersName=models.CharField(max_length=50)
    SpouseName=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    HighestEducation = models.CharField(max_length=50)
    University = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo/')



    class Meta:
        abstract=True
    def __str__(self):
        return self.Statename

class AndhraPradesh(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class ArunachalPradesh(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Assam(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Bihar(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Chhattishgarh(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)
    


class Goa(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Gujarat(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Haryana(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class HimachalPradesh(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class JammuandKashmir(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Jharkhand(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Karnataka(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Kerala(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class MadhyaPradesh(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Maharashtra(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Manipur(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Meghalaya(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Mizoram(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Nagaland(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Odisha(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Punjab(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Rajasthan(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Sikkim(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class TamilNadu(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Telangana(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Tripura(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class UttarPradesh(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class Uttarakhand(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)


class WestBengal(Statesforloksabha):
    constituencyName = models.CharField(max_length=30)





